const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector("nav");

btnNavEl.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});
