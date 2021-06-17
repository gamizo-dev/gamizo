// Menu js
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


//Video Player js
var videoC = document.querySelector(".game-video");
var video = document.getElementById("video");

// video.addEventListener("load", () => {
//   if (video.played == flase) {
//     videoC.addEventListener("click", ()=>{
//       video.play();
//       console.log("playing success")
//     })
//   } 
//   else {
//     continue;
//   }
// });

videoC.addEventListener("click", () => {
  if (video.volume == 0.0) {
    video.volume = 1.0;
  } else {
    video.volume = 0.0;
  }
});
