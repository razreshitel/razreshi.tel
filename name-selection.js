document.querySelectorAll('.hero__name').forEach((name) => {
  name.addEventListener('mousedown', (event) => {
    if (event.detail !== 3) return;

    event.preventDefault();
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(name);
    selection.removeAllRanges();
    selection.addRange(range);
  });
});
