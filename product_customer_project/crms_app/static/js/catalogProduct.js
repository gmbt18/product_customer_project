window.onload = () => {
  document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
    e.addEventListener('change', changeCategory);
  });
  document.querySelectorAll('input[type="checkbox"]').forEach(e => {
    e.addEventListener('change', changeSubcategory);
  });

  document.querySelectorAll('input[name="ratingsRadio"]').forEach(e => {
    e.addEventListener('change', changeMinRating);
  });

  document.querySelectorAll('.product-card').forEach(e => {
    const RATING_ARR = e.querySelector('.product-rating').textContent.match(/\d+/g);
    let avg = 0;
    let count = 0;
    for (let i = 0; i < RATING_ARR.length; i++) {
      avg += RATING_ARR[i] * (i+1);
      count += Number(RATING_ARR[i]);
    }
    avg = shortenDecimal(avg / count);
    e.querySelector('.full-stars').title = `${shortenDecimal(avg)}/5 (${count} ratings)\n1* - ${RATING_ARR[0]} ratings\n2* - ${RATING_ARR[1]} ratings\n3* - ${RATING_ARR[2]} ratings\n4* - ${RATING_ARR[3]} ratings\n5* - ${RATING_ARR[4]} ratings`;
    e.querySelector('.full-stars').style.width = shortenDecimal(avg * 20) + '%';

    e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.slice(0, 80) + '...';
  });
};

changeCategory = () => {
  const CURR_CATEGORY = document.querySelector('input[name="categoryRadio"]:checked').value;
  const SPINAL_CATEGORY = CURR_CATEGORY.replace(/([A-Z])/, '-$1').toLowerCase();
  document.querySelectorAll('input[type="checkbox"]').forEach(e => e.checked = false)
  document.querySelector('.curr-category').textContent = CURR_CATEGORY.charAt(0).toUpperCase() + CURR_CATEGORY.slice(1,CURR_CATEGORY.length);
  document.querySelector('.audio-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.clothes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.shoes-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.tech-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector('.accessories-filter-subcategories').classList.replace('d-flex', 'd-none');
  document.querySelector(`.${CURR_CATEGORY}-filter-subcategories`).classList.replace('d-none', 'd-flex');
  document.querySelectorAll('.audio-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.clothes-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.shoes-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.tech-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll('.accessories-cat-products').forEach(e => e.classList.replace('d-flex', 'd-none'));
  document.querySelectorAll(`.${SPINAL_CATEGORY}-cat-products`).forEach(e => e.classList.replace('d-none', 'd-flex'));
}

changeSubcategory = () => {
  let checkedSubs = [];
  document.querySelectorAll('input[type="checkbox"]:checked').forEach(e => {
    checkedSubs.push(e.value);
  })
  if (checkedSubs.length) {
    checkedSubs = checkedSubs.map(e => {
      return e.replace(/([A-Z])/, '-$1').toLowerCase();
    })
    document.querySelectorAll('.products-group').forEach(e => {
      let sub = e.classList[1].replace('-sub-products', '');
      if (checkedSubs.includes(sub)) e.classList.replace('d-none', 'd-flex');
      else if (!checkedSubs.includes(sub)) e.classList.replace('d-flex', 'd-none');
    })
  } else {
    document.querySelectorAll('.products-group').forEach(e => {
      e.classList.replace('d-none', 'd-flex')
    })
  }
}

changeMinRating = event => {
  document.querySelectorAll('.product-card').forEach(e => {
    if (Number(e.querySelector('.full-stars').style.width.replace('%','')) / 20 >= event.target.value) {
      e.classList.replace('d-none', 'd-flex');
    } else {
      e.classList.replace('d-flex', 'd-none');
    }
  })
}

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** 2)) / (10 ** 2);
}