window.onload = () => {
  document.querySelector('.update-btn').addEventListener('click', updateMode);
  document.querySelector('.finish-update-btn').addEventListener('click', submitUpdate);
  document.querySelector('.cancel-update-btn').addEventListener('click', updateToView);
  if (document.querySelector('.superuser-span').textContent === 'True') {
    document.querySelector('.add-btn').addEventListener('click', addMode);
    document.querySelector('.finish-adding-btn').addEventListener('click', submitAdd);
    document.querySelector('.cancel-adding-btn').addEventListener('click', addToView);
  } else document.querySelector('.subscribe-btn').addEventListener('click', subscribe);
}

updateMode = () => {
  document.querySelector('.profile-view').classList.replace('d-flex', 'd-none');
  document.querySelector('.profile-form').classList.replace('d-none', 'd-flex');
  document.querySelector('.profile-form').action = document.querySelector('.customer-update-url').textContent;
  document.querySelector('.update-btn').classList.replace('d-block', 'd-none');
  if (document.querySelector('.superuser-span').textContent === 'True') {
    document.querySelector('.add-btn').classList.replace('d-block', 'd-none');
    document.querySelector('.finish-adding-btn').classList.replace('d-block', 'd-none');
    document.querySelector('.cancel-adding-btn').classList.replace('d-block', 'd-none');
  } else document.querySelector('.subscribe-btn').classList.replace('d-block', 'd-none');
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
  } else document.querySelector('.subscribe-btn').classList.replace('d-none', 'd-block');
  document.querySelector('.finish-update-btn').classList.replace('d-block', 'd-none');
  document.querySelector('.cancel-update-btn').classList.replace('d-block', 'd-none');
}

addMode = () => {

}

submitAdd = () => {

}

addToView = () => {

}

subscribe = () => {

}
