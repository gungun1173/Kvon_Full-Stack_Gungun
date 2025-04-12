$(document).ready(function(){

    $(".btn-1").click(function(){
        $(".txt").removeClass("hidden");
       let read = $(".input").val();
       $(".txt").text(read);
    });

    $(".btn-2").click(function(){
       $(".txt").addClass("hidden");
     });
});