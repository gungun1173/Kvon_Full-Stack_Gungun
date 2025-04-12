$(document).ready(function () {
    $(".email").click(function () {
        $(".email").css("border-color", "BLUE");
    });

    let val1 = $(".email").val();
    let val2 = $(".password").val();


    $(".email").focusout(function () {

        if (val1.length < 8) {
            alert('Invalid Input');
        }
    });

    $(".password").focusout(function () {

        if (val2.length < 6) {
            alert('Invalid Input');
        }
    });

});