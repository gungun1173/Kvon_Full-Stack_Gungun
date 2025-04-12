
$(document).ready(function(){

  

   $(".append").click(function(){
  
  $(".display-2").val($(".display-2").val() + $(this).html())
  
});

   $(".clear").click(function(){

       $(".display-2").val("");
   });
    
   $(".calculate").click(function(){
        
        $(".display-2").val(eval($(".display-2").val()));
   });
});