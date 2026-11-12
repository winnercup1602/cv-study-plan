const CODE_PROPERTY = 'registrationCode';
const NOTE_PREFIX = 'note:';

function doGet() {
  const notes = readNotes_(PropertiesService.getScriptProperties())
    .sort((left, right) => left.createdAt.localeCompare(right.createdAt))
    .map(publicNote_);
  return json_({ ok: true, notes });
}

function doPost(event) {
  const data = event.parameter;
  const properties = PropertiesService.getScriptProperties();
  const code = properties.getProperty(CODE_PROPERTY);
  if (!code) return json_({ ok: false, error: 'unavailable' });
  if (!data.code || data.code !== code) {
    return json_({ ok: false, error: 'code' });
  }

  const action = data.action || 'add';
  const session = Number(data.session);
  const url = (data.url || '').trim();
  const webUrl = /^https?:\/\/(?:\[[\da-f:.]+\]|[a-z\d.-]+)(?::\d{1,5})?(?:[/?#][^\s\\]*)?$/i;
  if (!['add', 'update', 'delete'].includes(action) ||
      !Number.isSafeInteger(session) || session < 1 ||
      (action !== 'add' && (!/^[a-z\d_-]{16,64}$/i.test(data.id || '') || !data.previousUrl)) ||
      (action !== 'delete' && (url.length > 2048 || !webUrl.test(url) || /[\u0000-\u001f\u007f]/.test(url)))) {
    return json_({ ok: false, error: 'invalid' });
  }

  const lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return json_({ ok: false, error: 'unavailable' });
  try {
    const key = NOTE_PREFIX + (action === 'add' ? Utilities.getUuid() : data.id);
    const stored = action === 'add' ? null : properties.getProperty(key);
    const current = stored && JSON.parse(stored);
    if (current && current.session !== session) return json_({ ok: false, error: 'missing' });
    if (action === 'update' && !current) return json_({ ok: false, error: 'missing' });
    if (action === 'update' && current.url === url) return json_({ ok: true, note: publicNote_(current) });
    if (current && current.url !== data.previousUrl) return json_({ ok: false, error: 'conflict' });
    if (action === 'delete') {
      if (current) properties.deleteProperty(key);
      return json_({ ok: true, removed: data.id });
    }

    const duplicate = readNotes_(properties).find(note => note.session === session && note.url === url);
    if (duplicate) {
      return action === 'add'
        ? json_({ ok: true, note: publicNote_(duplicate), duplicate: true })
        : json_({ ok: false, error: 'duplicate' });
    }
    const note = {
      id: current ? current.id : key.slice(NOTE_PREFIX.length),
      session,
      url,
      createdAt: current ? current.createdAt : new Date().toISOString(),
    };
    properties.setProperty(key, JSON.stringify(note));
    return json_({ ok: true, note: publicNote_(note) });
  } finally {
    lock.releaseLock();
  }
}

function readNotes_(properties) {
  const values = properties.getProperties();
  return Object.keys(values).filter(key => key.startsWith(NOTE_PREFIX))
    .map(key => JSON.parse(values[key]));
}

function publicNote_(note) {
  // Previously published pages use title as their link text.
  const { id, session, url, createdAt } = note;
  return { id, session, url, createdAt, title: url };
}

function json_(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
