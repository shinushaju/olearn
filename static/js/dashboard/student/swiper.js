import Swiper from 'https://unpkg.com/swiper@7/swiper-bundle.esm.browser.min.js'

const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    autoHeight: true,
    slidesPerView: 4,
    spaceBetween: 10,

    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 1,
            spaceBetween: 10
        },
        // when window width is >= 480px
        480: {
            slidesPerView: 1,
            spaceBetween: 10
        },
        // when window width is >= 640px
        640: {
            slidesPerView: 4,
            spaceBetween: 10
        }
    },
    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
    },
});