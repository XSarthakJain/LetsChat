$(document).ready(function() {
  $(".btn-pref .btn").click(function () {
      $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
      // $(".tab").addClass("active"); // instead of this do the below 
      $(this).removeClass("btn-default").addClass("btn-primary");   
  });
  
  $('#search').keyup(function(){
      
      $("ul").empty()
  
     var searchField = $('#search').val();
     console.log(searchField);
  if(searchField.length)
    $.ajax({
                  method:'POST',
                  url:'/liveSearchProcess/',
                  data:{
                    search:searchField
                  },
                  success:function(data){
                    console.log(data);
                    
                    for(var i=0;i<(data.Id).length;i++)
                    {
                      
                       $('#result').append('<li class="list-group-item link-class" ><img src="'+data.picture[i]+'" height="40" width="40" class="img-thumbnail" />'+data.Username[i]+' | <span class="text-muted">'+data.uname[i]+'</span></li>');
                      }
                   incomingRequest();
                   outgoingRequest();
              
                  },
                  error:function(data){
                      console.log('Error!');
                      
                  }
  
              });
  else{
    incomingRequest();
    outgoingRequest();
  }
  
  });
  
    $('#result').on('click', 'li', function() {
    var click_text = $(this).text().split('|');
    $('#search').val($.trim(click_text[0]));
    console.log($('#personId').val($.trim(click_text[1])));
    $("#result").html('');
   });
  });
  
  //Incoming Request
  function incomingRequest(){
  $.ajax({
                  method:'POST',
                  url:'/incomingRequest/',
                  
                  success:function(data){
                    console.log(data);
                    for(var i=0;i<(data.senderId).length;i++)
                    {
                      
                       $('#incomingResult').append('<a href="/profile/'+data.senderId[i]+'" style="text-decoration:none;"><li class="list-group-item link-class" ><img src="'+data.pic[i]+'" height="50" width="50" class="img-thumbnail" />'+data.senderName[i]+' | <span class="text-muted">'+data.senderId[i]+'</span></li></a>');
                      }
  
  
    },
     error:function(data){}
   })
  
  }
  


  
  //Incoming Request  
  function outgoingRequest(){
  $.ajax({
                  method:'POST',
                  url:'/outgoingRequest/',
                  
                  success:function(data){
                    console.log(data);

                 
                    for(var i=0;i<(data.reciverId).length;i++)
                    {
                      
                       $('#outgoingResult').append('<a href="/profile/'+data.reciverId[i]+'" style="text-decoration:none;"><li class="list-group-item link-class" ><img src="'+data.reciverPic[i]+'" height="50" width="50" class="img-thumbnail" />'+data.receiverName[i]+' | <span class="text-muted">'+data.reciverId[i]+'</span></li></a>');
                      }
  
  
    },
     error:function(data){}
   })
  
  }
  
  incomingRequest();
  
  outgoingRequest();

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
  document.getElementById("coverWell").style.backgroundColor="black";
  document.getElementById("coverWell").style.border="none";
  document.getElementById("tab2").style.color="white";
  document.getElementById("tab3").style.color="white";
  document.getElementById("result").style.backgroundColor="black";  

}

function dayMode()
{
  
}

  autoMode();


