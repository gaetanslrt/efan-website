/* =========================================================================
   EFAN / FASN — navigation behaviour
   Mega menus (desktop) + slide-in panel with accordions (mobile).
   No dependencies.
   ========================================================================= */

/* =========================================================================
   Accessibility settings — high contrast and dyslexia-friendly font.
   The choice is stored in localStorage and applied by a small script in
   <head> before first paint; this part drives the panel in the header.
   ========================================================================= */
(function () {
  'use strict';

  var KEY = 'efan-a11y';
  var root = document.documentElement;
  var toggle = document.querySelector('.a11y__toggle');
  var panel = document.getElementById('a11y-panel');
  if (!toggle || !panel) { return; }

  var radios = Array.prototype.slice.call(panel.querySelectorAll('input[type="radio"]'));
  var prefersMore = window.matchMedia ? window.matchMedia('(prefers-contrast: more)') : null;

  function stored() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }

  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* private mode */ }
  }

  function settings() {
    var s = stored();
    return {
      contrast: s.contrast || (prefersMore && prefersMore.matches ? 'high' : 'standard'),
      font: s.font || 'standard'
    };
  }

  function apply(s) {
    if (s.contrast === 'high') { root.setAttribute('data-contrast', 'high'); }
    else { root.removeAttribute('data-contrast'); }
    if (s.font === 'dyslexic') { root.setAttribute('data-font', 'dyslexic'); }
    else { root.removeAttribute('data-font'); }
    radios.forEach(function (r) {
      r.checked = s[r.name.replace('a11y-', '')] === r.value;
    });
  }

  radios.forEach(function (r) {
    r.addEventListener('change', function () {
      var s = stored();
      s[r.name.replace('a11y-', '')] = r.value;
      save(s);
      apply(settings());
    });
  });

  /* ------------------------------------------------------------- panel */
  function isOpen() { return toggle.getAttribute('aria-expanded') === 'true'; }

  function open() {
    toggle.setAttribute('aria-expanded', 'true');
    panel.hidden = false;
  }

  function close(returnFocus) {
    toggle.setAttribute('aria-expanded', 'false');
    panel.hidden = true;
    if (returnFocus) { toggle.focus(); }
  }

  toggle.addEventListener('click', function () {
    if (isOpen()) { close(false); } else { open(); }
  });

  panel.querySelector('.a11y-panel__close').addEventListener('click', function () {
    close(true);
  });

  panel.querySelector('.a11y-panel__reset').addEventListener('click', function () {
    try { localStorage.removeItem(KEY); } catch (e) { /* ignore */ }
    apply(settings());
  });

  document.addEventListener('keydown', function (e) {
    if ((e.key === 'Escape' || e.key === 'Esc') && isOpen()) {
      close(panel.contains(document.activeElement) || document.activeElement === toggle);
    }
  });

  document.addEventListener('click', function (e) {
    if (isOpen() && !panel.contains(e.target) && !toggle.contains(e.target)) { close(false); }
  });

  document.addEventListener('focusin', function (e) {
    if (isOpen() && !panel.contains(e.target) && e.target !== toggle) { close(false); }
  });

  /* Keep several open tabs in step. */
  window.addEventListener('storage', function (e) {
    if (e.key === KEY || e.key === null) { apply(settings()); }
  });

  apply(settings());
  toggle.hidden = false;
})();

(function () {
  'use strict';

  var DESKTOP = window.matchMedia('(min-width: 62em)');

  var nav     = document.getElementById('main-nav');
  var burger  = document.getElementById('burger');
  var overlay = document.getElementById('nav-overlay');
  if (!nav || !burger) { return; }

  var toggles = Array.prototype.slice.call(nav.querySelectorAll('.nav__btn'));

  /* ---------------------------------------------------------------- menus */
  function panelOf(btn) {
    return document.getElementById(btn.getAttribute('aria-controls'));
  }

  function closeMenu(btn) {
    var panel = panelOf(btn);
    btn.setAttribute('aria-expanded', 'false');
    if (panel) { panel.hidden = true; }
  }

  function closeAllMenus(except) {
    toggles.forEach(function (btn) {
      if (btn !== except) { closeMenu(btn); }
    });
  }

  function openMenu(btn) {
    var panel = panelOf(btn);
    if (DESKTOP.matches) { closeAllMenus(btn); }
    btn.setAttribute('aria-expanded', 'true');
    if (panel) { panel.hidden = false; }
  }

  toggles.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      if (open) { closeMenu(btn); } else { openMenu(btn); }
    });
  });

  /* --------------------------------------------------------- mobile panel */
  function openNav() {
    nav.classList.add('is-open');
    burger.setAttribute('aria-expanded', 'true');
    if (overlay) { overlay.hidden = false; }
    document.body.classList.add('nav-open');
  }

  function closeNav() {
    nav.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    if (overlay) { overlay.hidden = true; }
    document.body.classList.remove('nav-open');
  }

  burger.addEventListener('click', function () {
    if (nav.classList.contains('is-open')) { closeNav(); } else { openNav(); }
  });

  var closeBtn = document.getElementById('nav-close');
  if (closeBtn) {
    closeBtn.addEventListener('click', function () {
      closeNav();
      burger.focus();
    });
  }

  /* Following a link inside the mobile panel should dismiss it. */
  nav.addEventListener('click', function (e) {
    var link = e.target.closest ? e.target.closest('a') : null;
    if (link && !DESKTOP.matches) { closeNav(); }
  });

  if (overlay) {
    overlay.addEventListener('click', function () {
      closeNav();
      closeAllMenus();
    });
  }

  /* Duplicate the enrollment call to action inside the mobile panel. */
  var list = nav.querySelector('.nav__list');
  var headerCta = document.querySelector('.header__cta');
  if (list && headerCta) {
    var item = document.createElement('li');
    item.className = 'nav__mobile-cta';
    var link = headerCta.cloneNode(true);
    link.classList.remove('header__cta');
    item.appendChild(link);
    list.appendChild(item);
  }

  /* ------------------------------------------------------- global closing */
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape' && e.key !== 'Esc') { return; }

    var openBtn = toggles.filter(function (b) {
      return b.getAttribute('aria-expanded') === 'true';
    })[0];

    if (openBtn) {
      closeMenu(openBtn);
      openBtn.focus();
    } else if (nav.classList.contains('is-open')) {
      closeNav();
      burger.focus();
    }
  });

  document.addEventListener('click', function (e) {
    if (!DESKTOP.matches) { return; }
    if (nav.contains(e.target) || burger.contains(e.target)) { return; }
    closeAllMenus();
  });

  /* Close the desktop mega menu once focus leaves the navigation. */
  document.addEventListener('focusin', function (e) {
    if (!DESKTOP.matches) { return; }
    if (nav.contains(e.target)) { return; }
    closeAllMenus();
  });

  /* ---------------------------------------------------------- breakpoint */
  function syncBreakpoint() {
    closeNav();
    closeAllMenus();
  }
  if (typeof DESKTOP.addEventListener === 'function') {
    DESKTOP.addEventListener('change', syncBreakpoint);
  } else if (typeof DESKTOP.addListener === 'function') {
    DESKTOP.addListener(syncBreakpoint);
  }
})();

/* =========================================================================
   Gallery lightbox — progressive enhancement over plain image links.
   Without JavaScript the links still open the full-size photograph.
   ========================================================================= */
(function () {
  'use strict';

  var links = Array.prototype.slice.call(document.querySelectorAll('.shot__link'));
  if (!links.length) { return; }

  var strings = document.documentElement.lang === 'fr'
    ? { close: 'Fermer', prev: 'Photo précédente', next: 'Photo suivante', of: 'sur' }
    : { close: 'Close', prev: 'Previous photo', next: 'Next photo', of: 'of' };

  var box = document.createElement('div');
  box.className = 'lightbox';
  box.hidden = true;
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.innerHTML =
    '<div class="lightbox__bar">' +
      '<span class="lightbox__count"></span>' +
      '<button type="button" class="lightbox__close">' + strings.close + ' ×</button>' +
    '</div>' +
    '<div class="lightbox__stage">' +
      '<button type="button" class="lightbox__nav" data-dir="-1" aria-label="' + strings.prev + '">‹</button>' +
      '<img alt="" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">' +
      '<button type="button" class="lightbox__nav" data-dir="1" aria-label="' + strings.next + '">›</button>' +
    '</div>' +
    '<p class="lightbox__caption"></p>';
  document.body.appendChild(box);

  var img = box.querySelector('img');
  var caption = box.querySelector('.lightbox__caption');
  var count = box.querySelector('.lightbox__count');
  var closeBtn = box.querySelector('.lightbox__close');
  var navs = Array.prototype.slice.call(box.querySelectorAll('.lightbox__nav'));
  var current = 0;
  var lastFocus = null;

  function captionOf(link) {
    var li = link.closest ? link.closest('li') : null;
    var p = li ? li.querySelector('.shot__caption') : null;
    return p ? p.textContent.trim() : (link.querySelector('img') || {}).alt || '';
  }

  function show(i) {
    current = (i + links.length) % links.length;
    var link = links[current];
    img.src = link.getAttribute('href');
    img.alt = captionOf(link);
    caption.textContent = captionOf(link);
    count.textContent = (current + 1) + ' ' + strings.of + ' ' + links.length;
  }

  function open(i) {
    lastFocus = document.activeElement;
    show(i);
    box.hidden = false;
    document.body.classList.add('nav-open');
    closeBtn.focus();
  }

  function close() {
    box.hidden = true;
    document.body.classList.remove('nav-open');
    img.src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7';
    if (lastFocus && lastFocus.focus) { lastFocus.focus(); }
  }

  links.forEach(function (link, i) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      open(i);
    });
  });

  navs.forEach(function (b) {
    b.addEventListener('click', function () {
      show(current + parseInt(b.getAttribute('data-dir'), 10));
    });
  });

  closeBtn.addEventListener('click', close);
  box.addEventListener('click', function (e) {
    if (e.target === box || e.target.classList.contains('lightbox__stage')) { close(); }
  });

  document.addEventListener('keydown', function (e) {
    if (box.hidden) { return; }
    if (e.key === 'Escape' || e.key === 'Esc') { close(); }
    else if (e.key === 'ArrowLeft') { show(current - 1); }
    else if (e.key === 'ArrowRight') { show(current + 1); }
    else if (e.key === 'Tab') {
      /* keep focus inside the dialog */
      var focusable = [closeBtn].concat(navs);
      var i = focusable.indexOf(document.activeElement);
      e.preventDefault();
      var next = e.shiftKey ? i - 1 : i + 1;
      focusable[(next + focusable.length) % focusable.length].focus();
    }
  });
})();
