

$(document).ready(function () {
    $(".btn").click(async function fetchData() {
        try {
            const response = await fetch("https://qapi.vercel.app/api/random")
            const data = await response.json();
            $(".text").html('<span>"</span>' + data.quote + '<span>"</span>');
            $(".author").html('<span>--</span>' + " " + data.author);

        }
        catch (error) {
            console.error(error);

        }
    });
});

// const $btn = $(".btn")
// $btn.click(function changeQuote() {
//     let number = Math.floor(Math.random() * quote_list.length);
//     $(".text").html('<span>"</span>' + quote_list[number].quote + '<span>"</span>');
//     $(".author").html(quote_list[number].author);


// });
