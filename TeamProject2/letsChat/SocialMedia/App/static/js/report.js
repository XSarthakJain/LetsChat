function reportTitle(title)
{
	document.getElementById("loadingIdDiv").style.display="block";
	document.getElementById("reportTextBox").value = title;

	postIdCol = document.getElementById("postIdCol").value;
	$.ajax({
      method:'POST',
      url:'/reportSubmission/',
      data:{
        postID : postIdCol,  
        reportTitle:title,
      },
      success:function(e){
        console.log(e);
        
        
        document.getElementById("loadingIdDiv").style.display="none";
        myFunction();
      },
      error:function(data){
        console.log('Failed');
      }
    })
}





function myFunction() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

function textBoxSubmit()
{
	var v = document.getElementById("reportTextBox").value;
	reportTitle(v);

}

function typinglimit()
{
	var v = document.getElementById("reportTextBox").value;
	if(v.length > 75 || v.length ==75)
	{
		document.getElementById("reportTextBox").value = v.slice(0,75);
		document.getElementById("reportTextBox").style.border="2px solid red";
		document.getElementById("textBoxLimitAlert").innerHTML="75/75";
	}

	else
	{
		document.getElementById("reportTextBox").style.border="2px solid grey";
		document.getElementById("textBoxLimitAlert").innerHTML=v.length+"/75";
		document.getElementById("textBoxLimitAlert").style.color="grey";
		document.getElementById("reportTextBox").value = v;		
	}
}


//Night Mode
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

  document.getElementById("wholeBody").style.backgroundColor="lightgrey";
  
  document.getElementsByClassName("modal-content")[0].style.backgroundColor="black";  
  document.getElementsByClassName("modal-content")[0].style.color='grey' ;

   
}

function dayMode()
{
  
}

  autoMode();

  