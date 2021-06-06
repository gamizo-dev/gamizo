var hamburger = document.getElementById("hamburger");
var menu = document.getElementById("menu");
var line = document.getElementsByClassName("line");

var i = 0;
hamburger.addEventListener("click", function () {
  hamburger.classList.toggle("menu-open");
  menu.classList.toggle("menu-open");
  for (i = 0; i < line.length; i++) {
    line[i].classList.toggle("menu-open");
  }
});
