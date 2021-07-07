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

// window.onload = () => {
//   new Vue({
//     el: "#app",
//     data() {
//       return {
//         sortBy: "age",
//         sortDesc: false,
//         fields: [
          
//           { key: "first_name", sortable: true },
//           { key: "age", sortable: true },
//           { key: "isActive", sortable: false }
//         ],
//         items: [
//           {
//             isActive: true,
//             age: 40,
//             first_name: "Dickerson",
//             last_name: "Macdonald"
//           },
//           { isActive: false, age: 21, first_name: "Larsen", last_name: "Shaw" },
//           {
//             isActive: false,
//             age: 89,
//             first_name: "Geneva",
//             last_name: "Wilson"
//           },
//           { isActive: true, age: 38, first_name: "Jami", last_name: "Carney" }
//         ]
//       };
//     }
//   });
// };

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