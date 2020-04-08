/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result gets added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLOBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game.

*/


var scores, roundScore, activePlayer, dice, gamePlaying, rollSix;

newGame();
//scores = [0, 0];
//roundScore = 0;
//activePlayer = 0;  // 0 is player1, 1 is player2

// Creating the dice

//dice = Math.floor(Math.random() * 6) + 1;

// DOM manipulation uses the document object
// Allows us to select stuff like css

//document.querySelector('#current-' + activePlayer).textContent = dice;

// I can wirte innerHTML code but it needs to be in string form
//document.querySelector('#current-' + activePlayer).innerHTML = '<em>' + dice + '</em>'


// set a value in the variable x using setters and getters.
//var x = document.querySelector('#score-1').textContent;
//console.log(x)

// used query selector to hide the dice image


//function btn() {
//    //do something
//};
//
//btn();

//document.querySelector('.btn-roll').addEventListener('click',btn); 
//btn here will be a call back function b/c it is called by event listener
// or create an anonomou function, create the function within 

//document.querySelector('.dice').style.display = 'none';

// another way to access element from HTML
// set all the scores to 0.... moved to newGame()
//document.getElementById('score-0').textContent = '0';
//document.getElementById('score-1').textContent = '0';
//document.getElementById('current-0').textContent = '0';
//document.getElementById('current-1').textContent = '0';

document.querySelector('.btn-roll').addEventListener('click', function() {
    if (gamePlaying) {
        // 1. random number
        var dice1 = Math.floor(Math.random() * 6) + 1;
        // var dice2 = Math.floor(Math.random() * 6) + 1;


        // 2. Display the results
        // var diceDOM = document.querySelector('.dice');
        document.getElementById('dice-1').style.display = 'block';
        //document.getElementById('dice-2').style.display = 'block';
        
        document.getElementById('dice-1').src = 'dice-' + dice1 + '.png';
        //document.getElementById('dice-2').src = 'dice-' + dice2 + '.png';


        // diceDOM.style.display = 'block';
        //diceDOM.src = 'dice-' + dice + '.png';
        
        // If the dice is a 6 add it it rollSix
        if ( (dice1 === 6)) { //|| (dice2 === 6) )  {
            rollSix += 1;
        }
        
        // 3. update the round score IF the rolled number was not a 1
            if ( (dice1 !== 1)  && (rollSix !== 2) ) {  //recall 1== does not perform type coercion
            // Add the score
            roundScore += (dice1);
            document.querySelector('#current-' + activePlayer).textContent = roundScore;
        } else {
            //Its the next players turn

            nextPlayer();
        }
    }
});

document.querySelector('.btn-hold').addEventListener('click', function() {
    if (gamePlaying) {
        // Add current score to gloabl score
        scores[activePlayer] += roundScore;

        // upadate the UI
        document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer];
        var inputScore = document.querySelector('.final-score').value;
        
        // check if the value inputScore is not empty,  undefined, 0, null or "" are COERCED
        if (inputScore) {
            var winningScore = inputScore;
        } else {
            winningScore = 100;
        }
        // check if player won the game
        if (scores[activePlayer] >= winningScore) {
            document.querySelector('#name-' + activePlayer).textContent = 'Winner!';
            // document.querySelector('.dice').style.display = 'none';
            document.getElementById('dice-1').style.display = 'none';
            //document.getElementById('dice-2').style.display = 'none';
            document.querySelector('.player-' + activePlayer + '-panel').classList.add('winner');
            document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');
            gamePlaying = false;

        } else { // games continues
            // Next Player
            nextPlayer();
        }
    }
});


function nextPlayer() {
    //Its the next players turn

    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
    roundScore = 0;
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';

    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');
    // document.querySelector('.player-0-panel').classList.remove('active');
    // document.querySelector('.player-1-panel').classList.add('active');

    // document.querySelector('.dice').style.display = 'none'; 
    document.getElementById('dice-1').style.display = 'none';
    //document.getElementById('dice-2').style.display = 'none';
}


document.querySelector('.btn-new').addEventListener('click', newGame);

function newGame() {
    scores = [0, 0];
    activePlayer = 0;
    roundScore = 0;
    rollSix = 0
    gamePlaying = true;
    // document.querySelector('.dice').style.display = 'none';
    document.getElementById('dice-1').style.display = 'none';
    //document.getElementById('dice-2').style.display = 'none';

    document.getElementById('score-0').textContent = '0';
    document.getElementById('score-1').textContent = '0';
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';
    
    document.getElementById('name-0').textContent = 'Player 1';
    document.getElementById('name-1').textContent = 'Player 2';
    
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-1-panel').classList.remove('active');
    document.querySelector('.player-0-panel').classList.add('active');

};





