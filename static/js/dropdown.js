console.log("page is fully loaded");
const modalElem = document.querySelector('.pg-modal');
const inputElem = document.querySelector('.pg-modal input');
const data = [

];
var category = document.getElementsByClassName("categorisedClass");
for(i=0;i<category.length;i++){
  data.push({link:category[i], title: category[i].textContent});
}
// convert item object to html that we can insert
function getItemHTML(item) {
  return `
  <a href=${item.link}>
    <li tabindex="0">
            <span>${item.title}</span>
    </li>
    </a>
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
  console.log("belowRenderData");

  const content = document.querySelector('.content');
  const cardshift = document.getElementsByClassName('.cards');
  //Show content of dropdown on click
  function ShowContent(){
    if(content.style.display ="none"){
        content.style.display ="block";
        cardshift.classList.add("shift");
    }
    else{
      content.style.display="none";
      cardshift.classList.remove("shift");
    }
    console.log(content.style.display);
    console.log(cardshift.classList);
  }
