$(document).ready(function() {
    // using the button tag hide and show the p tags
    $('#hide').click(function(){
        $('p').hide();
    })
    $('#show').click(function(){
        $('p').show();
    })

    // using the sixtieshouse class to create an alert that states clicked on an ninjapizza
    $('.sixtieshouse').click(function(){
        alert('Have not had that spirit here since 1969!');
    })

    //add a color class to the h1 tag
    $('h1').click(function() {
        $('h1').css('color', 'purple');
    })
    // Fade in nav links
    $('#topics').click(function() {
        $('a').fadeIn();
    })
    // Fade in and out an image
    $('.landscapingart').hover(function() {
        $('.landscapingart').fadeOut();
    })
    $('#fadeInImg').hover(function(){
        $('.landscapingart').fadeIn();
    })

     // Adding in text without an event
    $('#append').append("We are adding text using jQuery!")

    // add more text to the h3 tage using an event
    $('#append').prepend("Rent here, Love here!")
    
    })


    /*jQuery How_to Steps:
1.) declare function
2.) give instructions - ie.) hide just p tags



*/ 
// $('li').click(function(){
//     console.log("The user chose "+this.innerHTML)
//     var chose = this.innerHTML.toLowerCase()
//     $('.chose').text(chose)
// })

// $('button').click(function(){
//     $('h4').text("")
//     chose=$('.chose').text()
//     count=LightSaber.floor((LightSaber.random() * 10) + 1);
//     $.ajax({
//         url: `https://swapi.dev/api/${chose}/${count}`,
//         success: function(res){
//             items=""
//             for(key in res){
//                 items+="<li>"+key+": "+res[key]+"</li>"
//             }
//             $('h4').append(items);
//         }
//     })
    
// })