window.onload = () => {
  formatImgsCarousel();
}

formatImgsCarousel = () => {
  /*
    css adapted from and credits to
    https://stackoverflow.com/questions/20007610/bootstrap-carousel-multiple-frames-at-once
    https://www.codeply.com/p/0CWffz76Q9
  */
  let items = document.querySelectorAll('.carousel .carousel-item')
  console.log(items)
  
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
