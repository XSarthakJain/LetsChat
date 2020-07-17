function getCookie(){
  var nameEQ = "Mode" + "=";
      var ca = document.cookie.split(';');
      for(var i=0;i < ca.length;i++) {
          var c = ca[i];
          while (c.charAt(0)==' ') c = c.substring(1,c.length);
          if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length,c.length)
            
          }
      }
  
  }    


  function autoMode(){
    v=getCookie();
     
      if(v=="darkMode"){
        
        nightMode(); 
      }
      
      else{
        
        dayMode();
      }
     
  }  
      
function nightMode()  
{        
  
  document.getElementById("header").style.backgroundColor="black";  
  document.getElementById("header").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";

  document.getElementById("wholeBody").style.backgroundColor="black";
  document.getElementById("footerDiv").style.backgroundColor="black";
  document.getElementById("footerDiv").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";
  document.getElementById("finalFooter").style.backgroundColor="black";

  document.getElementById("personPic").style.backgroundColor="black";
  document.getElementsByClassName("personContaints")[0].style.color="grey";
  document.getElementsByClassName("personContaints")[1].style.color="grey";
  document.getElementsByClassName("personContaints")[2].style.color="grey";



   
}

function dayMode()  
{
  
}

  autoMode();

  