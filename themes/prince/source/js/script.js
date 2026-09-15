(function () {
  'use strict';

  var toggle = document.querySelector('.navbar-toggle');
  var menu = document.querySelector('.main-nav-items');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var isOpen = toggle.classList.toggle('is-open');
      menu.classList.toggle('is-open', isOpen);
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.setAttribute('aria-label', isOpen ? '关闭导航' : '打开导航');
    });

    menu.addEventListener('click', function (event) {
      if (event.target.tagName === 'A') {
        toggle.classList.remove('is-open');
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  if (window.jQuery && window.jQuery.fancybox) {
    window.jQuery('.post-entry p img').each(function () {
      var image = window.jQuery(this);
      if (!image.parent().hasClass('fancybox')) {
        image.wrap(
          '<a class="fancybox" data-fancybox="article" href="' +
          this.src +
          '" data-caption="' +
          (this.alt || '') +
          '"></a>'
        );
      }
    });
  }
})();
