console.log(PRODUCTS);

window.onload = () => {
  let productCards = document.querySelectorAll('.product-card');

  for (i in PRODUCTS ) {
    for (j in productCards) {
      if (PRODUCTS[i].name == productCards[j].querySelector('.card-title').textContent) {
        productCards[j].querySelector('.ratings').title = PRODUCTS[i].rating + '/5';
        productCards[j].querySelector('.full-stars').style.width = 20 * PRODUCTS[i].rating + '%';
        break;
      }
    }
  }
  const percentage = '50%';
};
