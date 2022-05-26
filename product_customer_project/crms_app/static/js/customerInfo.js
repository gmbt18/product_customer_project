window.onload = () => {
  document.querySelector('.update-btn').addEventListener('click', updateMode);
  document.querySelector('.finish-update-btn').addEventListener('click', submitUpdate);
  document.querySelector('.cancel-update-btn').addEventListener('click', updateToView);
  document.querySelector('.editing-customer-img').addEventListener('click', editImg);
  document.getElementById('pictureInput').addEventListener('change', readImgFile);
  if (document.querySelector('.superuser-span').textContent === 'True') {
    document.querySelector('.add-btn').addEventListener('click', addMode);
    document.querySelector('.finish-adding-btn').addEventListener('click', submitAdd);
    document.querySelector('.cancel-adding-btn').addEventListener('click', addToView);
  } else { 
    document.querySelectorAll('.subscription-btn').forEach(e => {
      if (document.querySelector('.subscription-span').textContent === 'True') {
        e.textContent = 'Unsubscribe';
      } else e.textContent = 'Subscribe';
      e.addEventListener('click', handleSubscription);
    });
  }

  if (document.querySelector('.is-new-span').textContent === 'True') {
    console.log('what')
    document.querySelector('.update-btn').click();
  }

  switch (document.getElementById('sexField').value) {
    case '0':
      document.getElementById('sexField').value = 'Male';
      break;
    case '1':
      document.getElementById('sexField').value = 'Female';
      break;
    case '2':
      document.getElementById('sexField').value = 'Intersex';
      break;
  }

  document.getElementById('birthdayField').value = document.getElementById('birthdayField').value.split(',').slice(0,-1).join(',');
  document.querySelectorAll('.customer-name').forEach(e => e.addEventListener('click', viewProfile));
  if (document.querySelector('.birthday-span')) {
    let birthdayArr = document.querySelector('.birthday-span').textContent.split(',').slice(0,-1).join('').split(' ');
    switch (birthdayArr[0]) {
      case 'January':
        birthdayArr[0] = '01';
        break;
      case 'February':
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
      case 'August':
        birthdayArr[0] = '08';
        break;
      case 'September':
        birthdayArr[0] = '09';
        break;
      case 'October':
        birthdayArr[0] = '10';
        break;
      case 'November':
        birthdayArr[0] = '11';
        break;
      case 'December':
        birthdayArr[0] = '12';
        break;
    }
    birthdayArr[1] = '0' + birthdayArr[1];
    document.getElementById('birthdayInput').value = `${birthdayArr[2]}-${birthdayArr[0]}-${birthdayArr[1]}`;
  }
}

updateMode = () => {
  document.querySelector('.profile-view').classList.replace('d-flex', 'd-none');
  document.querySelector('.profile-form').classList.replace('d-none', 'd-flex');
  // document.querySelector('.profile-form').action = document.querySelector('.customer-update-url').textContent;
  document.querySelector('.update-btn').classList.replace('d-block', 'd-none');
  if (document.querySelector('.superuser-span').textContent === 'True') {
    document.querySelector('.add-btn').classList.replace('d-block', 'd-none');
    document.querySelector('.finish-adding-btn').classList.replace('d-block', 'd-none');
    document.querySelector('.cancel-adding-btn').classList.replace('d-block', 'd-none');
  } else document.querySelector('.subscription-btn').classList.replace('d-block', 'd-none');
  document.querySelector('.finish-update-btn').classList.replace('d-none', 'd-block');
  document.querySelector('.cancel-update-btn').classList.replace('d-none', 'd-block');
}

submitUpdate = () => {
  document.querySelector('.profile-form').submit();
  updateToView();
}

updateToView = () => {
  document.querySelector('.profile-view').classList.replace('d-none', 'd-flex');
  document.querySelector('.profile-form').classList.replace('d-flex', 'd-none');
  document.querySelector('.update-btn').classList.replace('d-none', 'd-block');
  if (document.querySelector('.superuser-span').textContent === 'True') {
    document.querySelector('.add-btn').classList.replace('d-none', 'd-block');
  } else document.querySelector('.subscription-btn').classList.replace('d-none', 'd-block');
  document.querySelector('.finish-update-btn').classList.replace('d-block', 'd-none');
  document.querySelector('.cancel-update-btn').classList.replace('d-block', 'd-none');
}

readImgFile = event => {
  if (event.target.files && event.target.files[0]) {
    let reader = new FileReader();

    reader.onload = e => {
      document.querySelector('.editing-customer-img').src = e.target.result;
    }
    
    reader.readAsDataURL(event.target.files[0]);
  }
}

editImg = () => {
  document.getElementById('pictureInput').click();
}

addMode = () => {
  document.querySelector('.register-link').click();
}

submitAdd = () => {

}

addToView = () => {

}

handleSubscription = event => {
  if (event.target.textContent === 'Subscribe') document.querySelector('.subscribe-link').click();
  else document.querySelector('.unsubscribe-link').click();
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
