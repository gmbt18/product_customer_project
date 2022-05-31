window.onload = () => {
  // if (document.querySelector('.superuser-auth-span').textContent === 'True') {
  //   document.querySelector('.product-search-view-btn').addEventListener('click', changeSearchMode);
  //   document.querySelector('.customer-search-view-btn').addEventListener('click', changeSearchMode);
  // }
  // document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
  //   e.addEventListener('change', changeCategory);
  // });
  // document.querySelector('.search-products-btn').addEventListener('click', submitProductSearchForm);
  document.querySelector('.search-btn').addEventListener('click', filterCustomers);
  document.querySelector('.view-all-btn').addEventListener('click', filterCustomers);

  document.querySelector('.bottom-left-div').querySelectorAll('input[type="radio"]').forEach(e => {
    e.addEventListener('change', changeSort);
  });

  document.querySelectorAll('.search-group').forEach(e => {
    e.querySelector('.update-btn').addEventListener('click', updateMode);
    e.querySelector('.finish-update-btn').addEventListener('click', submitUpdate);
    e.querySelector('.cancel-update-btn').addEventListener('click', updateToView);
    e.querySelector('.view-btn').addEventListener('click', viewProfile);
    e.querySelector('.editing-customer-img').addEventListener('click', editImg);
    e.querySelector('.picture-input').addEventListener('change', readImgFile);

    let targetCustomer = e.querySelector('.customer-customer-span').textContent;
    let targetID = '';
    e.querySelectorAll('.auth-user-info-div').forEach(e => {
      if (e.querySelector('.auth-user-username').textContent === targetCustomer) {
        targetID = e.querySelector('.auth-user-id').textContent;
      }
    });
    e.querySelector('.target-id-span').textContent = targetID;
    e.querySelector('.profile-form').action = `/crms/customerInfoUpdate/${targetID}`;

    switch (e.querySelector('.sex-field').value) {
      case '0':
        e.querySelector('.sex-field').value = 'Male';
        break;
      case '1':
        e.querySelector('.sex-field').value = 'Female';
        break;
      case '2':
        e.querySelector('.sex-field').value = 'Intersex';
        break;
    }
  
    e.querySelector('.birthday-field').value = e.querySelector('.birthday-field').value.split(',').slice(0,-1).join(',');
    if (e.querySelector('.birthday-span').textContent.length > 0) {
      const TODAY = new Date();
      let birthdayArr = e.querySelector('.birthday-span').textContent.split(',').slice(0,-1).join('').split(' ');
      switch (birthdayArr[0]) {
        case 'Jan.':
          birthdayArr[0] = '01';
          break;
        case 'Feb.':
          birthdayArr[0] = '02';
          break;
        case 'March':
          birthdayArr[0] = '03';
          break;
        case 'April':
          birthdayArr[0] = '04';
          break;
        case 'May':
          birthdayArr[0] = '05';
          break;
        case 'June':
          birthdayArr[0] = '06';
          break;
        case 'July':
          birthdayArr[0] = '07';
          break;
        case 'Aug.':
          birthdayArr[0] = '08';
          break;
        case 'Sept.':
          birthdayArr[0] = '09';
          break;
        case 'Oct.':
          birthdayArr[0] = '10';
          break;
        case 'Nov.':
          birthdayArr[0] = '11';
          break;
        case 'Dec.':
          birthdayArr[0] = '12';
          break;
      }
      birthdayArr[1].length === 1 ? birthdayArr[1] = '0' + birthdayArr[1]: '';
      e.querySelector('.birthday-input').value = `${birthdayArr[2]}-${birthdayArr[0]}-${birthdayArr[1]}`;
      e.querySelector('.age-span').textContent = getAge(`${birthdayArr[2]}/${birthdayArr[0]}/${birthdayArr[1]}`);
      e.querySelector('.is-curr-month-birthday-span').textContent = (birthdayArr[0].replace('0','') == (TODAY.getMonth()+1));
      // console.log('test')
      // console.log(birthdayArr[0].replace('0',''), (TODAY.getMonth()+1), (birthdayArr[0].replace('0','') == (TODAY.getMonth()+1)))
      // console.log(`${birthdayArr[2]}-${birthdayArr[0]}-${birthdayArr[1]}`);
    }
  });
}

// code from and credits to
// https://stackoverflow.com/a/7091965
// https://jsfiddle.net/codeandcloud/n33RJ/
function getAge(dateString) {
  var today = new Date();
  var birthDate = new Date(dateString);
  var age = today.getFullYear() - birthDate.getFullYear();
  var m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
  }
  return age;
}

filterCustomers = event => {
  const DIV_TYPES = ['all','sex0','sex1','sex2'];
  for (i in DIV_TYPES) {
    let query = {};
    if (event.target.textContent === 'Search') {
      query = {
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
    }
    if (event.target.textContent === 'View All') {
      query = {
        name: '',
        sex: '3',
        nationality: '',
        citizenship: '',
        presentAddress: '',
        permanentAddress: '',
        billingAddress: '',
        shippingAddress: '',
        officeAddress: '',
        personalMobileNumber: '',
        officeMobileNumber: '',
        homeLandlineNumber: '',
        officeLandlineNumber: '',
        personalEmail: '',
        officeEmail: ''
      }
    }
    let customers = [];
    let filteredIndices = [];
    document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
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
      if (!e.name.toLowerCase().includes(query.name.toLowerCase())) mismatch++;
      if (query.sex !== '3' && e.sex !== query.sex) mismatch++;
      if (!e.nationality.toLowerCase().includes(query.nationality.toLowerCase())) mismatch++;
      if (!e.citizenship.toLowerCase().includes(query.citizenship.toLowerCase())) mismatch++;
      if (!e.presentAddress.toLowerCase().includes(query.presentAddress.toLowerCase())) mismatch++;
      if (!e.permanentAddress.toLowerCase().includes(query.permanentAddress.toLowerCase())) mismatch++;
      if (!e.billingAddress.toLowerCase().includes(query.billingAddress.toLowerCase())) mismatch++;
      if (!e.shippingAddress.toLowerCase().includes(query.shippingAddress.toLowerCase())) mismatch++;
      if (!e.officeAddress.toLowerCase().includes(query.officeAddress.toLowerCase())) mismatch++;
      if (!e.personalMobileNumber.includes(query.personalMobileNumber)) mismatch++;
      if (!e.officeMobileNumber.includes(query.officeMobileNumber)) mismatch++;
      if (!e.homeLandlineNumber.includes(query.homeLandlineNumber)) mismatch++;
      if (!e.officeLandlineNumber.includes(query.officeLandlineNumber)) mismatch++;
      if (!e.personalEmail.toLowerCase().includes(query.personalEmail.toLowerCase())) mismatch++;
      if (!e.officeEmail.toLowerCase().includes(query.officeEmail.toLowerCase())) mismatch++;

      // if (e.name == "Superuser") {
      //   if (!e.name.toLowerCase().includes(query.name.toLowerCase())) console.log(1);
      //   if (query.sex !== '3' && e.sex !== query.sex) console.log(2);
      //   if (!e.nationality.toLowerCase().includes(query.nationality.toLowerCase())) console.log(3);
      //   if (!e.citizenship.toLowerCase().includes(query.citizenship.toLowerCase())) console.log(4);
      //   if (!e.presentAddress.toLowerCase().includes(query.presentAddress.toLowerCase())) console.log(5);
      //   if (!e.permanentAddress.toLowerCase().includes(query.permanentAddress.toLowerCase())) console.log(6);
      //   if (!e.billingAddress.toLowerCase().includes(query.billingAddress.toLowerCase())) console.log(7);
      //   if (!e.shippingAddress.toLowerCase().includes(query.shippingAddress.toLowerCase())) console.log(8);
      //   if (!e.officeAddress.toLowerCase().includes(query.officeAddress.toLowerCase())) console.log(9);
      //   if (!e.personalMobileNumber.includes(query.personalMobileNumber)) console.log(10);
      //   if (!e.officeMobileNumber.includes(query.officeMobileNumber)) console.log(11);
      //   if (!e.homeLandlineNumber.includes(query.homeLandlineNumber)) console.log(12);
      //   if (!e.officeLandlineNumber.includes(query.officeLandlineNumber)) console.log(13);
      //   if (!e.personalEmail.toLowerCase().includes(query.personalEmail.toLowerCase())) console.log(14);
      //   if (!e.officeEmail.toLowerCase().includes(query.officeEmail.toLowerCase())) console.log(15);
      //   console.log(query)
      // }

      if (mismatch === 0) filteredIndices.push(i);
    });
    // console.log(query)
    // console.log(customers);
    // console.log(filteredIndices);
    document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
      filteredIndices.includes(i) ? e.classList.replace('d-none', 'd-flex') : e.classList.replace('d-flex', 'd-none');
    });
  }
}

updateMode = event => {
  event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.profile-view').classList.replace('d-flex', 'd-none');
  event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.profile-form').classList.replace('d-none', 'd-flex');
  event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.update-btn').classList.replace('d-block', 'd-none');
  event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.view-btn').classList.replace('d-block', 'd-none');
  event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.finish-update-btn').classList.replace('d-none', 'd-block');
  event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.cancel-update-btn').classList.replace('d-none', 'd-block');
}

submitUpdate = event => {
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.profile-form').submit();
  updateToView();
}

updateToView = event => {
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.profile-view').classList.replace('d-none', 'd-flex');
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.profile-form').classList.replace('d-flex', 'd-none');
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.update-btn').classList.replace('d-none', 'd-block');
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.view-btn').classList.replace('d-none', 'd-block');
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.finish-update-btn').classList.replace('d-block', 'd-none');
  event.target.parentElement.parentElement.parentElement.parentElement.querySelector('.cancel-update-btn').classList.replace('d-block', 'd-none');
}

viewProfile = event => {
  window.location.href = window.location.href.split('/').slice(0,-2).join('/') + `/customerInfo/${event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.target-id-span').textContent}`;
}

readImgFile = event => {
  if (event.target.files && event.target.files[0]) {
    let reader = new FileReader();

    reader.onload = e => {
      event.target.parentElement.querySelector('.editing-customer-img').src = e.target.result;
    }
    
    reader.readAsDataURL(event.target.files[0]);
  }
}

editImg = event => {
  event.target.parentElement.querySelector('.picture-input').click();
}

let hiddenByBirthday = [];
changeSort = () => {
  const AGE_SORT = document.querySelector('input[name="ageRadio"]:checked').value;
  const SEX_SORT = document.querySelector('input[name="sexRadio"]:checked').value;
  const NATIONALITY_SORT = document.querySelector('input[name="nationalityRadio"]:checked').value;
  const BIRTHDAY_SORT = document.querySelector('input[name="birthdayRadio"]:checked').value;
  const DIV_TYPES = ['all','sex0','sex1','sex2'];

  switch (AGE_SORT) {
    case 'any':
      break;
    case 'ascending':
      for (i in DIV_TYPES) {
        let agesArr = [];
        let maxOrder = 0;
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.age-span').textContent !== '') agesArr.push(e.querySelector('.age-span').textContent);
        });
        agesArrSorted = [...agesArr].sort((a,b) => a - b);
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
          if (e.querySelector('.age-span').textContent !== '') {
            e.style.order = agesArrSorted.indexOf(agesArr[i]);
            maxOrder++;
          }
        });
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
          if (e.querySelector('.age-span').textContent === '') e.style.order = i + maxOrder;
        });
      }
      break;
    case 'descending':
      for (i in DIV_TYPES) {
        let agesArr = [];
        let maxOrder = 0;
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.age-span').textContent !== '') agesArr.push(e.querySelector('.age-span').textContent);
        });
        agesArrSorted = [...agesArr].sort((a,b) => b - a);
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
          if (e.querySelector('.age-span').textContent !== '') {
            e.style.order = agesArrSorted.indexOf(agesArr[i]);
            maxOrder++;
          }
        });
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
          if (e.querySelector('.age-span').textContent === '') e.style.order = i + maxOrder;
        });
      }
      break;
  }

  switch (SEX_SORT) {
    case 'any':
      document.querySelector('.all-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex0-profiles-group').classList.replace('d-flex', 'd-none');
      document.querySelector('.sex1-profiles-group').classList.replace('d-flex', 'd-none');
      document.querySelector('.sex2-profiles-group').classList.replace('d-flex', 'd-none');
      break;
    case 'ascending':
      document.querySelector('.all-profiles-group').classList.replace('d-flex', 'd-none');
      document.querySelector('.sex0-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex1-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex2-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex0-profiles-group').style.order = 0;
      document.querySelector('.sex1-profiles-group').style.order = 1;
      document.querySelector('.sex2-profiles-group').style.order = 2;
      break;
    case 'descending':
      document.querySelector('.all-profiles-group').classList.replace('d-flex', 'd-none');
      document.querySelector('.sex0-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex1-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex2-profiles-group').classList.replace('d-none', 'd-flex');
      document.querySelector('.sex0-profiles-group').style.order = 2;
      document.querySelector('.sex1-profiles-group').style.order = 1;
      document.querySelector('.sex2-profiles-group').style.order = 0;
      break;
  }

  switch (NATIONALITY_SORT) {
    case 'any':
      break;
    case 'ascending':
      for (i in DIV_TYPES) {
        let nationalityArr = [];
        let maxOrder = 0;
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.nationality-field').value !== '') nationalityArr.push(e.querySelector('.nationality-field').value);
        });
        let nationalityArrSorted = [...nationalityArr];
        nationalityArrSorted.sort();
        let iter = 0;
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.nationality-field').value !== '') {
            e.style.order = nationalityArrSorted.indexOf(nationalityArr[iter]);
            // console.log(nationalityArrSorted.indexOf(nationalityArr[iter]), nationalityArr[iter], nationalityArrSorted[nationalityArrSorted.indexOf(nationalityArr[iter])])
            nationalityArr[iter] = '';
            iter++;
            maxOrder++;
          }
        });
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.nationality-field').value === '') {
            e.style.order = iter + maxOrder;
            iter++;
          }
        });
      }
      break;
    case 'descending':
      for (i in DIV_TYPES) {
        let nationalityArr = [];
        let maxOrder = 0;
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.nationality-field').value !== '') nationalityArr.push(e.querySelector('.nationality-field').value);
        });
        let nationalityArrSorted = [...nationalityArr];
        nationalityArrSorted.sort().reverse();
        let iter = 0;
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.nationality-field').value !== '') {
            e.style.order = nationalityArrSorted.indexOf(nationalityArr[iter]);
            // console.log(nationalityArrSorted.indexOf(nationalityArr[iter]), nationalityArr[iter], nationalityArrSorted[nationalityArrSorted.indexOf(nationalityArr[iter])])
            nationalityArr[iter] = '';
            iter++;
            maxOrder++;
          }
        });
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach(e => {
          if (e.querySelector('.nationality-field').value === '') {
            e.style.order = iter + maxOrder;
            iter++;
          }
        });
      }
      break;
  }

  switch (BIRTHDAY_SORT) {
    case 'all':
      for (i in DIV_TYPES) {
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
          if (hiddenByBirthday.includes(i)) {
            e.classList.replace('d-none', 'd-flex');
            hiddenByBirthday.splice(hiddenByBirthday.indexOf(i),1);
          }
        })
      }
      break;
    case 'currMonth':
      for (i in DIV_TYPES) {
        document.querySelector(`.${DIV_TYPES[i]}-profiles-group`).querySelectorAll('.search-group').forEach((e,i) => {
          if (e.querySelector('.is-curr-month-birthday-span').textContent === 'false') {
            if (e.classList.contains('d-flex')) hiddenByBirthday.push(i);
            e.classList.replace('d-flex', 'd-none');
          }
        });
      }
      break;
  }
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
