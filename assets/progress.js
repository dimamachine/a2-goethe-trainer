// Общий трекер прохождения. Используется во всех модулях.
// Состояние сериализуется в localStorage под ключом STORAGE_KEY.
// API: window.Progress.{is,set,toggle,reset,count,total,setTotal,subscribe,renderDoneButton,placeDoneButton}
(function () {
  'use strict';
  const STORAGE_KEY = 'a2_progress_v1';
  const TOTALS_KEY = 'a2_progress_totals_v1';

  function load() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
    catch (_) { return {}; }
  }
  function save(data) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); } catch (_) {}
  }
  function loadTotals() {
    try { return JSON.parse(localStorage.getItem(TOTALS_KEY) || '{}'); }
    catch (_) { return {}; }
  }
  function saveTotals(t) {
    try { localStorage.setItem(TOTALS_KEY, JSON.stringify(t)); } catch (_) {}
  }

  let state = load();
  const subscribers = [];

  function notify(module) {
    subscribers.forEach(fn => {
      try { fn(module); } catch (_) {}
    });
  }

  function is(module, taskId) {
    return !!(state[module] && state[module][taskId]);
  }
  function set(module, taskId, done) {
    if (!module || !taskId) return;
    if (!state[module]) state[module] = {};
    if (done) state[module][taskId] = true;
    else delete state[module][taskId];
    if (Object.keys(state[module]).length === 0) delete state[module];
    save(state);
    notify(module);
  }
  function toggle(module, taskId) {
    set(module, taskId, !is(module, taskId));
  }
  // Сбрасывает прогресс модуля (или весь, если module не задан). Тоталы не трогаем.
  function reset(module) {
    if (module) delete state[module];
    else state = {};
    save(state);
    notify(module);
  }
  function count(module) {
    if (!module) {
      let n = 0;
      Object.keys(state).forEach(m => n += Object.keys(state[m]).length);
      return n;
    }
    return state[module] ? Object.keys(state[module]).length : 0;
  }
  function setTotal(module, n) {
    const totals = loadTotals();
    totals[module] = n;
    saveTotals(totals);
  }
  function total(module) {
    const totals = loadTotals();
    if (!module) return Object.values(totals).reduce((a, b) => a + b, 0);
    return totals[module] || 0;
  }
  function subscribe(fn) {
    subscribers.push(fn);
    return () => {
      const i = subscribers.indexOf(fn);
      if (i >= 0) subscribers.splice(i, 1);
    };
  }

  // Slug-функция для генерации стабильных ID из произвольных строк
  function slug(s) {
    return String(s || '')
      .toLowerCase()
      .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '')
      .slice(0, 80);
  }

  // Рендерит кнопку «Erledigt» (тот же вид во всех модулях, что и в Lesen).
  // Возвращает <button class="btn btn-done"> с состоянием .is-done.
  // opts: { module, taskId, label, onChange }
  function renderDoneButton(opts) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn-done';
    btn.dataset.module = opts.module;
    btn.dataset.taskId = opts.taskId;
    function refresh() {
      const done = is(opts.module, opts.taskId);
      btn.classList.toggle('is-done', done);
      btn.textContent = done ? '✓ Erledigt' : '○ Als erledigt';
      btn.setAttribute('aria-pressed', done ? 'true' : 'false');
      btn.title = done
        ? 'Erledigt — Klick zum Zurücksetzen'
        : (opts.label || 'Als erledigt markieren');
    }
    let firedOnPointerDown = false;
    btn.addEventListener('pointerdown', (e) => {
      if (e.button !== undefined && e.button !== 0) return;
      e.stopPropagation();
      toggle(opts.module, opts.taskId);
      refresh();
      if (opts.onChange) opts.onChange(is(opts.module, opts.taskId));
      firedOnPointerDown = true;
    });
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (firedOnPointerDown) { firedOnPointerDown = false; e.preventDefault(); return; }
      toggle(opts.module, opts.taskId);
      refresh();
      if (opts.onChange) opts.onChange(is(opts.module, opts.taskId));
    });
    // Авто-обновление при внешних изменениях прогресса (напр. сброс модуля).
    // Отписка вызывается в placeDoneButton при замене кнопки — без утечек.
    btn._unsub = subscribe((m) => { if (!m || m === opts.module) refresh(); });
    refresh();
    return btn;
  }

  // Кладёт кнопку «Erledigt» в контейнер (напр. панель управления .controls),
  // заменяя ранее вставленную. Прижимает вправо. Возвращает кнопку или null.
  // container — DOM-элемент; opts — как у renderDoneButton.
  function placeDoneButton(container, opts) {
    if (!container) return null;
    const old = container.querySelector('.btn-done');
    if (old) { if (old._unsub) old._unsub(); old.remove(); }
    if (!opts || !opts.taskId) return null;
    const btn = renderDoneButton(opts);
    container.appendChild(btn);
    return btn;
  }

  // ——— Общие хелперы (раньше дублировались в каждой странице) ———
  function escapeHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
  }
  const _lastPick = new WeakMap();  // не выдаём тот же элемент два раза подряд
  function pick(arr) {
    if (!arr || !arr.length) return undefined;
    if (arr.length === 1) return arr[0];
    const last = _lastPick.get(arr);
    let x;
    do { x = arr[Math.floor(Math.random() * arr.length)]; } while (x === last);
    _lastPick.set(arr, x);
    return x;
  }
  window.escapeHtml = escapeHtml;
  window.pick = pick;

  window.Progress = {
    is, set, toggle, reset, count, total, setTotal, subscribe,
    renderDoneButton, placeDoneButton, slug,
    STORAGE_KEY, TOTALS_KEY,
    _state: () => state,
    _reload: () => { state = load(); }
  };
})();
