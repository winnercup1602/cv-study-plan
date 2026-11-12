(() => {
  const endpoint = 'https://script.google.com/macros/s/AKfycbxjegCNCDm3UiXGaAbO6yGcVL9hl39YiN4V6vEvI9z6fQM5lNsUjtAtd3k4nTlzQY3F_w/exec';
  const template = document.querySelector('#session-notes-template');
  const cards = new Map();
  let registrationCode = '';

  function webUrl(value) {
    try {
      const url = new URL(value);
      if (['http:', 'https:'].includes(url.protocol) && !url.username && !url.password) {
        return url.href;
      }
    } catch {
      return null;
    }
    return null;
  }

  async function request(body) {
    const response = await fetch(endpoint, {
      method: body ? 'POST' : 'GET',
      body,
      credentials: 'omit',
      cache: 'no-store',
      signal: AbortSignal.timeout(15000),
    });
    if (!response.ok) throw new Error('Notes request failed');
    return response.json();
  }

  function showNote(note) {
    const url = webUrl(note.url);
    if (!url || !cards.has(note.session)) return;
    for (const card of cards.get(note.session)) {
      if (card.ids.has(note.id)) continue;
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.textContent = note.title;
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      item.append(link);
      card.list.append(item);
      card.ids.add(note.id);
      card.list.hidden = false;
    }
  }

  for (const container of document.querySelectorAll('[data-session-notes]')) {
    const session = Number(container.dataset.sessionNotes);
    container.append(template.content.cloneNode(true));
    const list = container.querySelector('ul');
    const details = container.querySelector('details');
    const form = container.querySelector('form');
    const submit = form.querySelector('button');
    const status = container.querySelector('[role="status"]');
    const codeInput = form.elements.code;
    if (!cards.has(session)) cards.set(session, []);
    cards.get(session).push({ list, ids: new Set() });

    details.addEventListener('toggle', () => {
      if (details.open && !codeInput.value) codeInput.value = registrationCode;
    });
    form.addEventListener('submit', async event => {
      event.preventDefault();
      if (submit.disabled) return;
      const url = webUrl(form.elements.url.value.trim());
      const title = form.elements.title.value.trim();
      const code = codeInput.value.trim();
      if (!url || !title || !code || url.length > 2048) {
        status.textContent = '제목, 올바른 웹 주소(http 또는 https), 등록 코드를 입력해 주세요.';
        return;
      }

      submit.disabled = true;
      status.textContent = '등록 중…';
      try {
        const result = await request(new URLSearchParams({ session, title, url, code }));
        if (result.error === 'code') {
          status.textContent = '등록 코드를 확인해 주세요.';
          codeInput.focus();
          return;
        }
        if (result.error === 'invalid') {
          status.textContent = '제목과 웹 주소를 확인해 주세요.';
          return;
        }
        if (!result.ok || !result.note) throw new Error('Note was not saved');
        showNote(result.note);
        registrationCode = code;
        form.reset();
        details.open = false;
        container.querySelector('summary').focus();
        status.textContent = result.duplicate ? '이미 등록된 링크입니다.' : '노트를 등록했습니다.';
      } catch {
        status.textContent = '노트를 등록할 수 없습니다. 잠시 후 다시 시도해 주세요.';
      } finally {
        submit.disabled = false;
      }
    });
  }

  if (cards.size) {
    request()
      .then(result => {
        if (!result.ok || !Array.isArray(result.notes)) throw new Error('Notes unavailable');
        result.notes.forEach(showNote);
      })
      .catch(() => {
        document.querySelector('#session-notes-load-error').hidden = false;
      });
  }
})();
