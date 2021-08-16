//videoplayer js
const videos = document.getElementsByClassName("impvideo");
// const play_btn = document.querySelectorAll(".play_arrow");

const play_btn = document.getElementsByClassName("play_arrow");
var z = 0;
// const backvideos= document.getElementsByClassName("backdrop-video");
function newfunc() {
  for (var i = 0; i < videos.length; i++) {
    elementInViewport(videos[i]);
  }
}
function elementInViewport(videos) {
  var bounding = videos.getBoundingClientRect();

  if (
    bounding.top >= 0 &&
    bounding.left >= 0 &&
    bounding.right <=
      (window.innerWidth || document.documentElement.clientWidth) &&
    bounding.bottom <=
      (window.innerHeight || document.documentElement.clientHeight)
  ) {
    // console.log('Element is in the viewport!');
    if(z){

      videos.play();
    }
    // return 1;
    
    videos.loop = true;
  } else {
    // console.log('Element is NOT in the viewport!');
    videos.pause();
    // return 0;
    videos.loop = false;
  }
}

// window.addEventListener('resize', checkScroll, false);
// function disappearArrow(){
//   if(z==1){
//   for( var r=0;r<play_btn.length;r++){
//   play_btn[r].style.opacity=0;
//   }
// }
// }

function disappearArrow() {
  for (var r = 0; r < play_btn.length; r++) {
    play_btn[r].style.opacity = 0;
    z=1;
  }
}
// document.addEventListener("click", disappearArrow, (z = 1), false);
document.addEventListener("click", disappearArrow,true);

// document.addEventListener("scroll", disappearArrow, false);
window.addEventListener("click", newfunc, false);
window.addEventListener("scroll", newfunc, false);
