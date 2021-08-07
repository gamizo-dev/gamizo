// // Menu js
// var hamburger = document.getElementById("hamburger");
// var menu = document.getElementById("menu");
// var line = document.getElementsByClassName("line");

// var i = 0;
// hamburger.addEventListener("click", function () {
//   hamburger.classList.toggle("menu-open");
//   menu.classList.toggle("menu-open");
//   for (i = 0; i < line.length; i++) {
//     line[i].classList.toggle("menu-open");
//   }
// });
document.addEventListener('contextmenu', event => event.preventDefault());

var menuBtn = document.querySelector(".menu-btn");
var sideMenu = document.querySelector("#nav-menu");
var crossBtn = document.querySelector("#nav-menu .menu-btn")
// var show=true;
// var i=0;
menuBtn.addEventListener('click', () =>{
  sideMenu.setAttribute("style","display:block;")
})

crossBtn.addEventListener('click', () => {
  sideMenu.setAttribute("style", "display:none;")
})

// document.addEventListener('click', () => {
//   if(show!=true && sideMenu.style.display=="block"){
//   sideMenu.setAttribute("style","display:none;")
// }
// })
