
var cursor="";

function searchPeople()
{	
	document.getElementById("brandSection").style.display="none";
	document.getElementById("searchBoxSectionContainer").style.display="block";
}

function closeTopSearchBar()
{
	document.getElementById("brandSection").style.display="block";
	document.getElementById("searchBoxSectionContainer").style.display="none";
}


function createAlbum()
{
  
	nameAlbum = document.getElementById("createAlbumName").value;
	descriptionAlbum = document.getElementById("createAlbumDescriprion").value;
	accessibilityAlbum = document.getElementById("crreatAlbumAccessibility").value;
  
	$.ajax({
       type:'POST',
      url:'/createAlbumDetails/',
      
      data:{
        name:nameAlbum,
        description:descriptionAlbum,
        accessibility:accessibilityAlbum,
      }, 
      success:function(e){
        document.getElementById("updateTextAreaId").value=e.des;

        document.getElementById("updateSelectId").value=e.access;

        console.log((e.media).length);

       
        if(e.status == "allready")
        {

          $('#myImageId1').empty();
          for(i=0;i<(e.media).length;i++)
          { 
            $('#myImageId1').append('<img src="'+e.media[i]+'" style="width:300px;height:200px;">');
          }
          
          $('#exampleModal').modal('hide'); 
          $('#exampleModalLong').modal('show'); 
          document.getElementById("exampleModalLongTitle").innerHTML = nameAlbum;
          document.getElementById("hiddenUploadTextBox").value = nameAlbum;
          document.getElementById("updateDivTextId").value=nameAlbum;
        }

        else
        {
          //$('#myGallerySelectId').append('<option>"'+nameAlbum+'"</option>');
          

          
          $('#exampleModal').modal('hide'); 
          $('#exampleModalLong').modal('show'); 
          document.getElementById("exampleModalLongTitle").innerHTML = nameAlbum;
          document.getElementById("hiddenUploadTextBox").value = nameAlbum;
          document.getElementById("updateDivTextId").value=nameAlbum;

          $("#myGallerySelectId").append('<option>'+nameAlbum+'</option>');
        }
      },
      error:function(data){
        console.log('Failed');
      }
    })

}


function readURL(input) {
  //document.getElementById("shareSubmitButton").type="submit";
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#imagePlacedID').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }

  functionality("Upload");
}

$("#albumSelectFileId").change(function() {
  readURL(this);
});

function functionality(v)
{
  
  cursorFun(v);
  if(v=="MyImage")
  {

    document.getElementById("myImageId").style.display="block";
    document.getElementById("imageUploadId").style.display="none";
    document.getElementById("settingId").style.display="none";
  }
  else if(v=="Upload")
  {
    document.getElementById("imageUploadId").style.display="block";
    document.getElementById("settingId").style.display="none";
    document.getElementById("myImageId").style.display="none";
  }
  else if(v=="Setting")
  {
    document.getElementById("settingId").style.display="block";
    document.getElementById("myImageId").style.display="none";
    document.getElementById("imageUploadId").style.display="none";
  }
}



function selectContent()
{


  v=document.getElementById("myGallerySelectId").value;


  if(v!="Select Gallery")
  { 

  document.getElementById("othersTitleHeading").textContent=v;
  $.ajax({
       type:'POST',
       url:'/createAlbumDetails/',
      
      data:{
       name:v,
      },
      success:function(e){
        
        document.getElementById("updateTextAreaId").value=e.des;

        document.getElementById("updateSelectId").value=e.access;

        
        console.log(e);
         if((e.media).length==0)
        {
          document.getElementsByClassName("no_Item")[0].style.display="block";
        }
        else
        {
          document.getElementsByClassName("no_Item")[0].style.display="none";
        }
        document.getElementById("userDefineAlbumContainerSelect").style.display="block";
        if(e.status == "allready")
        {

           $('#otherContentDivId').empty()
          for(i=0;i<(e.media).length;i++)
          { 
            $('#otherContentDivId').append('<div class="col-lg-3 col-md-4 col-sm-6 col-12 "style="border:5px solid #F5F5F5;" ><i class="fas fa-trash-alt" style="red" onclick="deletePicture(\''+e.picId[i]+'\')"></i><a href="'+e.media[i]+'" target="_blank"><img src="'+e.media[i]+'" class="img-fluid col-centered"></a></div>');
            
          }
          
        }

        
      },
      error:function(data){
        console.log('Failed');
      }
    })
}

else{
  document.getElementById("userDefineAlbumContainerSelect").style.display="none";
}

}

function Edit()
{
  nameAlbum = document.getElementById("othersTitleHeading").textContent;
  

  //

    $.ajax({
       type:'POST',
      url:'/createAlbumDetails/',
      
      data:{
        name:nameAlbum,
        
      },
      success:function(e){

        
         if((e.media).length==0)
        {
          document.getElementsByClassName("no_Item")[1].style.display="block";
        }
        else
        {
         document.getElementsByClassName("no_Item")[1].style.display="none"; 
        }
        
        if(e.status == "allready")
        {

          $('#myImageId1').empty()
          for(i=0;i<(e.media).length;i++)
          { 
            $('#myImageId1').append('<img src="'+e.media[i]+'" style="width:300px;height:200px;">');
          }
          
          $('#exampleModalLong').modal('show'); 
          document.getElementById("exampleModalLongTitle").innerHTML = nameAlbum;
          document.getElementById("hiddenUploadTextBox").value = nameAlbum;
          document.getElementById("updateDivTextId").value=nameAlbum;

          
        }

        
      },
      error:function(data){
        console.log('Failed');
      }
    })


  //
}


//Initial Tab Look
document.getElementById("deleteRepo").style.display="none";
document.getElementById("SettingEdit").style.display="none";
function openSettingTab(v)
{
  cursorFun(v);
  if(v=="SettingEdit")
  {
    document.getElementById("deleteRepo").style.display="none";
    document.getElementById(v).style.display="block";
    //document.getElementById("updateDivTextId").value=document.getElementById("exampleModalLongTitle").innerHTML;
  }
  else if(v=="deleteRepo")
  {
    document.getElementById("SettingEdit").style.display="none";
    document.getElementById(v).style.display="block";
  }
}

function deleteRepo()
{
  title=document.getElementById("exampleModalLongTitle").innerHTML;
  
  $.ajax({
       type:'POST',
       url:'/deleteAlbumRepo/',
      
      data:{
       title:title,
      },
      success:function(e){
        console.log(e);
        
        document.getElementById("snackbarContent").innerHTML="deleted";
        myFunction();
         $('#myGallerySelectId').find('[value="' + title + '"]').remove();
         $("#exampleModalLong").modal("hide");
         window.location.reload();

      },
      error:function(data){
        console.log('Failed');
      }
    })



}


function updateRepo()
{

  name=document.getElementById("updateDivTextId").value;
  description=document.getElementById("updateTextAreaId").value;
  access=document.getElementById("updateSelectId").value;

    $.ajax({
       type:'POST',
       url:'/UpdateAlbumRepo/',
      
      data:{
       name:name,
       description:description,
       accessibility:access,
      },
      success:function(e){
        console.log(e);
        document.getElementById("updateDivAlertHeding").innerHTML=e.Status;
        document.getElementById("snackbarContent").innerHTML="Updated";
        $("#exampleModalLong").modal("hide");
        myFunction();
      },
      error:function(data){
        console.log('Failed');
        document.getElementById("updateDivAlertHeding").innerHTML=e.Status;
      }
    })

}


//Delete Picture
function deletePicture(v)
{
  conf=confirm("do you really want to delete this picture,if you deleted this picture than you can not recover in future");
  if(conf){
    title=document.getElementById("myGallerySelectId").value;

    $.ajax({
         type:'POST',
         url:'/deleteAlbumPicture/',
        
        data:{
         pic:v,
         title:title,
        },
        success:function(e){
           selectContent();
        document.getElementById("snackbarContent").innerHTML="Deleted";
        myFunction();
        },
        error:function(data){
          console.log('Failed');
          
        }
      })
  }
}

function fileUpload()
{
  document.getElementById('albumSelectFileId').click();
  functionality('Upload');
}

function cursorFun(v)
{
  cursor = v;
  
  if(v=="Upload" || v=="SettingEdit" || v=="deleteRepo")
    {
      if(v=="Upload")
      {
        v1 = document.getElementById("albumSelectFileId").value;
        if(v1.length>0)
        {

         document.getElementById("saveChangesButton").value="Upload";  
         document.getElementById("saveChangesButton").style.display="block"; 
        }
      }
      else if(v=="deleteRepo")
      {
        document.getElementById("saveChangesButton").value="Update"; 
        document.getElementById("saveChangesButton").style.display="block"; 
      }
      else
        {
          document.getElementById("saveChangesButton").value="Delete";
          document.getElementById("saveChangesButton").style.display="block";
        }
    }
  else{
    document.getElementById("saveChangesButton").style.display="none";
  }
}

function Send()
{
  
  v = document.getElementById("albumSelectFileId").value;
  // alert(v);
  if(cursor=="Upload" && v.length>0)
    {
      $('#uploadFormDivId').submit();
    }
  else if(cursor=="deleteRepo")
  {
    v=confirm("Do you really want to delete this Album ?");
    if(v)
    {
      deleteRepo();
    }
  }

  else if(cursor=="SettingEdit")
  {
    updateRepo();
  }
  

}

function myFunction() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}

function formCreatValidation()
{
  name=document.getElementById("createAlbumName").value;

  if(name!="Select Gallery")
  {
    if(name.length>0)
    {
      document.getElementById("AlbumFormCreation").style.display="block";
    }
    else
    {
      document.getElementById("AlbumFormCreation").style.display="none";
    }
   }
   
   else
   {
    alert("You can not create the Gallery with this name");
    document.getElementById("createAlbumName").value="";
   } 
}






//NightMode
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
  document.getElementById("coverBackground").style.backgroundColor="black";
  document.getElementById("header").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";
  document.getElementById("header").style.backgroundColor="black";  
  document.getElementById("modalContentId").style.backgroundColor="black";
  document.getElementById("modalContentId").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";  
  document.getElementById("exampleModalLongTitle").style.color="white";
  document.getElementById("ModalFormBody").style.backgroundColor="black";
  document.getElementById("ModalFormBody").style.color="white";
  document.getElementById("ModalFormBody").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";  


}

function dayMode()
{
  
}

  autoMode();

