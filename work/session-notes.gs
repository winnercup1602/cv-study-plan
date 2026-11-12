const CODE_PROPERTY = 'registrationCode';
const NOTE_PREFIX = 'note:';

function doGet() {
  const properties = PropertiesService.getScriptProperties().getProperties();
  const notes = Object.keys(properties)
    .filter(key => key.startsWith(NOTE_PREFIX))
    .map(key => JSON.parse(properties[key]))
    .sort((left, right) => left.createdAt.localeCompare(right.createdAt));
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

  const session = Number(data.session);
  const title = (data.title || '').trim();
  const url = (data.url || '').trim();
  const webUrl = /^https?:\/\/(?:\[[\da-f:.]+\]|[a-z\d.-]+)(?::\d{1,5})?(?:[/?#][^\s\\]*)?$/i;
  if (!Number.isSafeInteger(session) || session < 1 || !title ||
      title.length > 120 || url.length > 2048 || !webUrl.test(url) ||
      /[\u0000-\u001f\u007f]/.test(title + url)) {
    return json_({ ok: false, error: 'invalid' });
  }

  // The same URL can be added to different sessions. Retries within one
  // session return the original note, including its title.
  const digest = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, session + '\n' + url);
  const id = Utilities.base64EncodeWebSafe(digest).replace(/=+$/, '');
  const key = NOTE_PREFIX + id;
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return json_({ ok: false, error: 'unavailable' });
  try {
    const saved = properties.getProperty(key);
    if (saved) return json_({ ok: true, note: JSON.parse(saved), duplicate: true });
    const note = { id, session, title, url, createdAt: new Date().toISOString() };
    properties.setProperty(key, JSON.stringify(note));
    return json_({ ok: true, note });
  } finally {
    lock.releaseLock();
  }
}

function json_(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
