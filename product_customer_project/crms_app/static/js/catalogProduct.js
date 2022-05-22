let minRating = 0;
let minPrice = 0;
let maxPrice = 9999999;

window.onload = () => {
  handleWindowResize();
  window.addEventListener('resize', handleWindowResize);
  document.querySelectorAll('input[name="categoryRadio"]').forEach(e => {
    e.addEventListener('change', changeCategory);
  });
  document.querySelectorAll('input[type="checkbox"]').forEach(e => {
    e.addEventListener('change', changeSubcategory);
  });
  document.querySelectorAll('input[name="ratingsRadio"]').forEach(e => {
    e.addEventListener('change', changeMinRating);
  });
  document.querySelector('.apply-pricing-filter-btn').addEventListener('click', changePrice);

  document.getElementById('sortSelect').addEventListener('change', changeSort);
  document.querySelector('.search-products-btn').addEventListener('click', searchProducts);

  document.querySelectorAll('.product-card').forEach(e => {
    e.querySelector('.product-condition-complaint').addEventListener('click', initializeComplaintModal);
    e.querySelector('.misleading-info-complaint').addEventListener('click', initializeComplaintModal);
    e.querySelector('.pornography-complaint').addEventListener('click', initializeComplaintModal);
  })

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
  });
};

handleWindowResize = () => {
  document.querySelectorAll('.product-card').forEach(e => {
    e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.replace('...', '');
    if (window.innerWidth < 1720) e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.slice(0, 64) + '...';
    else if (window.innerWidth >= 1720) e.querySelector('.product-name').textContent = e.querySelector('.product-name').textContent.slice(0, 80) + '...';
  })
}

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
  });
  if (checkedSubs.length) {
    checkedSubs = checkedSubs.map(e => {
      return e.replace(/([A-Z])/, '-$1').toLowerCase();
    });
    document.querySelectorAll('.products-group').forEach(e => {
      let sub = e.classList[1].replace('-sub-products', '');
      if (checkedSubs.includes(sub)) e.classList.replace('d-none', 'd-flex');
      else if (!checkedSubs.includes(sub)) e.classList.replace('d-flex', 'd-none');
    });
  } else {
    document.querySelectorAll('.products-group').forEach(e => {
      e.classList.replace('d-none', 'd-flex')
    });
  }
}

changeMinRating = e => {
  minRating = e.target.value;
  handleRatingPriceChange();
}

changePrice = () => {
  minPrice = document.getElementById('minPriceField').value;
  maxPrice = document.getElementById('maxPriceField').value;
  handleRatingPriceChange();
}

handleRatingPriceChange = () => {
  document.querySelectorAll('.product-card').forEach(e => {
    const RATING = Number(e.querySelector('.full-stars').style.width.replace('%','')) / 20;
    let price = 99999999;
    if (e.querySelector('.discounted-price')) {
      price = Number(e.querySelector('.discounted-price').textContent.replace('₱',''));
    } else if (!e.querySelector('.discounted-price')) {
      price = Number(e.querySelector('.original-price').textContent.replace('₱',''));
    }
    
    if (RATING >= minRating && price >= minPrice && price <= maxPrice) {
      setTimeout(e.classList.replace('d-none', 'd-flex'), 300)
    } else {
      setTimeout(e.classList.replace('d-flex', 'd-none'), 300)
    }
  });
}

changeSort = event => {
  switch (event.target.value) {
    case 'dateAddedDescending':
      document.querySelectorAll('.products-group').forEach(e => {
        let idArr = [];
        e.querySelectorAll('.product-card').forEach(f => idArr.push(f.querySelector('.product-id').textContent));
        idArr.sort((a,b) => a - b);
        e.querySelectorAll('.product-card').forEach(f => {
          f.style.order = (f.querySelector('.product-id').textContent - idArr[idArr.length-1]) * -1;
        });
      })
      break;
    case 'dateAddedAscending':
      document.querySelectorAll('.products-group').forEach(e => {
        let idArr = [];
        e.querySelectorAll('.product-card').forEach(f => idArr.push(f.querySelector('.product-id').textContent));
        idArr.sort((a,b) => a - b);
        e.querySelectorAll('.product-card').forEach(f => {
          f.style.order = f.querySelector('.product-id').textContent - idArr[0];
        });
      });
      break;
    case 'popularityDescending':
      document.querySelectorAll('.products-group').forEach(e => {
        let ratingsCountArr = [];
        e.querySelectorAll('.product-card').forEach(f => ratingsCountArr.push(f.querySelector('.product-rating').textContent.match(/\d+/g)));
        ratingsCountArr = ratingsCountArr.map(arr => arr.reduce((partialSum, curr) => partialSum + Number(curr), 0));
        ratingsCountArrSorted = [...ratingsCountArr].sort((a,b) => b - a);
        e.querySelectorAll('.product-card').forEach((f,i) => {
          f.style.order = ratingsCountArrSorted.indexOf(ratingsCountArr[i]);
        });
      });
      break;
    case 'popularityAscending':
      document.querySelectorAll('.products-group').forEach(e => {
        let ratingsCountArr = [];
        e.querySelectorAll('.product-card').forEach(f => ratingsCountArr.push(f.querySelector('.product-rating').textContent.match(/\d+/g)));
        ratingsCountArr = ratingsCountArr.map(arr => arr.reduce((partialSum, curr) => partialSum + Number(curr), 0));
        ratingsCountArrSorted = [...ratingsCountArr].sort((a,b) => a - b);
        e.querySelectorAll('.product-card').forEach((f,i) => {
          f.style.order = ratingsCountArrSorted.indexOf(ratingsCountArr[i]);
        });
      });
      break;
    case 'ratingDescending':
      document.querySelectorAll('.products-group').forEach(e => {
        let ratingsArr = [];
        e.querySelectorAll('.product-card').forEach(f => ratingsArr.push(Number(f.querySelector('.full-stars').style.width.replace('%','')) / 20));
        ratingsArrSorted = [...ratingsArr].sort((a,b) => b - a);
        e.querySelectorAll('.product-card').forEach((f,i) => {
          f.style.order = ratingsArrSorted.indexOf(ratingsArr[i]);
        });
      });
      break;
    case 'ratingAscending':
      document.querySelectorAll('.products-group').forEach(e => {
        let ratingsArr = [];
        e.querySelectorAll('.product-card').forEach(f => ratingsArr.push(Number(f.querySelector('.full-stars').style.width.replace('%','')) / 20));
        ratingsArrSorted = [...ratingsArr].sort((a,b) => a - b);
        e.querySelectorAll('.product-card').forEach((f,i) => {
          f.style.order = ratingsArrSorted.indexOf(ratingsArr[i]);
        });
      });
      break;
    case 'priceDescending':
      document.querySelectorAll('.products-group').forEach(e => {
        let priceArr = [];
        e.querySelectorAll('.product-card').forEach(f => {
          if (f.querySelector('.discounted-price')) {
            priceArr.push(Number(f.querySelector('.discounted-price').textContent.replace('₱','')));
          } else if (!f.querySelector('.discounted-price')) {
            priceArr.push(Number(f.querySelector('.original-price').textContent.replace('₱','')));
          }
        });
        priceArrSorted = [...priceArr].sort((a,b) => b - a);
        e.querySelectorAll('.product-card').forEach((f,i) => {
          f.style.order = priceArrSorted.indexOf(priceArr[i]);
        });
      });
      break;
    case 'priceAscending':
      document.querySelectorAll('.products-group').forEach(e => {
        let priceArr = [];
        e.querySelectorAll('.product-card').forEach(f => {
          if (f.querySelector('.discounted-price')) {
            priceArr.push(Number(f.querySelector('.discounted-price').textContent.replace('₱','')));
          } else if (!f.querySelector('.discounted-price')) {
            priceArr.push(Number(f.querySelector('.original-price').textContent.replace('₱','')));
          }
        });
        priceArrSorted = [...priceArr].sort((a,b) => a - b);
        e.querySelectorAll('.product-card').forEach((f,i) => {
          f.style.order = priceArrSorted.indexOf(priceArr[i]);
        });
      });
      break;
  }
}

searchProducts = () => {
  document.querySelectorAll('.product-card').forEach(e => {
    if (e.querySelector('.product-name').textContent.includes(document.getElementById('searchProductsField').value)) {
      e.classList.replace('d-none', 'd-flex');
    } else {
      e.classList.replace('d-flex', 'd-none');
    }
  });
}

initializeComplaintModal = event => {
  document.querySelector('.product-complaint-modal').querySelector('.complaint-product-name').textContent = event.target.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector('.product-name').textContent;
  document.querySelector('.product-complaint-modal').querySelector('.product-complaint-select').value = (event.target.textContent.charAt(0).toLowerCase() + event.target.textContent.slice(1,)).split(' ').join('');
}

shortenDecimal = num => {
  return Math.round((num + Number.EPSILON) * (10 ** 2)) / (10 ** 2);
}
