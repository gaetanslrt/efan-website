/* =========================================================================
   EFAN / FASN — navigation behaviour
   Mega menus (desktop) + slide-in panel with accordions (mobile).
   No dependencies.
   ========================================================================= */
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
