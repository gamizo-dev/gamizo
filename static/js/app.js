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

// render data initially once
  console.log("page is fully loaded");
const modalElem = document.querySelector('.pg-modal');
const inputElem = document.querySelector('.pg-modal input');

const data = [
  {img: 'https://via.placeholder.com/150', title: 'nice'},
  {img: 'https://via.placeholder.com/150', title: 'Phantom Oz'},
  {img: 'https://via.placeholder.com/150', title: 'Blaze'},
  {img: 'https://via.placeholder.com/150', title: 'AriS'},
  {img: 'https://via.placeholder.com/150', title: 'Revanant'},
  {img: 'https://via.placeholder.com/150', title: 'Knshika'},
  {img: 'https://via.placeholder.com/150', title: 'Rose'},
];

// convert item object to html that we can insert
function getItemHTML(item) {
  return `
    <li tabindex="0">
      <img src="${item.img}" alt="image " />
      <span>${item.title}</span>
    </li>
  `
}

// a function to render array of items to content
function render(items) {
  console.log("RenderItems")
  const container = document.querySelector('.content > ul');
  // clean old data
  container.innerHTML = "";
  // put new items
  for (const item of items) {
    const itemHTML = getItemHTML(item);
    container.innerHTML += itemHTML;
  }
}

// listen for user's input
inputElem.addEventListener('input', (e) => {
  const value = e.target.value;
  const filtered = data.filter(item => {
    // check if user's input is inside title
    // very basic search
    const title = item.title.toLowerCase()
    return title.includes(value.toLowerCase())
  });
  // render the filtered data
  render(filtered);
});

// runs whenever user clicks a key
document.addEventListener('keydown', function(event) {
  if (event.ctrlKey && event.key === '/') {
    event.preventDefault();
    // when user clicks "ctrl + /" we toggle the modal
    modalElem.classList.toggle('open');
  } else if (event.key === 'esc') {
    event.preventDefault();
    // when user clicks "esc" we close modal
    modalElem.classList.remove('open');
  }
});
  render(data);
  console.log("belowRenderData")
