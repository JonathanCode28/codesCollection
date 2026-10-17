$(document).ready(function(){
    $('.left img').hide();
    $('.right img').hide();
    function randomPcCharacter(){
        let imgs = ["img/hp.png", "img/ron.png", "img/her.png", "img/al.png", "img/min.png", "img/sev.png", "img/nev.png", "img/dra.png", "img/vol.png"];
        let randomNumber = Math.floor(Math.random() * imgs.length);
        return imgs[randomNumber];
    }
    
    $('#PlayBtn').click(function(){
        $('#msg').hide();
        $('.left img').hide();
        $('.right img').hide()
        let MyOption = $('#OptionSelect').find(':selected').val();
        let randomAnimal = randomPcCharacter();
        $('.left img').attr("src", MyOption);
        $('.right img').attr("src", randomAnimal);
        $('.left img').fadeIn('slow');
        $('.right img').fadeIn('slow')
        if(randomAnimal === MyOption){
            $('#msg').html("YES!!! you did it!");
            $('#msg').slideDown(1000);
            $('#msg').css("backgroundColor", "green");
            $('#winImg').fadeIn(1500);
            $('#winImg').animate({top: '350px'}, 500);
            $('#winImg').animate({left: '350px'}, 500);
            $('#winImg').animate({top: '0px'}, 500);
            $('#winImg').animate({left: '0px'}, 500);
            $('#winImg').animate({top: '350px'}, 500);
            $('#winImg').animate({left: '350px'}, 500);
            $('#winImg').animate({top: '0px'}, 500);
            $('#winImg').animate({left: '0px'}, 500);
            $('#winImg').fadeOut(1500);
        }else{
            $('#msg').html("NO!!! Do not try again!!! It is not possible!!!");
            $('#msg').slideDown(1000);
            $('#msg').css("backgroundColor", "red");
        }
    });
});