$(document).ready(function(){
    $('.like_form').submit(function(e){
        e.preventDefault();
    const video_id = $('.like-btn').val()
    const token=$('input[name=csrfmiddlewaretoken]').val();
    const url=$(this).attr('action') 
    $.ajax({
        method :"POST",
        url:url,
        headers:{'X-CSRFToken': token},
           data:{
               'video_id':video_id
           },
           success:function(response){
               if(response.liked==true){
                $('.like-btn').addClass('text-blue-700')
            }else{
              $('.like-btn').removeClass('text-blue-700')
            }
          
             like=$('#like-count').text(response.likes_count)
             parseInt(like)
               }

           
    })
})
})
