'use strict';

// DOM is a WEB API
const message = document.querySelector('.message')
const secretNum = document.querySelector('.number')
const guessBox = document.querySelector('.guess')
const check = document.querySelector('.check')
const again = document.querySelector('.again')
const body = document.querySelector('body')
var highscore = document.querySelector('.highscore')
var guessNum;
var randNumber = Math.floor(Math.random() * 20) + 1;
let score = 20;

//secretNum.textContent = randNumber

message.textContent = "Lets fight!" + '\u{1F389}'

check.addEventListener('click', () => {
    guessNum = Number(guessBox.value);
    // No input
    if(!guessNum) {
        message.textContent = '\u{1F9B2}' + ' No number';

        // Player winds
    } else if(guessNum === randNumber) {
        if (highscore < score) {
            Number(highscore.value) = score
        }
        body.style.backgroundColor = '#60b347';
        secretNum.textContent = randNumber
        message.textContent = '\u{1F973}' + ' Winner!!! ' + '\u{1F973}'
        secretNum.style.width = '30rem'
        highscore.textContent = score

        // When the guess is not equal to random number
    } else if(guessNum !== randNumber) {
        if (score > 1) {
            message.textContent = guessNum > randNumber ? 'Too High' : 'Too Low'
            score--         
            document.querySelector('.score').textContent = score
        } else {
            message.textContent = 'You lost ' + '\u{1F974}'
            document.querySelector('.score').textContent = 0;
        }
    }
        // Guess is too high
    // } else if (guessNum > randNumber) {
    //     if (score > 1) {
    //         score--
    //         message.textContent = 'Too High'
    //         document.querySelector('.score').textContent = score
    //     } else {
    //         message.textContent = 'You lost ' + '\u{1F974}'
    //     }

    //     // guess is too low
    // } else if (guessNum < randNumber) {
    //     if (score > 1) {
    //         score--
    //         message.textContent = 'Too Low'
    //         document.querySelector('.score').textContent = score
    //     } else {
    //         message.textContent = 'You lost ' + '\u{1F974}'
    //     }
    // } 
});

again.addEventListener('click', () => {
    message.textContent = 'Lets fights! ' + '\u{1F389}'
    randNumber = Math.floor(Math.random() * 20) + 1;
    secretNum.textContent = '?'
    body.style.backgroundColor = '#222'
    guessBox.value = ''
    document.querySelector('.score').textContent = '20'
    secretNum.style.width = '15rem'

});


function updateScore(number) {

}
