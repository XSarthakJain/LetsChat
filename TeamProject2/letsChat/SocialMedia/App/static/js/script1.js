  //All Deshboard Contents
//Post Alert Close

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
        document.getElementById("modeId").innerHTML="day Mode";
        nightMode(); 
      }
  
      else{
        document.getElementById("modeId").innerHTML="Night Mode";
        dayMode();
      }
  
  }
  
  autoMode();
  
  
  function visibleButton(){
    
    status=document.getElementById("TextPost").value;
    
    if(status!=""){
      document.getElementById("SubmitPost").style.display="block";
    }
    else{
      document.getElementById("SubmitPost").style.display="none";
    }
  
  }
  
  
  function openSearch() {
    document.getElementById("myOverlay").style.display = "block";
    
  }
  
  function closeSearch() {
    document.getElementById("myOverlay").style.display = "none";
  }
  
  
  //LogOut Section
  function openLogOut() {
    document.getElementById("myOverlayLogOut").style.display = "block";
    }
    
    function closeLogOut() {
    document.getElementById("myOverlayLogOut").style.display = "none";
    }
    
  
    function Mode(){
  
        var v=document.getElementById("modeId").innerHTML;
         
        if(v=="Night Mode"){
          nightMode();
          document.getElementById("modeId").innerHTML="day Mode";
        }
  
        else{
          dayMode();
          document.getElementById("modeId").innerHTML="Night Mode";
        }
  
  
    }
  
  
  
   
    //   $(document).ready(function () {
  
    //       // ANIMATEDLY DISPLAY THE NOTIFICATION COUNTER.
    //       // $('#noti_Counter')
    //       //     .css({ opacity: 0 })
    //       //     .text('7')  // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
    //       //     .css({ top: '-10px' })
    //       //     .animate({ top: '-2px', opacity: 1 }, 500);
  
    //       // $('#noti_Button').click(function () {
  
    //       //     // TOGGLE (SHOW OR HIDE) NOTIFICATION WINDOW.
    //       //     $('#notifications').fadeToggle('fast', 'linear', function () {
    //       //         if ($('#notifications').is(':hidden')) {
    //       //             $('#noti_Button').css('background-color', '#2E467C');
    //       //         }
    //       //         // CHANGE BACKGROUND COLOR OF THE BUTTON.
    //       //         else $('#noti_Button').css('background-color', '#FFF');
    //       //     });
  
    //       //     $('#noti_Counter').fadeOut('slow');     // HIDE THE COUNTER.
  
    //       //     return false;
    //       // });
  
    //       // // HIDE NOTIFICATIONS WHEN CLICKED ANYWHERE ON THE PAGE.
    //       // $(document).click(function () {
    //       //     $('#notifications').hide();
  
    //       //     // CHECK IF NOTIFICATION COUNTER IS HIDDEN.
    //       //     if ($('#noti_Counter').is(':hidden')) {
    //       //         // CHANGE BACKGROUND COLOR OF THE BUTTON.
    //       //         $('#noti_Button').css('background-color', '#2E467C');
    //       //     }
    //       // });
  
    //       $('#notifications').click(function () {
    //           return false;       // DO NOTHING WHEN CONTAINER IS CLICKED.
    //       });
    // });
  
  //Validation for Post Image
  $("#file1").on("change", function(e) {
  
    console.log(this.files[0].type);
    document.getElementById("SubmitPost").style.display="block";
    
    
    })
    
  
  
  function emojiCreater(){
      $("#TextPost").emojioneArea({
              pickerPosition: "bottom",
              tonesStyle: "bullet",
              
      });
      
  document.getElementById("SubmitPost").style.display="block";
  
    }
    
    // function likePost(data){
      
    //   Id = data
      
    //   $.ajax({
    //     method:'POST',
    //     url:'/postlike/',
    //     data:{
    //       postID : Id
    //     },
    //     success:function(e){
    //       likeCount = e['Result']
          
    //       document.getElementsByName(Id)[0].style.color=e['color'];
    //       document.getElementById(Id).innerHTML=likeCount+" Likes";
    //     },
    //     error:function(data){
    //       console.log('Failed');
    //     }
    //   })
    // }
  
  
  
  //Automatically Check Like Request
  // setInterval(function()
  // {
  // $.ajax({
  //       method:'POST',
  //       url:'/automaticallylike/',
        
  //       success:function(e){
          
          
  //         for(i=0;i<((e.like).length);i++){
            
  //           document.getElementById(e.userData[i]).innerHTML=e.like[i]+" Likes";
  //         }
  //       },
  //       error:function(data){
  //         console.log('Failed');
  //       }
  //     });
  // }, 5000); 
  
  
  //Story Slider
  $(document).ready(function() {
      $('#autoWidth').lightSlider({
          autoWidth:true,
          loop:false,
          controls:true,
          onSliderLoad: function() {
              $('#autoWidth').removeClass('cS-hidden');
  
          } 
      });  
  
    });
  
  
  
  function emojiCreater(){
      $("#TextPost").emojioneArea({
              pickerPosition: "bottom",
              tonesStyle: "bullet",
              
      });
      
  document.getElementById("SubmitPost").style.display="block";
  
  
    }
    
    // function likePost(data){
      
    //   Id = data
      
    //   $.ajax({
    //     method:'POST',
    //     url:'/postlike/',
    //     data:{
    //       postID : Id
    //     },
    //     success:function(e){
    //       likeCount = e['Result']
          
    //       document.getElementsByName(Id)[0].style.color=e['color'];
    //       document.getElementById(Id).innerHTML=likeCount+" Likes";
    //     },
    //     error:function(data){
    //       console.log('Failed');
    //     }
    //   })
    // }
  
  
  
  //Automatically Check Like Request
  // setInterval(function()
  // {
  // $.ajax({
  //       method:'POST',
  //       url:'/automaticallylike/',
        
  //       success:function(e){
          
          
  //         for(i=0;i<((e.like).length);i++){
            
  //           document.getElementById(e.userData[i]).innerHTML=e.like[i]+" Likes";
  //         }
  //       },
  //       error:function(data){
  //         console.log('Failed');
  //       }
  //     });
  // }, 5000); 
  
  
  
  //Set Image on input type =File
      $( "#FileInput" ).change(function() {
        $( "#Up" ).click();
      });
  
  
  //
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
  
  
  
  function nightMode(){
    //alert("Okkk");
  
      document.cookie = "Mode=darkMode";
      document.getElementById("body").style.background="grey";
      document.getElementById("header").style.background="black";
      document.getElementById("header").style.color="rgba(0, 150, 136, 1)";
      document.getElementById("header").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";
      document.getElementById("leftFixDiv").style.background="black";
  
      document.getElementById("profilePicImage").style.border="2px solid rgba(0, 150, 136, 1)";
      document.getElementsByClassName("maquee_text")[0].style.color="rgba(0, 150, 136, 1)";
  
      var y = document.getElementsByClassName("icon");
      var z = document.getElementsByClassName("title");
      for (i = 0; i < y.length; i++) {
      y[i].style.color="rgba(0, 150, 136, 1)";
      
    }
  
    for (i = 0; i < z.length; i++) {
      z[i].style.color="rgba(0, 150, 136, 1)";
    }
      document.getElementById("profileInsideHR").style.background = "rgba(0, 150, 136, 1)";
      document.getElementById("accountRightSectionPlaceModel").style.background = "black";
  
  



  var items=document.getElementsByClassName("modal-content");
    for(i=0;i<items.length;i++)
    {
      items[i].style.backgroundColor="#1e272c";  
      
      items[i].style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";
    }

    document.getElementById("notifications").style.backgroundColor="black";
    document.getElementById("noti_heading").style.backgroundColor="black";
    document.getElementById("seeAll").style.backgroundColor="black";

    document.getElementById("wrapperstorySectionId").style.backgroundColor="rgba(191, 191, 191, 0.5)";
    document.getElementById("wrapperstorySectionId").style.color="white";


   }  
  
  
  function dayMode(){
  
      document.cookie = "Mode=dayMode";
      var element = document.body;
      element.classList.toggle("day-mode");
      document.getElementById("body").style.background="white";
      document.getElementById("header").style.background="#E9ECEF";
      document.getElementById("header").style.color="rgba(0, 150, 136, 1)";
      document.getElementById("header").style.boxShadow="0px 0px 23px 0px rgba(0,0,0,0.5)";
      document.getElementById("leftFixDiv").style.background="rgba(0, 150, 136, 0.6)";
  
      document.getElementById("profilePicImage").style.border="2px solid white";
      document.getElementsByClassName("maquee_text")[0].style.color="white";
  
      var y = document.getElementsByClassName("icon");
      var z = document.getElementsByClassName("title");
      for (i = 0; i < y.length; i++) {
      y[i].style.color="white";
      
    }
  
    for (i = 0; i < z.length; i++) {
      z[i].style.color="white";
    }
      document.getElementById("profileInsideHR").style.background="white";
     
       document.getElementById("body").style.backgroundImage="url(static/images/body-light.jpg)";
      document.getElementById("accountRightSectionPlaceModel").style.background = "white";
      /*document.getElementById("PostAlert").style.background="rgba(191, 191, 191, 0.5)";
      document.getElementById("PostAlert").style.color="black";
      document.getElementById("searchBtnId").style.background="white";
      document.getElementById("searchBtnId").style.border="1px solid white";
      var bt=document.getElementById("searchBtnSubmitId") 
      bt.style.background="white";
      bt.style.border="1px solid white";
      bt.style.color="black";
      */

    var items=document.getElementsByClassName("modal-content");
    for(i=0;i<items.length;i++)
    {
      items[i].style.backgroundColor="#fff";
      
      items[i].style.boxShadow="none";
    }

    document.getElementById("notifications").style.backgroundColor="#fff";
    document.getElementById("noti_heading").style.backgroundColor="#fff";
    document.getElementById("seeAll").style.backgroundColor="#fff";

    document.getElementById("storySessionModalContent").style.backgroundColor="rgba(191, 191, 191, 0.5)";
    document.getElementById("storySessionModalContent").style.color="white";





   }
  
   function storySetPlace(v,v1,v2,v3,v4,v5)
   {
    
    document.getElementById("storyTextContent").innerHTML=v;
    document.getElementById("storyTextContent").style.color=v4;
    document.getElementById("storyTextContent").style.fontFamily=v5;
    document.getElementById("storyVisiblePersonName").innerHTML=v1;
    document.getElementsByClassName("storyProfileSection")[0].src=v2;
    document.getElementById("VisibleStoryBodySection").style.backgroundImage="url("+v3+")";
  
   }
  
   //
   function storyTextSetPlace(color,textContent,size,family,name,pic)
   {
      
      document.getElementById("VisibleStoryTextBodySection").style.backgroundColor = color;
      document.getElementById("textStoryTextContent").style.fontFamily=family;
      document.getElementById("textStoryTextContent").innerHTML=textContent;
      document.getElementById("textStoryTextContent").style.fontSize=size;
      document.getElementsByClassName("storyProfileSection")[1].src=pic;
      document.getElementById('textStoryVisiblePersonName').innerHTML=name;
   }
  
   //Post Result by Internet
   function liveSearchPostResult(result)
   {
  
    document.getElementById("searchPostResultModel").src="https://www.bing.com/search?q="+result;
    if(result.length>25)
      {
        document.getElementById("PostResultSearchModel").innerHTML="Search : "+result.slice(0,25)+"...";
      }
    else 
    {
       document.getElementById("PostResultSearchModel").innerHTML="Search : "+result;
    }
   }
  
  //Tag People Function1
  var postIdGlobal="";
  var taggedWholeFriendList;
  function tagPeopleFun1(pid)
  {
    postIdGlobal=pid;  
    document.getElementById("tagLoader").style.display="block";
    $.ajax({
        method:'POST',
        url:'/taggedSearchFriends/',
        data:{
          postId:pid,
        },
        success:function(e){
          $("#selectedPeople").empty();

          console.log(e.allName);
          seperator="";
          taggedWholeFriendList = e;
          $('#tagPeoplenameArea').empty();
          console.log(e);
          document.getElementById("tagLoader").style.display="none";
          for(i=0;i<(e.name).length;i++)
          {
           $('#tagPeoplenameArea').append('<span id="'+e.userId[i]+'"  onclick="tagging(\''+e.userId[i]+ '\',\''+e.name[i]+ '\')" ><label for="'+e.userId[i]+'"><span><img src="'+e.pic[i]+'" style="width:45px;height:45px;border-radius:50%;margin:8px;"></span>'+e.name[i]+'</label></span><br>');


           
          }
          for(i=0;i<(e.allTaggedList).length;i++){

            seperator=seperator+","+e.allTaggedList[i];
            
           

            $("#selectedPeople").append('<span class="badge badge-primary" id="Badge'+e.allTaggedList[i]+'">'+e.allTaggedList[i]+'<button type="button" class="close" aria-label="Dismiss"  ><span aria-hidden="true" onclick="closeBadge(\''+e.allTaggedList[i]+'\')">&times;</span></button></span>');
          }
  
        },
        error:function(data){
          console.log('Failed');
        }
      })
  
  }
  
  function storyTextSetPlaceManager(media,storydate,storyType,family,size,textContent,color,lenCaption,name,pic)
   {
  
      $("#storySlidesId").empty();
      console.log("media = "+media);
      console.log("storydate = "+storydate);
      console.log("storyType = "+storyType);
      console.log("family = "+family);
      console.log("size = "+size);
      console.log("textContent = "+textContent);
      console.log("color"+color);
      var storyTypeLocal = storyType.split("@");
      var familyLocal = family.split("@");
      var sizeLocal = size.split("@");
      var colorLocal = color.split("@");
      var mediaLocal = media.split("@");
      var lenCaptionLocal = lenCaption.split("@");
  
      var startLen = 0;
    for(var i=0 ; i< (storyTypeLocal.length)-1; i++) {
      console.log("startLen ",startLen);
      
      console.log(textContent.slice(startLen,lenCaptionLocal[i]));
  
      if(storyTypeLocal[i] == "image")
      { 
        if(i==0){
          $("#storySlidesId").append('<div class="carousel-item active" ><center><div id="VisibleStoryBodySection"><img src="'+mediaLocal[i]+'" style="width:100%;height:70vh;" alt="..."><h5 id="storyTextContent" style="color:'+colorLocal[i]+';font-family:'+familyLocal[i]+';white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">'+textContent.slice(startLen,lenCaptionLocal[i])+'</h5></div></center></div>');
        }
  
        else{
        $("#storySlidesId").append('<div class="carousel-item" ><center><div id="VisibleStoryBodySection"><img src="'+mediaLocal[i]+'" style="width:100%;height:70vh;" alt="..."><h5 id="storyTextContent" style="color:'+colorLocal[i]+';font-family:'+familyLocal[i]+';white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">'+textContent.slice(startLen,parseInt(lenCaptionLocal[i])+startLen)+'</h5></div></center></div>');
        }
      }
      else{  
  
        if(i==0){
          $("#storySlidesId").append('<div class="carousel-item active" ><center><div style="width:100%;height:70vh;padding:2%;background:'+colorLocal[i]+';display: flex;justify-content: center;align-items: center;" ><p style="font-family:'+familyLocal[i]+';font-size:'+sizeLocal[i]+';white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">'+textContent.slice(startLen,lenCaptionLocal[i])+'</p></div></center></div>');
        }
  
        else{
        $("#storySlidesId").append('<div class="carousel-item" ><center><div style="width:100%;height:70vh;padding:2%;background:'+colorLocal[i]+'; display: flex;justify-content: center;align-items: center;" ><div style="width:85%;text-align:center;"><center><p style="font-family:'+familyLocal[i]+';font-size:'+sizeLocal[i]+';white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">'+textContent.slice(startLen,parseInt(lenCaptionLocal[i])+startLen)+'</p></center></div></div></center></div>');
        }
  
  
      }
  
      startLen = startLen + parseInt(lenCaptionLocal[i]);
  
  
   }
    
    console.log("none Section Execute"+name);
    if(name==" Me")
    {
      console.log("none Section Execute");
      document.getElementById("StoryReplySectionPlaceId").style.display="none";
    }
    else
    {
      document.getElementById("StoryReplySectionPlaceId").style.display="block";
    }
      
  
      document.getElementsByClassName("storyProfileSection")[0].src=pic;
      document.getElementById('textStoryVisiblePersonName').innerHTML=name;
   }
  
  
  
  
   $(document).ready(function () {
  
    // ANIMATEDLY DISPLAY THE NOTIFICATION COUNTER.
    $('#noti_Counter')
        .css({ opacity: 0 })
          // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
        .css({ top: '-10px' })
        .animate({ top: '-2px', opacity: 1 }, 500);
  
    $('#noti_Button').click(function () {
  
        // TOGGLE (SHOW OR HIDE) NOTIFICATION WINDOW.
        $('#notifications').fadeToggle('fast', 'linear', function () {
            if ($('#notifications').is(':hidden')) {
                $('#noti_Button').css('background-color', '#2E467C');
            }
            // CHANGE BACKGROUND COLOR OF THE BUTTON.
            else $('#noti_Button').css('background-color', '#FFF');
        });
  
        $('#noti_Counter').fadeOut('slow');     // HIDE THE COUNTER.
  
        return false;
    });
  
    // HIDE NOTIFICATIONS WHEN CLICKED ANYWHERE ON THE PAGE.
    $(document).click(function () {
        $('#notifications').hide();
  
        // CHECK IF NOTIFICATION COUNTER IS HIDDEN.
        if ($('#noti_Counter').is(':hidden')) {
            // CHANGE BACKGROUND COLOR OF THE BUTTON.
            $('#noti_Button').css('background-color', '#2E467C');
        }
    });
  
    $('#notifications').click(function () {
        return false;       // DO NOTHING WHEN CONTAINER IS CLICKED.
    });
  });
  
  function tagFriendPeopleTextBox()
  {
    $('#tagPeoplenameArea').empty();
    var frnd = document.getElementById("tagFriendsTextBoxId").value;
     for(i=0;i<(taggedWholeFriendList.name).length;i++)
          {
            if(((taggedWholeFriendList.name[i].toUpperCase()).search(frnd.toUpperCase()))!=-1)
            {
              $('#tagPeoplenameArea').append('<input type="checkbox" id="'+taggedWholeFriendList.userId[i]+'" name="'+taggedWholeFriendList.userId[i]+'" value="'+taggedWholeFriendList.userId[i]+'"><label for="'+taggedWholeFriendList.userId[i]+'"><span><img src="'+taggedWholeFriendList.pic[i]+'" style="width:45px;height:45px;border-radius:50%;margin:8px;"></span>'+taggedWholeFriendList.name[i]+'</label><br>');

              $('#tagPeoplenameArea').append('<a href="/profile/'+taggedWholeFriendList.userId[i]+'" onclick="tagging(\''+taggedWholeFriendList.userId[i]+ '\',\''+taggedWholeFriendList.name[i]+ '\')"><label ><span><img src="'+taggedWholeFriendList.pic[i]+'" style="width:45px;height:45px;border-radius:50%;margin:8px;"></span>'+taggedWholeFriendList.name[i]+'</label></a><br>');
            }
           
          }
  
  }
  var seperator="";
  
  function tagging(val,val2){
    if(seperator.search(val)<0)
    {
      seperator=seperator+","+val;
    $("#selectedPeople").append('<span class="badge badge-primary" id="Badge'+val+'">'+val2+'<button type="button" class="close" aria-label="Dismiss"  ><span aria-hidden="true" onclick="closeBadge(\''+val+'\')">&times;</span></button></span>');
    }
  }
  
  function closeBadge(v)
  {
    console.log("seperator = "+seperator);
    console.log(v);
    
    seperator=seperator.replace(","+v,"");
   
    document.getElementById("Badge"+v).remove();
  }


function TagSubmissionForm()
{
  console.log("Working"); 

  $.ajax({
    method:'POST',
    url:'/tagSubmissionForm/',

    data:{
      tagPerson:seperator,
      postId:postIdGlobal,
    },
    
    success:function(e){
      document.getElementById("profile"+postIdGlobal).textContent="is with "+seperator.split(",");
    $("#selectedPeople").empty();
    seperator="";
    },
    error:function(data){
      console.log('Failed');
    }
  })

 $('#tagPeopleModel').modal('hide') 
}


function allTagList(Id)
{
  
  $.ajax({
    method:'POST',
    url:'/showAllTagPerson/',

    data:{
     
      postId:Id,
    },
    
    success:function(e){
      console.log(e);
    $("#AllTagPersonListId").empty();
    for (i=0;i<(e.userName).length;i++)
    {
    $("#AllTagPersonListId").append('<a href="/profile/'+e.userName[i]+'" style="text-decoration:none;border-radius:25px;padding:6px 12px;background:#E9ECEF;margin:8px;">'+e.FName[i]+' '+e.LName[i]+'</a><br><br>');
    }
    },
    error:function(data){
      console.log('Failed');
    }
  })



}



function seeAllCommentFunction(v1,v2,v3)
{
  $("#seeAllCommentsIdDiv").empty();

  $("#seeAllCommentsIdDiv").append('<div><span class="ml-5">'+v3+'</span></div>');
  if(v2!=""){
  $("#seeAllCommentsIdDiv").append('<center><div style=""><img src="'+v2+'" style="width:80%;height:250px;" alt=""></div></center><br><br>');
  }
  
  $.ajax({
    method:'POST',
    url:'/CommentShow/',

    data:{
     
      postId:v1,
    },
    
    success:function(e){
      console.log(e);
      nm=document.getElementById("mynameId").innerHTML;
      for(i=0;i<(e.ParentcommentId).length;i++)
      {

        $("#seeAllCommentsIdDiv").append('<div style="padding:8px;background:#E9ECEF;border-radius:25px;display: inline-block;"><span><img src="'+e.ParentcommentUserpic[i]+'" style="width:35px;height:35px;border-radius:50%;"></span><span  style="color:#00a087;font-weight:bold;" class="ml-2">'+e.parentcommentName[i]+' </span><br><span class="ml-5">'+e.ParentComment[i]+'</span><span><span id="replybtn" onclick="reply(\''+v1+'\',\''+e.ParentcommentId[i]+'\',\''+nm+'\',\''+e.ParentcommentByList[i]+'\')"><strong style="cursor:pointer;" class="ml-2 font-weight-bold">Reply</strong></span><br><input type="text" style="display:none" id="reply'+e.ParentcommentId[i]+'" placeholder="Type your reply"></span></div><br><br>');
        for(j=0;j<(e.childcommentId).length;j++)
        {
          if(e.ParentcommentId[i]==e.childcommentId[j]){
          $("#seeAllCommentsIdDiv").append('<div><i class="fas fa-reply"></i><div style="padding:8px;background:#E9ECEF;border-radius:25px;display: inline-block;"><span><img src="'+e.childcommentUserpic[j]+'" style="width:35px;height:35px;border-radius:50%; class="font-weight-bold"></span><span style="color:#00a087;font-weight:bold;" class="ml-2">'+e.childcommentName[j]+' </span><br><span class="ml-5">'+e.ChildComment[j]+'</span></div></div> <br>');
          
          }
          
        }$("#seeAllCommentsIdDiv").append('<hr>');


      }
    
    
    },
    error:function(data){
      console.log('Failed');
    }
  })


  
}

function storyReply(){
  receiver = document.getElementById('textStoryVisiblePersonName').textContent;
  message = document.getElementById('textStoryCommentReplay').value;
  $.ajax({
    method:'POST',
    url:'/storyreply/',

    data:{
    message:'Story:\n '+message,
    receiver:receiver,
    },
    
    success:function(e){
      document.getElementById("textStoryCommentReplay").value="";
      document.getElementById("snackbarMessage").innerHTML="your reply has sent";
      myFunction();
      console.log(e);
      
    },
    error:function(data){
      console.log('Failed');
      document.getElementById("snackbarMessage").innerHTML="Some issue occure";
      myFunction();
    }
  })

  console.log(receiver);
}


// Reply On Comments
function reply(ID,commentId,name,commentOf){
  console.log(ID)
  document.getElementById('reply'+commentId).style.display='block';
  document.getElementById('reply'+commentId).focus();
  //document.getElementById('reply'+commentId).value=name;

  $('#reply'+commentId).keyup(function(){
var reply = $('#reply'+commentId).val();
if (event.keyCode === 13){ // when enter key is pressed
  console.log(reply);
  $.ajax({
          method:'POST',
          url:'/reply/',
          data:{
            postId:ID,
            commentId:commentId,
            repliedBy:document.getElementById('currentUserId').value,
            repliedOn:commentOf,
            reply:reply,
          },
          success:function(data){
            alert("your reply has been saved");
            $('#seeAllComments').modal('hide'); 
  document.getElementById('allReplies'+commentId).innerHTML=reply
  document.getElementById('reply'+commentId).style.display='none';
}
      });
}

}
)};

function deletePost(val)
  {
    var result = confirm("Want to delete?");
    if (result) {
        
  
        $.ajax({
        method:'POST',
        url:'/deshboarDeletePost/',
        data:{
          postId:val,
        },
        
        success:function(e){
          
          console.log(e);
          
          $("#postBox"+val).remove();

          if (location.pathname != '/' ){
            location.replace("/");
        }
        },
        error:function(data){
          console.log('Failed');
        }
      })
  
  
  
  
    }
    else
    {
      alert("Not Deleted = ",+val);
    }
  }



  //Spam Message Check
  function SpamTester(message)
  {
    

    $.ajax({
        method:'POST',
        url:'/spamMessageTester/',
        data:{
          message:message,
        },
        
        success:function(e){
          
          console.log(e);
          if(e.status==0)
          {
            alert("Your Post does not comes into Spam.");
          }
          else if(e.status==1)
          {
            alert("There are more Probability that Your Post comes into Spam be Careful."); 
          }
          
          
        },
        error:function(data){
          console.log('Failed');
        }
      })

  }



  //Is Viewed Notification

  function viewNotification()
  {
    $.ajax({
        method:'POST',
        url:'/notifications/',
        data:{
          action:'viewed',
        },
        
        success:function(e){
          
          console.log(e);
          
          
        },
        error:function(data){
          console.log('Failed');
        }
      })  
  }

  // Snackbar

  function myFunction() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}