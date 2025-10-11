let index = 0;
const carousel = document.getElementById("carousel");
const images = carousel.children;
setInterval(() => {
  index = (index + 1) % images.length;
  carousel.style.transform = `translateX(-${index * 100}%)`;
}, 3000);

