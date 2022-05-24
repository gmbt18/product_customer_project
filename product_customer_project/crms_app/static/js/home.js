window.onload = () => {
  document.querySelectorAll('.login-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-login').click());
  });
  document.querySelectorAll('.products-catalog-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-catalog-product').click());
  });
  document.querySelectorAll('.monthly-catalog-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-catalog-monthly').click());
  });
  document.querySelectorAll('.advanced-search-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-advanced-search').click());
  });
  document.querySelectorAll('.profile-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-profile').click());
  });
  document.querySelectorAll('.change-password-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-change-password').click());
  });
  document.querySelectorAll('.forgot-password-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-forgot-password').click());
  });
  document.querySelectorAll('.logout-btn').forEach(e => {
    e.addEventListener('click', () => document.querySelector('.to-logout').click());
  });
}