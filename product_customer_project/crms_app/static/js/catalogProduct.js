window.onload = () => {
  document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
    e.addEventListener('change', changeCategory);
  })

  document.querySelectorAll('.product-card').forEach(e => {
    const RATING_ARR = e.querySelector('.product-rating').textContent.match(/\d+/g);
    let avg = 0;
    let count = 0;
    for (let i = 0; i < RATING_ARR.length; i++) {
      avg += RATING_ARR[i] * i+1;
      count += Number(RATING_ARR[i]);
    }
    avg /= count;
    e.querySelector('.full-stars').style.width = e.querySelector('.product-rating').textContent * 20 + '%';

    e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.slice(0, 80) + '...';
  })
};

changeCategory = () => {
  const CURR_CATEGORY = document.querySelector('input[name="categoryRadio"]:checked').value;
  document.querySelector('.curr-category').textContent = CURR_CATEGORY.charAt(0).toUpperCase() + CURR_CATEGORY.slice(1,CURR_CATEGORY.length);
  document.querySelector('.audio-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.clothes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.shoes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.tech-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.accessories-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector(`.${CURR_CATEGORY}-filter-subcategories`).classList.replace('d-none', 'd-flex');
}

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** numDecimals)) / (10 ** numDecimals);
}