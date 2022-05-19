window.onload = () => {
  document.querySelectorAll('.product-card').forEach(e => {
    console.log(e.querySelector('.product-rating').textContent.match(/\d+/g));
    const RATING_ARR = e.querySelector('.product-rating').textContent.match(/\d+/g);
    let avg = 0;
    let count = 0;
    for (let i = 0; i < RATING_ARR.length; i++) {
      avg += RATING_ARR[i] * i+1;
      count += Number(RATING_ARR[i]);
    }
    avg = shortenDecimal(avg / count);
    e.querySelector('.full-stars').style.width = avg * 20 + '%';
  })

  document.query
};

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** 2)) / (10 ** 2);
}
