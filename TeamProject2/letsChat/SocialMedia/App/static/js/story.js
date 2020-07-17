//Global Values   
var txt=false,colorValue="grey",fS="none",fF="none";

//Change story text Background
function colorPickerValue(v)
{ 
  document.getElementById("storySectionArea").style.background=v;
  colorValue=v;
}

function storyTextFieldArea()
{
 var v=document.getElementById("storyTextFieldArea").value;
 console.log(v);
 document.getElementById("storyPrintSectionArea").innerHTML=v;
 txt=v;
}

//For Mobile Screen TextArea
function storyTextFieldArea2()
{
 var v=document.getElementById("mobileScreenTextArea").value;
 console.log(v);
 document.getElementById("storyPrintSectionArea").innerHTML=v;
 txt=v;
}

function fontSizeValue()
{
  v=document.getElementById("fontSizeValueDiv").value;
  document.getElementById("storyPrintSectionArea").style.fontSize=v;
  fS = v;
}

//For Mobile Screen
function fontSizeValue1(v)
{
	document.getElementById("storyPrintSectionArea").style.fontSize=v;
	fS = v;
}

function fontFamilyValue()
{
 v=document.getElementById("fontFamilyValueSelect").value;
 document.getElementById("storyPrintSectionArea").style.fontFamily=v; 
 fF=v;
}

//For Mobile Screen
function fontFamilyValue1(v)
{
 document.getElementById("storyPrintSectionArea").style.fontFamily=v; 
 fF = v;
}

function colorPickerValue1()
{
		var v=document.getElementById("colorChooseList").value;
		document.getElementById("storySectionArea").style.background=v;
		colorValue = v;
}

function colorPickerValue2()
{
		var v=document.getElementById("colorChooseList2").value;
		document.getElementById("storySectionArea").style.background=v;
		colorValue = v;
}

//Share
function share(sendValue)
{	
	var images ="";
	var fontSize="";
	if(sendValue == "text")
	{
		v = document.getElementById("storyTextFieldArea").value
		v1 = document.getElementById("mobileScreenTextArea").value;
		
		if(v.length == 0 && v1.length == 0)
		{	$('alert').show();
			document.getElementById("alertBar").style.display="block";

		}

		else
		{
			if(v.length == 0)
				v=v1;
			
			//alert(colorValue);
			/*alert(fS);
			alert(fF);*/
			sendValuePortion();
			
			
		}
	}

	

	function sendValuePortion()
	{
        console.log('here')
	$.ajax({
      type: 'POST',
      url:'/storySubmissionForm/',
      data:{
        type:sendValue,
        fontSize:fS,
        fontFamily:fF,
        Caption:v,
        color:colorValue,
        image:images,
        // contentType: false,
        // processData: false,
      },
      success:function(e){
        console.log(e);

        {
		  // Get the snackbar DIV
		  var x = document.getElementById("snackbar");

		  // Add the "show" class to DIV
		  x.className = "show";

		  // After 3 seconds, remove the show class from DIV
		  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
		}
        
        
      },
      error:function(data){
        console.log('Failed');
      }
    })
}
		
	
}



function readURL(input) {
	document.getElementById("shareSubmitButton").type="submit";
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#imagePlace').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#imagePicker").change(function() {
  readURL(this);
});


//Image Upload Section 

//Write Caption
var maxCharCountVar;
function storyImageTextFieldAreaPlace()
{
	
	var v=document.getElementById("storyImageTextFieldArea").value;
 	var v1=document.getElementById("mobileScreenTextArea").value;
 	if(v.length<1)
 	{	
 		v=v1;
 	}
 		
 	if(v.length<=100){
    if(v.length>100)
      {alert("Higher Value");}
 		document.getElementById("imageCaption").innerHTML=v;
 		document.getElementById("numberOfWordIndicator").textContent=v.length+"/100";
 		maxCharCountVar = v;
    document.getElementById("numberOfWordIndicator1").textContent=v.length+"/100";
    maxCharCountVar = v;
 		document.getElementById("captionInput").value=v;
    document.getElementById("numberOfWordIndicator").style.color="grey";
    document.getElementById("numberOfWordIndicator1").style.color="grey";

 	}
 	else{
 		document.getElementById("numberOfWordIndicator").textContent="you can not insert more than 100 words";
 		document.getElementById("numberOfWordIndicator").style.color="red";
    document.getElementById("numberOfWordIndicator1").textContent="you can not insert more than 100 words";
    document.getElementById("numberOfWordIndicator1").style.color="red";

    


}  

if( v1.length < 1)
    {
      document.getElementById("storyImageTextFieldArea").value=v.slice(0,100);
    }
    else
    {
      document.getElementById("mobileScreenTextArea").value=v.slice(0,100);  
    }
    


}

//Font Family
function imagefontFamilyValue()
{
 v=document.getElementById("imagefontFamilyValueSelect").value;
 document.getElementById("imageCaption").style.fontFamily=v; 
 document.getElementById("fontFamilyInput").value=v;
}

//Color
function captioncolorPickerValue(v)
{
	document.getElementById("imageCaption").style.color=v; 	
	document.getElementById("colorInput").value=v;
}

function captioncolorPickerValue1()
{
	var v = document.getElementById("captioncolorPickerValueId").value;
	document.getElementById("imageCaption").style.color=v; 	
	
	document.getElementById("colorInput").value=v;
}



//Font Family for Image Story for Mobile Device
function fontFamilyValue2(v)
{
	document.getElementById("imageCaption").style.fontFamily=v;
	document.getElementById("fontFamilyInput").value=v;
}

function colorPickerValue4(v)
{
	document.getElementById("imageCaption").style.color=v;
	document.getElementById("colorInput").value=v;
}

$('#fileup').click(function() {
   $('#files').click();
});



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
  document.getElementsByClassName("rightSideDiv")[0].style.backgroundColor="lightgrey";
  document.getElementById("leftDivSect").style.borderRight="1px solid grey";
  


   
}

function dayMode()
{
  
}

  autoMode();




//Text Upload Section 

//Write Caption
var maxCharTextCountVar;
function storyTextFieldAreaPlace()
{
  
  var v=document.getElementById("storyTextFieldArea").value;
  var v1=document.getElementById("mobileScreenTextArea").value;
  if(v.length<1)
  { 
    v=v1;
  }
    
  if(v.length<=100){
    // document.getElementById("storyTextFieldArea").value=v;
    // document.getElementById("mobileScreenTextArea").value=v;
    document.getElementById("numberOfWordIndicator").textContent=v.length+"/100";
    document.getElementById("numberOfWordIndicator1").textContent=v.length+"/100";
    maxCharTextCountVar = v;
    
    
  } 
  else{
    document.getElementById("numberOfWordIndicator").textContent="you can not insert more than 100 words";
    document.getElementById("numberOfWordIndicator").style.color="red";
    document.getElementById("numberOfWordIndicator1").textContent="you can not insert more than 100 words";
    document.getElementById("numberOfWordIndicator1").style.color="red";
    
    
    
  }

  if(v1.length<1)
  {
    storyTextFieldArea();
    document.getElementById("storyTextFieldArea").value=v.slice(0,100);
  }
  else{
    storyTextFieldArea2();
    document.getElementById("mobileScreenTextArea").value=v.slice(0,100);
  }
}
  