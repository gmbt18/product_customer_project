window.onload = () => {
  if (document.querySelector('.superuser-auth-span').textContent === 'True') {
    document.querySelector('.product-search-view-btn').addEventListener('click', changeSearchMode);
    document.querySelector('.customer-search-view-btn').addEventListener('click', changeSearchMode);
  }
  document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
    e.addEventListener('change', changeCategory);
  });
  // document.querySelector('.search-products-btn').addEventListener('click', submitProductSearchForm);
  document.querySelectorAll('.view-btn').forEach(e => e.addEventListener('click', viewProfile));
}

changeSearchMode = event => {
  console.log(event.target)
  if (event.target.textContent === 'Product Search') {
    document.querySelector('.product-right-div').classList.replace('d-none', 'd-flex');
    document.querySelector('.customer-right-div').classList.replace('d-flex', 'd-none');
    document.querySelector('.product-search-btn').classList.replace('btn-secondary', 'btn-dark');
    document.querySelector('.customer-search-btn').classList.replace('btn-dark', 'btn-secondary');
  }
  else if (event.target.textContent === 'Customer Search') {
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

viewProfile = event => {
  const TARGET_CUSTOMER = event.target.parentElement.parentElement.querySelector('.customer-customer-span').textContent;
  let targetID = '';
  event.target.parentElement.parentElement.querySelectorAll('.auth-user-info-div').forEach(e => {
    console.log(e.querySelector('.auth-user-username').textContent, TARGET_CUSTOMER)
    if (e.querySelector('.auth-user-username').textContent === TARGET_CUSTOMER) {
      targetID = e.querySelector('.auth-user-id').textContent;
    }
  });
  window.location.href = window.location.href.split('/').slice(0,-2).join('/') + `/customerInfo/${targetID}`;
}
