$(document).ready(function () {
    $(".btn-1").click(function () {
        $(".p-1").hide();
    });

    $("p").click(function () {
        $(this).hide();
    });

    $("#p1").hover(function () {
        alert("Welcome to JQuery tutorials!!")
    },
        function () {
            alert("The tutorial ends here....!")
        });
    
    $("input").focus(function(){
        $(this).css("background-color", "yellow")
    });
    $("input").blur(function(){
        $(this).css("background-color", "gray")
    });

    $(".box-1").on({
        mouseenter: function(){
            $(this).css("background-color", "gray")
        },
        mouseleave: function(){
            $(this).css("background-color", "blue")
        },
        click: function(){
            $(this).css("background-color", "purple")
        }
    });

    $("#flip-1").click(function(){
        $("#panel-1").fadeToggle();
    });

    $("#flip-2").click(function(){
        $("#panel-2").fadeOut();
    });

    $("#flip-3").click(function(){
        $("#panel-3").fadeIn();
    });

    $("#f-1").click(function(){
        $("#p-1").slideToggle();
    });

    $("#f-2").click(function(){
        $("#p-2").slideUp();
    });

    $("#f-3").click(function(){
        $("#p-3").slideDown();
    });

    $(".btn").click(function(){
        var box = $(".box")
        box.animate({height:'400px', opacity: '0.15'}, "slow");
        box.animate({width:'400px', opacity: '0.7'}, "slow");
        box.animate({height:'100px', opacity: '0.4'}, "slow");
        box.animate({width:'100px', opacity: '0.9'}, "slow");

    })

});