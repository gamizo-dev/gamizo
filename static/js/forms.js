//report form
var td= document.getElementsByClassName("more");
var cancel= document.getElementsByClassName("cancel");
var closebtn= document.getElementsByClassName("closebtn");
var report = document.getElementById("reportfrm")
var share = document.getElementById("sharefrm")
var j=0;
function ShowReportfrm() {
    console.log(j);
    if(report.style.display = "none"){
      // console.log(content.style.display);
      report.style.display = "block";
    j=1;
    }
}
function HideReportfrm(){
    if(j!==1){
        if(report.style.display="block"){
            report.style.display="none";
        }
    }
    j=0;
}
