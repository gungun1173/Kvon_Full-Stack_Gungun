
function randomColorGenerator(){
    let value1 = (0 + Math.random() * 255);
    let value2 = (0 + Math.random() * 255);
    let value3 = (0 + Math.random() * 255);
 return `rgb(${value1}, ${value2}, ${value3})`;
};

$(document).ready(function(){

   setInterval(() => {

        $(".box").css("background-color", randomColorGenerator());
       
        $(".box").css("color", randomColorGenerator());
    }, 500);


   setInterval(() => {
    $("h2").css("color", randomColorGenerator());
    $("body").css("background-color", randomColorGenerator());
   }, 1000);
});

