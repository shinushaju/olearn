var swiper = new Swiper(".swiper", {
        
    slidesPerView: 1,
    spaceBetween: 16,

    autoplay: {
    delay: 3000,
    },

    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });
