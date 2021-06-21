//Video Player js
// var videoC = document.querySelector(".game-video");
// var video = document.getElementById("video").autoplay;

// // video.addEventListener("load", () => {
// //   if (video.played == flase) {
// //     videoC.addEventListener("click", ()=>{
// //       video.play();
// //       console.log("playing success")
// //     })
// //   } 
// //   else {
// //     continue;
// //   }
// // });

// video.addEventListener("pause", () => {
// 	videoC.addEventListener("click", () =>{
// 		video.play();
// 	})
// })

// videoC.addEventListener("click", () => {
//   if (video.volume == 0.0) {
//     video.volume = 1.0;
//   } else {
//     video.volume = 0.0;
//   }
// });

// var videos = document.getElementsByClassName("impvideo"),
// fraction = 0.8;
// function checkScroll() {

//     for(var i = 0; i < videos.length; i++) {

//         var video = videos[i];

//         var y = video.offsetTop, h = video.offsetHeight,
//             b = y + h, //bottom
//             visibleY, visible;

//             // visibleX = Math.max(0, Math.min(w, window.pageXOffset + window.innerWidth - x, r - window.pageXOffset));
//             visibleY = Math.max(0, Math.min(h, window.pageYOffset + window.innerHeight - y, b - window.pageYOffset));

//             visible = visibleY / h;

//             if (visible > fraction) {
//                 video.play();
//             } else {
//                 video.pause();
//             }

//     }

// }
const videos = document.getElementsByClassName('impvideo');
for(i=0;i<videos.length;i++){
  videos[i].pause()
}
const observer = new IntersectionObserver(entries => {
    // Loop over the entries
    for(i=0;i<videos.length;i++){
      video=videos[i];
    entries.forEach(entry => {
      // If the element is visible
      if (entry.isIntersecting) {
        // Add the animation class
        video.play();
        return;
      }
      video.pause();
    });
  }
  });
  for(i=0;i<videos.length;i++){
  observer.observe(videos[i]);
  }

// window.addEventListener('scroll', checkScroll, false);
// window.addEventListener('resize', checkScroll, false);
