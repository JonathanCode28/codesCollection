const secretImg = document.getElementById('secretImg');
const imgHide = document.getElementById('imgHide');
const hide = document.getElementById('hide');

function checkImg(answer){
    if(answer==='v'){
        const vSound = new Audio('sounds/v.mp3')
        vSound.play()
       secretImg.setAttribute('src', 'imgs/v.png')
    }else{
       secretImg.setAttribute('src', 'imgs/x.png')
       const xSound = new Audio('sounds/x.mp3')
       xSound.play()
    }
    document.getElementById('imgX').style.display='none';
    document.getElementById('secretDiv').style.display='block';
}
function checkBtn(answer){
    if(answer==='v'){
        const vSound = new Audio('sounds/v.mp3')
        vSound.play()
       secretImg.setAttribute('src', 'imgs/v.png')
    }else{;
       secretImg.setAttribute('src', 'imgs/x.png')
       const xSound = new Audio('sounds/x.mp3')
       xSound.play()
    }
    hide.style.display = 'none';
    document.getElementById('secretDiv').style.display='block';
}