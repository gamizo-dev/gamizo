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

var y = document.getElementsByClassName("report_form");
var op =0;
function toggleText(id){
  op++;
  console.log("toggleText");
  var x = document.getElementById("r"+id);
  if (x.style.display != "block") {
    y[id-1].style.display="block";
    for( i=0;i<y.length;i++){
      if(i!==id-1){
      y[i].style.display="none";
      }
    }
  }

}


function fnc(){
    if(op%2==0){
      console.log("body");
      for( i=0;i<y.length;i++){
        if(y[i].style.display="block"){
          y[i].style.display="none";
        }
      }
    }
  }

// /* When the user clicks on the button,
// toggle between hiding and showing the dropdown content */
// function myFunction() {
//   console.log("here");
//   document.getElementById("myDropdown").classList.toggle("show");
// }

// // Close the dropdown menu if the user clicks outside of it
// window.onclick = function(event) {
//   console.log("outhere");
//   if (!event.target.matches('.dropbtn')) {
//     console.log("inhere");
//     var dropdowns = document.getElementsByClassName("dropdown-content");
//     var l;
//     for (l = 0; l < dropdowns.length; l++) {
//       var openDropdown = dropdowns[l];
//       if (openDropdown.classList.contains('show')) {
//         openDropdown.classList.remove('show');
//       }
//     }
//   }
// }