$(document).ready(function(){
$('.delete').on('click', function(){
    var $this = $(this)
    var _user_id = $(this).data('answer');
    $.ajax({
      url: "/delete",
      type: "get",
      data: {
        'user_id':_user_id,
      },
      dataType: "json",
      success: function (res) {
        if(res.bool==true){
          $this.parents(".content").remove();
        }else{
          alert(res.message);}
        }
    });
  });
});