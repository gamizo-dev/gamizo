//videoplayer js
const videos = document.getElementsByClassName("impvideo");
const play_btn = DocumentTimeline.getElementsByClassName("play_arrow");
// const backvideos= document.getElementsByClassName("backdrop-video");
function newfunc() {
  for (var i = 0; i < videos.length; i++) {
    elementInViewport(videos[i]);
  }
}
function elementInViewport(videos) {
  var bounding = videos.getBoundingClientRect();

  if ( bounding.top >= 0 && bounding.left >= 0 && bounding.right <= (window.innerWidth || document.documentElement.clientWidth) && bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)) {
    // console.log('Element is in the viewport!');
    videos.play();
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

window.addEventListener("scroll", newfunc, false);

