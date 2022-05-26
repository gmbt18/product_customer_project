window.onload = () => {
  // if (document.querySelector('.superuser-auth-span').textContent === 'True') {
  //   document.querySelector('.product-search-view-btn').addEventListener('click', changeSearchMode);
  //   document.querySelector('.customer-search-view-btn').addEventListener('click', changeSearchMode);
  // }
  // document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
  //   e.addEventListener('change', changeCategory);
  // });
  document.querySelector('.search-customers-btn').addEventListener('click', filterCustomers);
  // document.querySelector('.search-products-btn').addEventListener('click', submitProductSearchForm);
  document.querySelectorAll('.view-btn').forEach(e => e.addEventListener('click', viewProfile));
}

// changeSearchMode = event => {
//   if (event.target.textContent === 'Product Search') {
//     document.querySelector('.product-right-div').classList.replace('d-none', 'd-flex');
//     document.querySelector('.customer-right-div').classList.replace('d-flex', 'd-none');
//     document.querySelector('.product-search-btn').classList.replace('btn-secondary', 'btn-dark');
//     document.querySelector('.customer-search-btn').classList.replace('btn-dark', 'btn-secondary');
//   }
//   else if (event.target.textContent === 'Customer Search') {
//     document.querySelector('.product-right-div').classList.replace('d-flex', 'd-none');
//     document.querySelector('.customer-right-div').classList.replace('d-none', 'd-flex');
//     document.querySelector('.product-search-btn').classList.replace('btn-dark', 'btn-secondary');
//     document.querySelector('.customer-search-btn').classList.replace('btn-secondary', 'btn-dark');
//   }
// }

// changeCategory = () => {
//   const CURR_CATEGORY = document.querySelector('input[name="categoryRadio"]:checked').value;
//   const SPINAL_CATEGORY = CURR_CATEGORY.replace(/([A-Z])/, '-$1').toLowerCase();
//   document.querySelectorAll('input[type="checkbox"]').forEach(e => e.checked = false);
//   document.querySelector('.audio-filter-subcategories').classList.replace('d-flex', 'd-none');
//   document.querySelector('.clothes-filter-subcategories').classList.replace('d-flex', 'd-none');
//   document.querySelector('.shoes-filter-subcategories').classList.replace('d-flex', 'd-none');
//   document.querySelector('.tech-filter-subcategories').classList.replace('d-flex', 'd-none');
//   document.querySelector('.accessories-filter-subcategories').classList.replace('d-flex', 'd-none');
//   document.querySelector(`.${CURR_CATEGORY}-filter-subcategories`).classList.replace('d-none', 'd-flex');
//   document.querySelectorAll('.audio-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
//   document.querySelectorAll('.clothes-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
//   document.querySelectorAll('.shoes-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
//   document.querySelectorAll('.tech-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
//   document.querySelectorAll('.accessories-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
//   document.querySelectorAll(`.${SPINAL_CATEGORY}-cat-products`).forEach(e => e.classList.replace('d-none', 'd-flex'));
// }

// submitProductSearchForm = () => {
//   // const includesAll = 
//   // const CHECKED_CATEGORY = document.querySelector('input[name="categoryRadio"]:checked').value;
//   // let checkedSubs = [];
//   // document.querySelectorAll('input[type="checkbox"]:checked').forEach(e => {
//   //   checkedSubs.push(e.value);
//   // });
//   // const CHECKED_MIN_RATING = document.querySelector('input[name="ratingsRadio"]:checked').value;
//   // const MIN_PRICE = document.getElementById('minPriceField').value;
//   // const MAX_PRICE = document.getElementById('maxPriceField').value;
//   document.querySelector('.product-search-form').submit();
// }

filterCustomers = () => {
  const QUERY = {
    name: document.getElementById('nameField').value,
    sex: document.getElementById('sexField').value,
    nationality: document.getElementById('nationalityField').value,
    citizenship: document.getElementById('citizenshipField').value,
    presentAddress: document.getElementById('presentAddressField').value,
    permanentAddress: document.getElementById('permanentAddressField').value,
    billingAddress: document.getElementById('billingAddressField').value,
    shippingAddress: document.getElementById('shippingAddressField').value,
    officeAddress: document.getElementById('officeAddressField').value,
    personalMobileNumber: document.getElementById('personalMobileNumberField').value,
    officeMobileNumber: document.getElementById('officeMobileNumberField').value,
    homeLandlineNumber: document.getElementById('homeLandlineNumberField').value,
    officeLandlineNumber: document.getElementById('officeLandlineNumberField').value,
    personalEmail: document.getElementById('personalEmailField').value,
    officeEmail: document.getElementById('officeEmailField').value
  }
  let customers = [];
  let filteredIndices = [];
  document.querySelectorAll('.search-group').forEach(e => {
    let customer = {};
    customer.name = e.querySelector('.name-field').value.replace('Name: ', '');
    customer.birthday = e.querySelector('.birthday-field').value;
    customer.sex = e.querySelector('.sex-field').value;
    customer.nationality = e.querySelector('.nationality-field').value;
    customer.citizenship = e.querySelector('.citizenship-field').value;
    customer.presentAddress = e.querySelector('.present-address-field').value;
    customer.permanentAddress = e.querySelector('.permanent-address-field').value;
    customer.billingAddress = e.querySelector('.billing-address-field').value;
    customer.shippingAddress = e.querySelector('.shipping-address-field').value;
    customer.officeAddress = e.querySelector('.office-address-field').value;
    customer.personalMobileNumber = e.querySelector('.personal-mobile-number-field').value;
    customer.officeMobileNumber = e.querySelector('.office-mobile-number-field').value;
    customer.homeLandlineNumber = e.querySelector('.home-landline-number-field').value;
    customer.officeLandlineNumber = e.querySelector('.office-landline-number-field').value;
    customer.personalEmail = e.querySelector('.personal-email-field').value;
    customer.officeEmail = e.querySelector('.office-email-field').value;
    customers.push(customer);
  });
  customers.forEach((e,i) => {
    let mismatch = 0;
    if (!e.name.toLowerCase().includes(QUERY.name.toLowerCase())) mismatch++;
    if (QUERY.sex !== '0' && e.sex !== QUERY.sex) mismatch++;
    if (!e.nationality.toLowerCase().includes(QUERY.nationality.toLowerCase())) mismatch++;
    if (!e.citizenship.toLowerCase().includes(QUERY.citizenship.toLowerCase())) mismatch++;
    if (!e.presentAddress.toLowerCase().includes(QUERY.presentAddress.toLowerCase())) mismatch++;
    if (!e.permanentAddress.toLowerCase().includes(QUERY.permanentAddress.toLowerCase())) mismatch++;
    if (!e.billingAddress.toLowerCase().includes(QUERY.billingAddress.toLowerCase())) mismatch++;
    if (!e.shippingAddress.toLowerCase().includes(QUERY.shippingAddress.toLowerCase())) mismatch++;
    if (!e.officeAddress.toLowerCase().includes(QUERY.officeAddress.toLowerCase())) mismatch++;
    if (e.personalMobileNumber !== QUERY.personalMobileNumber) mismatch++;
    if (e.officeMobileNumber !== QUERY.officeMobileNumber) mismatch++;
    if (e.homeLandlineNumber !== QUERY.homeLandlineNumber) mismatch++;
    if (e.officeLandlineNumber !== QUERY.officeLandlineNumber) mismatch++;
    if (!e.personalEmail.toLowerCase().includes(QUERY.personalEmail.toLowerCase())) mismatch++;
    if (!e.officeEmail.toLowerCase().includes(QUERY.officeEmail.toLowerCase())) mismatch++;
    if (mismatch === 0) filteredIndices.push(i);
  });
  document.querySelectorAll('.search-group').forEach((e,i) => {
    filteredIndices.includes(i) ? e.classList.replace('d-none', 'd-flex') : e.classList.replace('d-flex', 'd-none');
  });
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
