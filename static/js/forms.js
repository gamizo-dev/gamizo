//report form
var td= document.getElementsByClassName("more");
var cancel= document.getElementsByClassName("cancel");
var closebtn= document.getElementsByClassName("closebtn");
var report = document.getElementById("reportfrm")
var share = document.getElementById("sharefrm")
var j=0;
function ShowReportfrm(id) {
    console.log(j);
    gamename=id;
    if(report.style.display = "none"){
      // console.log(content.style.display);
      report.style.display = "block";
    j=1;
    }
    document.getElementById('repname').value=gamename;
    console.log(gamename);
    rp=document.getElementById('repname')
    console.log(rp);
}
function HideReportfrm(){
    if(j!==1){
        if(report.style.display="block"){
            report.style.display="none";
        }
    }
    j=0;
}
