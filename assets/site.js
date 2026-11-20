(() => {
  const button = document.getElementById('back-to-top');
  if (!button) return;
  const update = () => { button.hidden = window.scrollY < 360; };
  window.addEventListener('scroll', update, { passive: true });
  update();
  button.addEventListener('click', () => {
    const behavior = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    window.scrollTo({ top: 0, behavior });
  });
})();
