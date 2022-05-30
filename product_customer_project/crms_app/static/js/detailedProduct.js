const TODAY = new Date();
const DATE = (TODAY.getMonth()+1)+'/'+TODAY.getDate()+'/'+(TODAY.getFullYear()-2000);

window.onload = () => {
  formatImgsCarousel();

  document.getElementById('quantityMinusBtn').addEventListener('click', minusQuantity);
  document.getElementById('quantityAddBtn').addEventListener('click', addQuantity);

  document.getElementById('smallImgsCarousel').querySelectorAll('img').forEach(e => {
    e.addEventListener('click', changeMainImg);
  });

  const RATING_ARR = document.querySelector('.product-rating').textContent.match(/\d+/g);
  let avg = 0;
  let count = 0;
  for (let i = 0; i < RATING_ARR.length; i++) {
    avg += RATING_ARR[i] * (i+1);
    count += Number(RATING_ARR[i]);
  }
  avg = !isNaN(shortenDecimal(avg / count)) ? shortenDecimal(avg / count) : 0;
  document.querySelector('.product-rating').textContent = `${avg}/5`;
  document.querySelector('.full-stars').title = `${shortenDecimal(avg)}/5 (${count} ratings)\n1* - ${RATING_ARR[0]} ratings\n2* - ${RATING_ARR[1]} ratings\n3* - ${RATING_ARR[2]} ratings\n4* - ${RATING_ARR[3]} ratings\n5* - ${RATING_ARR[4]} ratings`;
  document.querySelector('.full-stars').style.width = shortenDecimal(avg * 20) + '%';

  // const RATING_ARR = document.querySelector('.product-rating').textContent;
  // document.querySelector('.product-rating').textContent = `${RATING_ARR}/5`;
  // document.querySelector('.full-stars').style.width = shortenDecimal(RATING_ARR * 20) + '%';

  document.querySelector('.input-empty-stars').querySelectorAll('.fa-star').forEach((e,i) => {
    e.addEventListener('click', () => rate(i+1));
  });
  document.querySelector('.input-full-stars').querySelectorAll('.fa-star').forEach((e,i) => {
    e.addEventListener('click', () => rate(i+1));
  });
  document.querySelector('.date-today').textContent = DATE;
  document.querySelector('.submit-review-btn').addEventListener('click', submitReview);
  fixReviews();
}

formatImgsCarousel = () => {
  /*
    code adapted from and credits to
    https://stackoverflow.com/questions/20007610/bootstrap-carousel-multiple-frames-at-once
    https://www.codeply.com/p/0CWffz76Q9
  */
  let items = document.querySelectorAll('.carousel .carousel-item')

  items.forEach((el) => {
      // number of slides per carousel-item
      const minPerSlide = 4
      let next = el.nextElementSibling
      for (let i=1; i<minPerSlide; i++) {
          if (!next) {
              // wrap carousel by using first child
              next = items[0]
          }
          let cloneChild = next.cloneNode(true)
          el.appendChild(cloneChild.children[0])
          next = next.nextElementSibling
      }
  })
  /* 
    end copied code
  */
}

addQuantity = () => {
  document.getElementById('quantityField').value = Number(document.getElementById('quantityField').value) + 1;
}

minusQuantity = () => {
  document.getElementById('quantityField').value = Number(document.getElementById('quantityField').value) - 1;
}

changeMainImg = event => {
  document.querySelector('.main-image').src = event.target.src;
}

rate = num => {
  document.querySelector('.input-full-stars').style.width = num*20 + '%';
  document.getElementById('ratingField').value = num;
  console.log(document.getElementById('ratingField').value)
}

submitReview = () => {
  document.querySelector('.review-form').submit();
}

fixReviews = () => {
  let dates = [];
  document.querySelectorAll('.review-div').forEach(e => {
    e.querySelector('.full-stars').style.width = shortenDecimal(e.querySelector('.rating-span').textContent * 20) + '%';
    dates.push(e.querySelector('.review-date').textContent);
  });
}

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** 2)) / (10 ** 2);
}
