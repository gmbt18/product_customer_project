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
