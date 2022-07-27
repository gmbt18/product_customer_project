window.onload = () => {
  handleWindowResize();
  window.addEventListener('resize', handleWindowResize);
}

handleWindowResize = () => {
  document.querySelectorAll('.product-card').forEach(e => {
    e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.replace('...', '');
    if (window.innerWidth < 1720) e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.slice(0, 64) + '...';
    else if (window.innerWidth >= 1720) e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.slice(0, 80) + '...';
  });
}