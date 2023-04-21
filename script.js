
const path = './assets/slideshow/';
const images = [
    'image1.png',
    'image2.png',
    'image3.png',
    'image4.png',
];

let currentIndex = 0;
const heroImage = document.querySelector('.hero-image');

function changeBackgroundImage() {
    heroImage.style.backgroundImage = `url('${path}${images[currentIndex]}')`;
    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(changeBackgroundImage, 2000); 