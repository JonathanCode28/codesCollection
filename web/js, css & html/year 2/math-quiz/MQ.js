const numberInput = document.getElementById('numberInput');
const scoreSpan = document.getElementById('scoreSpan');
const msg = document.getElementById('msg');

let number1 = 1;
let number2 = 2;
let score = 0;
let max = 10;

function check(){
    let answer = number1 + number2;
    let userAnswer = +numberInput.value;
    console.log(userAnswer)
    if(userAnswer === 0)return;
    if(userAnswer === answer){
        //alert("VERY GOOD!!!")
        score++;
        scoreSpan.innerHTML = score;
        numberInput.disabled = true;
        numberInput.value='';
        msg.innerHTML = "GREAT!!! YOU DID IT!"
    }else{
        //alert("TRY AGAIN...");
        msg.innerHTML = "SORRY... TRY AGAIN!"
    }
}
function newGame(){
    max+=10;
    numberInput.disabled = false;
    msg.innerHTML = "";
    number1 = Math.ceil(Math.random() *max);
    number2 = Math.ceil(Math.random() *max);
    console.log(number1, number2);
    
    document.getElementById('spanNumber1').innerHTML = number1;
    document.getElementById('spanNumber2').innerHTML = number2;
}
