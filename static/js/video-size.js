var video = document.querySelectorAll(".impvideo");
var main = document.querySelectorAll(".game-video");
var backVideo = document.querySelectorAll(".backdrop-video");

function videoResize() {
  for (i = 0; i < video.length; i++) {
    console.log("resizing");
    if (video[i].offsetHeight > video[i].offsetWidth) {
      video[i].setAttribute("style", `max-height: ${main[i].offsetHeight}px;`);
      backVideo[i].setAttribute(
        "style",
        `max-width: ${main[i].offsetWidth}px;`
      );
    } else if (video[i].offsetHeight < video[i].offsetWidth) {
      video[i].setAttribute("style", `max-width: ${main[i].offsetWidth}px;`);
      backVideo[i].setAttribute(
        "style",
        `max-height: ${main[i].offsetHeight}px;`
      );
    } else if (video[i].offsetHeight == video[i].offsetWidth) {
      video[i].setAttribute("style", `max-width: ${main[i].offsetWidth}px;`);
    }
  }
}

window.addEventListener("load", videoResize);
window.addEventListener("resize", videoResize);