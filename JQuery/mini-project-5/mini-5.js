$(document).ready(function () {
    $("body").css("background-color", "rgb(7, 129, 107)");
    $("button").css("background-color", "rgb(17, 174, 146)");
    $("button").css("color", "white")

    // Removing the Modal
    $(".fa-xmark").click(function () {
        $(".popup").addClass("hidden");
        $("body").css("background-color", "rgb(17, 174, 146)");
    });

    // Validating the Email
    $(".subscribe").click(function () {

        let value = $(".email").val();
        let val2 = $(".password").val();
        function isEmail(value) {

            // Regular Expression for searching the pattern
            const regex = /^([a-z0-9_\.\-\+])+\@([gmail]{5})+\.([com]{3})$/;
            if (!regex.test(value)) {
                return false;
            }
            else {
                return true;
            }
        }

        function isPassword(val2){
            const pss = /^([0-9]{6})$/;
            if(!pss.test(val2)){
                return false;
            }
            else{
                return true;
            }
        }
        if (value === "" || isEmail(value) === false || val2 === "" || isPassword(val2) === false) {
            alert('Invalid Email or Password');
        }
        else {

            $(".content").html("<h2>Thanks for Subscribing!!</h2>");
        }

    });

    // Showing the Modal
    $(".in").click(function () {
        $(".popup").removeClass("hidden");
        $("body").css("background-color", "rgb(7, 129, 107)");

    });




});