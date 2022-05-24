window.onload = () => {
  document.querySelector('.update-btn').addEventListener('click', updateMode);
  document.querySelector('.finish-update-btn').addEventListener('click', submitUpdate);
  document.querySelector('.cancel-update-btn').addEventListener('click', cancelUpdate);
  document.querySelector('.add-btn').addEventListener('click', addMode);
  document.querySelector('.finish-adding-btn').addEventListener('click', submitAddition);
  document.querySelector('.cancel-adding-btn').addEventListener('click', cancelAdding);
  document.querySelector('.subscribe-btn').addEventListener('subscribe', subscribe);
}

updateMode = () => {
  document.querySelectorAll('input').forEach(e => e.disabled = false);
}

submitUpdate = () => {
  
}
