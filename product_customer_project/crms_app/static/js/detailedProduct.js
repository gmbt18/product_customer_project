window.onload = () => {
  formatImgsCarousel();
  
  const RATING_ARR = document.querySelector('.product-rating').textContent.match(/\d+/g);
  let avg = 0;
  let count = 0;
  for (let i = 0; i < RATING_ARR.length; i++) {
    avg += RATING_ARR[i] * (i+1);
    count += Number(RATING_ARR[i]);
  }
  avg = shortenDecimal(avg / count);
  console.log(avg);
  document.querySelector('.product-rating').textContent = `${avg}/5`;
  document.querySelector('.full-stars').title = `${shortenDecimal(avg)}/5 (${count} ratings)\n1* - ${RATING_ARR[0]} ratings\n2* - ${RATING_ARR[1]} ratings\n3* - ${RATING_ARR[2]} ratings\n4* - ${RATING_ARR[3]} ratings\n5* - ${RATING_ARR[4]} ratings`;
  document.querySelector('.full-stars').style.width = shortenDecimal(avg * 20) + '%';
}

formatImgsCarousel = () => {
  /*
    css adapted from and credits to
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
    end copied css
  */
}

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** 2)) / (10 ** 2);
}
