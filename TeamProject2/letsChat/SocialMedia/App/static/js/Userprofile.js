//Vertical Tab
function openAboutOpt(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent5");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks5");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}



//Tab for Photos
function openPhotosOpt(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent6");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks6");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}












$(document).ready(function() {



$(".btn-pref .btn").click(function () {
    $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
    // $(".tab").addClass("active"); // instead of this do the below 
    $(this).removeClass("btn-default").addClass("btn-primary");   
});

val1=document.getElementById("profile").innerHTML;
val2=document.getElementById("profileUser").innerHTML;
if(val1==val2){
  document.getElementById("EditProfileButton").style.display="block";
}
else{
  document.getElementById("addbtn").style.display="block";
}

});

function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}



//Edit Button
function editOpen(evt, opt) {
  var i, tabcontent, tablinks;
  
 $('#ProfileImage1').modal('hide'); 
  $('#CoverImage1').modal('hide'); 
  $('#Intro1').modal('hide'); 
  
  document.getElementById("editProfileModalTitle").innerHTML=opt;
  document.getElementById("noneOpt").style.display="block";
  document.getElementById("noneOpt").dataset.target="#"+opt+"1";

  tabcontent = document.getElementsByClassName("tabcontent1");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks1");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(opt).style.display = "block";
  evt.currentTarget.className += " active";
}

// Get the modal



//Edit Profile Picture
function edit(){
  
  document.getElementById("editProfileModalTitle").innerHTML="CoverImage";
  myProfileModal();
	document.getElementById("myModalLabel").innerHTML;
  document.getElementById("introAlertMessage").style.display="none";
	
}


	v=document.getElementById("myModalLabel").innerHTML;
	if(v=="Modal title"){
		document.getElementById("noneOpt").style.display="none";
	}
	


function request(action,user1,user2){

  // user1 == myself // user2 = friend
      
      myself = user1;     // Not in use currentlly
      userProfile = user2;
      btnvalue = action;
      
        if(btnvalue === 'add'){
            $.ajax({
            method:'POST',
            url:'/addfriend/',
            data:{
                profileId:userProfile,
                action:'add' // 1 for adding
            },
            success:function(e){
                document.getElementById('addbtn').value="Cancel Request";
                document.getElementById('addbtn').style.background="grey";

            }
        })
        }
        else if(btnvalue === 'cancel'){
            $.ajax({
            method:'POST',
            url:'/addfriend/',
            data:{
                profileId:userProfile,
                action:'cancel' // 0 for cancelling
            },
            success:function(e){
                document.getElementById('addbtn').value="Add Friend";
                document.getElementById('addbtn').style.background="grey";
            }
        })
        }
        else if(btnvalue === 'unfriend'){
          $.ajax({
          method:'POST',
          url:'/addfriend/',
          data:{
              profileId:userProfile,
              action:'unfriend' // 1 for adding
          },
          success:function(e){
              document.getElementById('addbtn').value="Add Friend";
              document.getElementById('addbtn').style.background="grey";
          }
      })
      }
      else if(btnvalue === 'confirm'){
        
        $.ajax({
        method:'POST',
        // yha pr issue hai ajax url p ni ja rha ye
        url:'/addfriend/',
        data:{
            profileId:userProfile,
            action:'confirm' // 1 for adding
        },
        success:function(e){
          // import notification;
          // notification.confirmNotification(sender,receiver,name,senderPic);

            document.getElementById('addbtn').value="Unfriend";
            document.getElementById('addbtn').style.background="grey";
        }
    })
    }
        
  }

document.getElementById("introAlertMessage").style.display="none";
    function introSubmission(){
        
                document.getElementById("IntroButt").innerHTML="Loading..";
                document.getElementById('loader').style.display = 'block';
                //document.getElementById("introLoader").classList.add("classToBeAdded");
                //element.classList.add("spinner-border spinner-border-sm");
                
                quote = document.getElementById("quote").value;
                dOB = document.getElementById("dOB").value;
                gender = document.getElementById("gender").value;
                mobileNumber = document.getElementById("mobileNumber").value;
                countryName = document.getElementById("countryName").value;
                cityName = document.getElementById("cityName").value; 
                currentEducation = document.getElementById("currentEducation").value;
                educationStartYear = document.getElementById("educationStartYear").value;
                educationEndYear = document.getElementById("educationEndYear").value;
                companyName = document.getElementById("companyName").value;
                companyPosition = document.getElementById("companyPosition").value;
                companyCity = document.getElementById("companyCity").value;
                companyDescription = document.getElementById("companyDescription").value;

        
        $.ajax({
            method:'POST',
            url:"/userIntroInsert/",
            data:{
                
                "quote":quote,
                "dOB":dOB,
                "gender":gender,
                "mobileNumber":mobileNumber,
                "countryName":countryName,
                "cityName":cityName,
                "currentEducation":currentEducation,
                "educationStartYear":educationStartYear,
                "educationEndYear":educationEndYear,
                "companyName":companyName,
                "companyPosition":companyPosition,
                "companyCity":companyCity,
                "companyDescription":companyDescription,
                
            },
            success:function(e){
                //document.getElementById()
                document.getElementById('loader').style.display = 'none';
                console.log("Success");
                document.getElementById("Intro1").style.display='none';
            document.getElementById("introAlertMessage").style.display="block";
           document.getElementById("introAlertMessage").className="alert alert-success";
           document.getElementById("introAlertMessage").innerHTML="your data has successfully updated";
           document.getElementById("IntroButt").innerHTML="Save Changes";


           document.getElementById("headerQuote").innerHTML=quote;
           document.getElementById("tableMobile").textContent=mobileNumber;
           document.getElementById("tableMobile1").textContent=mobileNumber;
           document.getElementById("tableGender").textContent=gender;
           document.getElementById("tableGender1").textContent=gender;
           document.getElementById("tableDOB").textContent=dOB;
           document.getElementById("tableDOB1").textContent=dOB;
           document.getElementById("tableQuote").textContent=quote;
           document.getElementById("tableCountryName").textContent=countryName;
           document.getElementById("tableCountryName1").textContent=countryName;
           document.getElementById("tableCityName").textContent=cityName;
           document.getElementById("tableCityName1").textContent=cityName;
           document.getElementById("tablecurrentEducation").textContent=currentEducation;
           document.getElementById("tableEducationStartYear").textContent=educationStartYear;
           document.getElementById("tableEducationStartYear1").textContent=educationStartYear;
           document.getElementById("tableEducationEndYear").textContent=educationEndYear;
           document.getElementById("tableEducationEndYear1").textContent=educationEndYear;

           document.getElementById("tableCompanyName").textContent=companyName;
           document.getElementById("tableCompanyPosition").textContent=companyPosition;
           document.getElementById("tableCompanyCity").textContent=companyCity;
           document.getElementById("tableCompanyDescription").textContent=companyDescription;
           document.getElementById("tableCompanyName1").textContent=companyName;
           document.getElementById("tableCompanyPosition1").textContent=companyPosition;
           document.getElementById("tableCompanyCity1").textContent=companyCity;
           document.getElementById("tableCompanyDescription1").textContent=companyDescription;
           

           
            },
            error:function(e){
                console.log('Fail');
                document.getElementById("introAlertMessage").style.display="block";
                document.getElementById("introAlertMessage").className="alert alert-primary";
                document.getElementById("introAlertMessage").innerHTML="your data has not Updated";
           
            }

        })
    }
    document.getElementById('loader').style.display = 'none';
   


    //Friends

function tagPeopleFun1(ID)
{
  
  document.getElementById("tagLoader").style.display="block";
  $.ajax({
      method:'POST',
      url:'/taggedSearchFriends/',
      data:{
        id:ID,
        action:'friend'
      },
      success:function(e){
        
        $('#friendsListId').empty();
        console.log(e);
        document.getElementById("tagLoader").style.display="none";
        for(i=0;i<(e.name).length;i++)
        {
         $('#friendsListId').append('<a href="/profile/'+e.userId[i]+'"><label style="color:rgba(0,150,136,0.8);"><span style="color:rgba(0,150,136,0.8);"><img src="'+e.pic[i]+'" style="width:55px;height:55px;border-radius:50%;padding:5px;border:2px solid rgba(0,150,136,0.8);margin:8px;"></span>'+e.name[i]+'</label></a><br>');
        }

      },
      error:function(data){
        console.log('Failed');
      }
    })

}


function showPhotos(val)
{
 
  $.ajax({
    method:'POST',
    url:'/showPhotosfun/',
    data:{
      id:val,
      
    },
    success:function(e){
      
      // $('#friendsListId').empty();
      // console.log(e);
      // document.getElementById("tagLoader").style.display="none";
      // for(i=0;i<(e.name).length;i++)
      // {
      //  $('#friendsListId').append('<a href="/profile/'+e.userId[i]+'"><label ><span><img src="'+e.pic[i]+'" style="width:45px;height:45px;border-radius:50%;margin:8px;"></span>'+e.name[i]+'</label></a><br>');
      // }

    },
    error:function(data){
      console.log('Failed');
    }
  })


}

function profilePicFunction(name)
{
  
    $.ajax({
    method:'POST',
    url:'/showProfilePicfun/',
    data:{
      name:name,
      
    },
    success:function(e){
      
      console.log(e);
      if(e.status)
      {
        $("#profilePicImageId").empty();
        for(i=0;i<(e.profileData).length;i++)
        {
          $("#profilePicImageId").append('<div class="col-lg-3 col-md-4 col-sm-6 col-12" style="border:5px solid #F5F5F5;"><a href="'+e.profileData[i]+'" target="_blank"><img src="'+e.profileData[i]+'" class="img-fluid col-centered"></a></div>');
        }
      }

    },
    error:function(data){
      console.log('Failed');
    }
  })
  
}

function coverPicFunction(name)
{
  
    $.ajax({
    method:'POST',
    url:'/showCoverPicfun/',
    data:{
      name:name,
      
    },
    success:function(e){
      
      console.log(e);
      if(e.status)
      {
        $("#coverPicImageId").empty();
        for(i=0;i<(e.coverData).length;i++)
        {
          $("#coverPicImageId").append('<div class="col-lg-3 col-md-4 col-sm-6 col-12" style="border:5px solid #F5F5F5;"><a href="'+e.coverData[i]+'" target="_blank"><img src="'+e.coverData[i]+'" class="img-fluid col-centered"></a></div>');
        }
      }

    },
    error:function(data){
      console.log('Failed');
    }
  })
}

function postPicFunction(name)
{
  
    $.ajax({
    method:'POST',
    url:'/showPostPicfun/',
    data:{
      name:name,
      
    },
    success:function(e){
      
      console.log(e);
      if(e.status)
      {
        $("#postPicImageId").empty();
        for(i=0;i<(e.postData).length;i++)
        {
          $("#postPicImageId").append('<div class="col-lg-3 col-md-4 col-sm-6 col-12" style="border:5px solid #F5F5F5;"><a href="/showPost/'+e.postId[i]+'" target="_blank"><img src="'+e.postData[i]+'" class="img-fluid col-centered"></a></div>');
        }
      }

    },
    error:function(data){
      console.log('Failed');
    }
  })
}

function otherPicFunction(name)
{
  

//$("#bd-example-modal-sm").modal("show");

  $("#bd-example-modal-sm").appendTo("body");

  $('#bd-example-modal-sm').modal('show'); 
    $.ajax({
    method:'POST',
    url:'/showOtherPicfun/',
    data:{
      name:name,
      
    },
    success:function(e){
      
      console.log(e);
      
        console.log(e);
        $("#otherAlbumCount").empty();
        for(i=0;i<(e.directory).length;i++)
        {
          $("#otherAlbumCount").append('<span style="margin:12px;"><p style="" class="reponameId" onclick="selectedDirectoryName(\''+e.directory[i]+'\',\''+name+'\')">'+e.directory[i]+'</p></span>');

        }
      

    },
    error:function(data){
      console.log('Failed');
    }
  })
}

function selectedDirectoryName(v,v1)
{

  
    $.ajax({
    method:'POST',
    url:'/showSelectOptionPic/',
    data:{
      name:v1,
      username:v,
      
    },
    success:function(e){
      
      console.log(e);
      if(e.status)
      {
        $('#bd-example-modal-sm').modal('hide'); 
        $("#showSelectOptionPicId").empty();
        for(i=0;i<(e.albumPicUrl).length;i++)
        {
          $("#showSelectOptionPicId").append('<div class="col-lg-3 col-md-4 col-sm-6 col-12" style="border:5px solid #F5F5F5;"><a href="'+e.albumPicUrl[i]+'" target="_blank"><img src="'+e.albumPicUrl[i]+'" class="img-fluid col-centered"></a></div>');

        }
        $("#bd-example-modal-sm").appendTo("body");
        $('#bd-example-modal-sm').modal('hide'); 
      }

    },
    error:function(data){
      console.log('Failed');
    }
  })

}


function editProfileFunction()
{

// $('#ProfileImage1').modal('hide'); 
//   $('#CoverImage1').modal('hide'); 
//   $('#Intro1').modal('hide');
 
$("#myModal").modal("show");

 $("#myModal").appendTo("body");
}


//$("#Timeline").appendTo("body");


$( document ).ready(function() {
    console.log( "ready!" );
    $(".welcomeModal").appendTo("body");

    $('.welcomeModal').modal('show'); 
    $('.welcomeModal').modal('hide'); 

});

function myProfileModal()
{
  $('#ProfileImage1').modal('hide'); 
  $('#CoverImage1').modal('hide'); 
  $('#Intro1').modal('hide'); 
  $("#myModal").modal("hide");
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

  document.getElementById("wholeBody").style.backgroundColor="black";
  document.getElementById("wrapperJumbotron").style.backgroundColor="black";

  document.getElementById("headerName").style.color="rgba(0,150,136,0.8)";
  document.getElementById("headerQuote").style.color="rgba(0,150,136,0.8)";

  // document.getElementsByClassName("myPostClass").style.backgroundColor="black";

  document.getElementById("Timeline").style.color="grey";
  var items = document.getElementsByClassName("myPostClass");
  for (var i=0; i < items.length; i++) {
    items[i].style.backgroundColor="black";
    items[i].style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";  
    items[i].style.borderBottom="2px solid rgba(0, 150, 136, 1)";
    // items[i].style.-moz-box-shadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";  
    // items[i].style.-webkit-box-shadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";  

    document.getElementsByClassName("commentHereClass")[i].style.backgroundColor="black";
    document.getElementsByClassName("material-icons")[i].style.color="rgba(0,150,136,0.8)";
  }


  var items =document.getElementsByClassName("modalContentClass");
  for (var i=0; i < items.length; i++) {
    items[i].style.backgroundColor="black";
    items[i].style.color="rgba(0,150,136,0.8)";
    items[i].style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";  
    
  }



  
  

}

function dayMode()
{
  
}

  autoMode();

  