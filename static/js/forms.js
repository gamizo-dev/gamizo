//report form
var td= document.getElementsByClassName("more");
var cancel= document.getElementsByClassName("cancel");
var closebtn= document.getElementsByClassName("closebtn");
var report = document.getElementById("reportfrm");
var share = document.getElementById("sharefrm");
var sharebtn = document.getElementsByClassName("share");
var j=0;
function ShowReportfrm(id, cat) {
    console.log(j);
    gamename=id;
    category=cat;
    if(report.style.display = "none"){
      report.style.display = "block";
    j=1;
    }
    document.getElementById('repname').value=gamename;
    document.getElementById('repname2').value=category;

}
function HideReportfrm(){
    if(j!==1){
        if(report.style.display="block"){
            report.style.display="none";
        }
    }
    j=0;
}
cancel.addEventListener("click", function(event){
    event.preventDefault()
  });

function ShowSharefrm(id, cat) {
    console.log(j);
    gamename=id;
    category=cat;
    if(share.style.display = "none"){
      share.style.display = "block";
    j=1;
    }
    document.getElementById('repname').value=gamename;
    document.getElementById('repname2').value=category;

}
function HideSharefrm(){
    if(j!==1){
        if(report.style.display="block"){
            report.style.display="none";
        }
    }
    j=0;
}