/* Click a screenshot (.shots img) to zoom; click outside / ✕ / Esc to close.
   No-op on pages without a .shots gallery. Load with `defer`. */
(function () {
  // Desktop only — skip click-to-zoom on phones / narrow viewports.
  if (!window.matchMedia('(min-width: 768px)').matches) return;

  var shots = document.querySelectorAll('.shots img');
  if (!shots.length) return;

  var box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.innerHTML = '<button class="lightbox__close" type="button" aria-label="Close">✕</button><img alt="">';
  document.body.appendChild(box);
  var big = box.querySelector('img');

  function open(src, alt) {
    big.src = src;
    big.alt = alt || '';
    box.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    box.classList.remove('open');
    document.body.style.overflow = '';
  }

  shots.forEach(function (img) {
    var frame = img.closest('.shot__media') || img;
    frame.addEventListener('click', function () {
      open(img.currentSrc || img.src, img.alt);
    });
  });

  // click anywhere except the image itself (backdrop or ✕) closes
  box.addEventListener('click', function (e) {
    if (e.target !== big) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && box.classList.contains('open')) close();
  });
})();
