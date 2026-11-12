(() => {
  const endpoint = 'https://script.google.com/macros/s/AKfycbxjegCNCDm3UiXGaAbO6yGcVL9hl39YiN4V6vEvI9z6fQM5lNsUjtAtd3k4nTlzQY3F_w/exec';
  const template = document.querySelector('#session-notes-template');
  const cards = new Map();
  const changedIds = new Set();
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

  function showNote(note, activeCard) {
    const url = webUrl(note.url);
    if (!url || !cards.has(note.session)) return;
    let activeControls;
    for (const card of cards.get(note.session)) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.textContent = url;
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      const controls = createControls(card, note);
      item.append(link, controls.fragment);
      const previous = card.items.get(note.id);
      if (previous) previous.replaceWith(item);
      else card.list.append(item);
      card.items.set(note.id, item);
      card.list.hidden = false;
      if (card === activeCard) activeControls = controls;
    }
    return activeControls;
  }

  function removeNote(session, id) {
    for (const card of cards.get(session)) {
      card.items.get(id)?.remove();
      card.items.delete(id);
      card.list.hidden = card.items.size === 0;
    }
  }

  function createControls(card, note) {
    const fragment = template.content.cloneNode(true);
    const details = fragment.querySelector('details');
    const summary = details.querySelector('summary');
    const form = details.querySelector('form');
    const submit = form.querySelector('[type="submit"]');
    const remove = form.querySelector('[type="button"]');
    const status = fragment.querySelector('[role="status"]');
    const urlInput = form.elements.url;
    const codeInput = form.elements.code;
    if (note) {
      summary.textContent = '수정 / 삭제';
      urlInput.value = note.url;
      submit.textContent = '수정 저장';
      remove.hidden = false;
      form.querySelector('p').hidden = true;
    }

    details.addEventListener('toggle', () => {
      if (details.open && !codeInput.value) codeInput.value = registrationCode;
    });
    form.addEventListener('submit', event => {
      event.preventDefault();
      save(note ? 'update' : 'add');
    });
    remove.addEventListener('click', () => save('delete'));

    async function save(action) {
      if (submit.disabled) return;
      const code = codeInput.value.trim();
      const url = action === 'delete' ? '' : webUrl(urlInput.value.trim());
      if (!code) {
        status.textContent = '참가자 등록 코드를 입력해 주세요.';
        codeInput.focus();
        return;
      }
      if (action !== 'delete' && (!url || url.length > 2048)) {
        status.textContent = '올바른 웹 주소(http 또는 https)를 입력해 주세요.';
        urlInput.focus();
        return;
      }

      submit.disabled = true;
      remove.disabled = true;
      status.textContent = '처리 중…';
      try {
        const body = new URLSearchParams({ action, session: card.session, url, code });
        if (note) {
          body.set('id', note.id);
          body.set('previousUrl', note.url);
        }
        const result = await request(body);
        if (result.error === 'code') {
          status.textContent = '등록 코드를 확인해 주세요.';
          codeInput.focus();
          return;
        }
        const errors = {
          invalid: '웹 주소를 확인해 주세요.',
          duplicate: '같은 회차에 이미 등록된 링크입니다.',
          missing: '이미 삭제된 링크입니다. 페이지를 새로고침해 주세요.',
          conflict: '다른 참가자가 링크를 변경했습니다. 새로고침 후 다시 시도해 주세요.',
        };
        if (errors[result.error]) {
          status.textContent = errors[result.error];
          return;
        }
        if (!result.ok) throw new Error('Note was not saved');
        registrationCode = code;
        if (action === 'delete') {
          if (result.removed !== note.id) throw new Error('Note was not removed');
          changedIds.add(note.id);
          removeNote(card.session, note.id);
          card.registration.status.textContent = '링크를 삭제했습니다.';
          card.registration.summary.focus();
          return;
        }

        if (!result.note) throw new Error('Note was not saved');
        changedIds.add(result.note.id);
        if (action === 'update') {
          const updated = showNote(result.note, card);
          updated.status.textContent = '링크를 수정했습니다.';
          updated.summary.focus();
          return;
        }
        if (!result.duplicate || !card.items.has(result.note.id)) showNote(result.note);
        form.reset();
        details.open = false;
        summary.focus();
        status.textContent = result.duplicate ? '이미 등록된 링크입니다.' : '링크를 등록했습니다.';
      } catch {
        status.textContent = '링크를 처리할 수 없습니다. 잠시 후 다시 시도해 주세요.';
      } finally {
        submit.disabled = false;
        remove.disabled = false;
      }
    }
    return { fragment, status, summary };
  }

  for (const container of document.querySelectorAll('[data-session-notes]')) {
    const session = Number(container.dataset.sessionNotes);
    const list = document.createElement('ul');
    list.className = 'session-note-links';
    list.setAttribute('aria-label', '세션 노트');
    list.hidden = true;
    const card = { session, list, items: new Map() };
    card.registration = createControls(card);
    container.append(list, card.registration.fragment);
    if (!cards.has(session)) cards.set(session, []);
    cards.get(session).push(card);
  }

  if (cards.size) {
    request()
      .then(result => {
        if (!result.ok || !Array.isArray(result.notes)) throw new Error('Notes unavailable');
        for (const note of result.notes) {
          if (!changedIds.has(note.id)) showNote(note);
        }
      })
      .catch(() => {
        document.querySelector('#session-notes-load-error').hidden = false;
      });
  }
})();
