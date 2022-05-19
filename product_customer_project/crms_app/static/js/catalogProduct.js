window.onload = () => {
  document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
    e.addEventListener('change', changeCategory);
  })
  document.querySelectorAll('input[type="checkbox"]').forEach(e => {
    e.addEventListener('change', changeSubcategory);
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
  const SPINAL_CATEGORY = CURR_CATEGORY.replace(/([A-Z])/, '-$1').toLowerCase();
  console.log(SPINAL_CATEGORY);
  document.querySelectorAll('input[type="checkbox"]').forEach(e => e.checked = false)
  document.querySelector('.curr-category').textContent = CURR_CATEGORY.charAt(0).toUpperCase() + CURR_CATEGORY.slice(1,CURR_CATEGORY.length);
  document.querySelector('.audio-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.clothes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.shoes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.tech-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.accessories-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector(`.${CURR_CATEGORY}-filter-subcategories`).classList.replace('d-none', 'd-flex');
  document.querySelector('.audio-cat-products').classList.replace('d-flex', 'd-none');
  document.querySelector('.clothes-cat-products').classList.replace('d-flex', 'd-none');
  document.querySelector('.shoes-cat-products').classList.replace('d-flex', 'd-none');
  document.querySelector('.tech-cat-products').classList.replace('d-flex', 'd-none');
  document.querySelector('.accessories-cat-products').classList.replace('d-flex', 'd-none');
  document.querySelector(`.${SPINAL_CATEGORY}-cat-products`).classList.replace('d-flex', 'd-none');
}

changeSubcategory = () => {
  let checkedSubs = [];
  document.querySelectorAll('input[type="checkbox"]:checked').forEach(e => {
    checkedSubs.push(e.value);
  })
  if (checkedSubs.length) {
    checkedSubs = checkedSubs.map(e => {
      return e.replace(/([A-Z])/, '-$1').toLowerCase();
    })
    document.querySelectorAll('.products-group').forEach(e => {
      let sub = e.classList[1].replace('-sub-products', '');
      if (checkedSubs.includes(sub)) e.classList.replace('d-none', 'd-flex');
      else if (!checkedSubs.includes(sub)) e.classList.replace('d-flex', 'd-none');
    })
  } else {
    document.querySelectorAll('.products-group').forEach(e => {
      e.classList.replace('d-none', 'd-flex')
    })
  }
}

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** numDecimals)) / (10 ** numDecimals);
}