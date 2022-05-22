window.onload = () => {
  if (document.querySelector('.superuser-auth-span').textContent == true) {
    document.querySelector('.product-search-view-btn').addEventListener('click', changeSearchMode('productSearch'));
    document.querySelector('.customer-search-view-btn').addEventListener('click', changeSearchMode('customerSearch'));
  }
  document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
    e.addEventListener('change', changeCategory);
  });
  document.querySelector('.search-products-btn').addEventListener('click', submitProductSearchForm);
}

changeSearchMode = mode => {
  if (mode === 'productSearch') {
    document.querySelector('.product-right-div').classList.replace('d-none', 'd-flex');
    document.querySelector('.customer-right-div').classList.replace('d-flex', 'd-none');
    document.querySelector('.product-search-btn').classList.replace('btn-secondary', 'btn-dark');
    document.querySelector('.customer-search-btn').classList.replace('btn-dark', 'btn-secondary');
  }
  else if (mode === 'customerSearch') {
    document.querySelector('.product-right-div').classList.replace('d-flex', 'd-none');
    document.querySelector('.customer-right-div').classList.replace('d-none', 'd-flex');
    document.querySelector('.product-search-btn').classList.replace('btn-dark', 'btn-secondary');
    document.querySelector('.customer-search-btn').classList.replace('btn-secondary', 'btn-dark');
  }
}

changeCategory = () => {
  const CURR_CATEGORY = document.querySelector('input[name="categoryRadio"]:checked').value;
  const SPINAL_CATEGORY = CURR_CATEGORY.replace(/([A-Z])/, '-$1').toLowerCase();
  document.querySelectorAll('input[type="checkbox"]').forEach(e => e.checked = false);
  document.querySelector('.audio-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.clothes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.shoes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.tech-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.accessories-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector(`.${CURR_CATEGORY}-filter-subcategories`).classList.replace('d-none', 'd-flex');
  document.querySelectorAll('.audio-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.clothes-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.shoes-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.tech-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.accessories-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll(`.${SPINAL_CATEGORY}-cat-products`).forEach(e => e.classList.replace('d-none', 'd-flex'));
}

submitProductSearchForm = () => {
  // const includesAll = 
  // const CHECKED_CATEGORY = document.querySelector('input[name="categoryRadio"]:checked').value;
  // let checkedSubs = [];
  // document.querySelectorAll('input[type="checkbox"]:checked').forEach(e => {
  //   checkedSubs.push(e.value);
  // });
  // const CHECKED_MIN_RATING = document.querySelector('input[name="ratingsRadio"]:checked').value;
  // const MIN_PRICE = document.getElementById('minPriceField').value;
  // const MAX_PRICE = document.getElementById('maxPriceField').value;
  document.querySelector('.product-search-form').submit();
}
