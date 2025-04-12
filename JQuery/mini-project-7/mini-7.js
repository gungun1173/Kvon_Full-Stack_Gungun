
$(document).ready(function(){
   
    const carouselrow = $(".blog-row");
    const cards = Array.from($(".blog-card"));


    function updatecarousel() {
        const movecard = cards.shift();
        cards.push(movecard);
        carouselrow.append(movecard);
    
    
    }
    
    setInterval(updatecarousel, 2000);
});
