'use strict';

const game = {
  team1: 'Bayern Munich',
  team2: 'Borrussia Dortmund',
  players: [
    [
      'Neuer',
      'Pavard',
      'Martinez',
      'Alaba',
      'Davies',
      'Kimmich',
      'Goretzka',
      'Coman',
      'Muller',
      'Gnarby',
      'Lewandowski',
    ],
    [
      'Burki',
      'Schulz',
      'Hummels',
      'Akanji',
      'Hakimi',
      'Weigl',
      'Witsel',
      'Hazard',
      'Brandt',
      'Sancho',
      'Gotze',
    ],
  ],
  score: '4:0',
  scored: ['Lewandowski', 'Gnarby', 'Lewandowski', 'Hummels'],
  date: 'Nov 9th, 2037',
  odds: {
    team1: 1.33,
    x: 3.25,
    team2: 6.5,
  },
};

const [players1, players2] = game.players;

console.log(players1);
console.log(players2);

const [gk, ...fieldPlayers] = players1;
console.log(gk, fieldPlayers);

const allPlayers = [...players1, ...players2];
console.log(allPlayers);

const playersFinal = [...players1, 'Thiago', 'Coutinho', 'Perisic'];
console.log(playersFinal);

// const {team1, x:draw, team2} = game.odds
const {
  odds: { team1, x: draw, team2 },
} = game;

console.log(team1, draw, team2);

const printGoals = function (...players) {
  console.log(`${players.length} goals were scores`);
  for (let i = 0; i < players.length; i++) {
    console.log(players[i]);
  }
};

printGoals('Davies', 'Muller', 'Lewandowski', 'Kimmich');

const scores = game.scored;
console.log(scores);
for (const [goal, name] of scores.entries()) {
  console.log(`Goal ${goal}: ${name}`);
}

const odds2 = game.odds;
console.log(odds2);
let sum = 0;
for (const [team, odd] of Object.entries(odds2)) {
  if (team !== 'x') sum += odd;
}
console.log(sum / 3);

const scorers = {
  Gnarby: 1,
  Hummels: 1,
  Lewandowski: 2,
};

const gameEvents = new Map([
  [17, '⚽ GOAL'],
  [36, '🔁 Substitution'],
  [47, '⚽ GOAL'],
  [61, '🔁 Substitution'],
  [64, '🔶 Yellow card'],
  [69, '🔴 Red card'],
  [70, '🔁 Substitution'],
  [72, '🔁 Substitution'],
  [76, '⚽ GOAL'],
  [80, '⚽ GOAL'],
  [92, '🔶 Yellow card'],
]);

const eventsAArray = [...new Set(gameEvents.values())];
// const eventsAArray = new Set([...gameEvents.values()])

console.log('Map to array', eventsAArray);

gameEvents.delete(64);
console.log(gameEvents, 'ENDDDD');

const checkDogs = (dogsJulia, dogsKate) => {
  const juliaCopy = dogsJulia.slice(1, -1);
  const allDogs = [...juliaCopy, ...dogsKate];
  allDogs.forEach((age, i) => {
    if (age < 3) {
      // its a puppu
      console.log(`Do number ${i + 1} is a puppy, and is ${age} years old`);
    } else {
      // its an adult
      console.log(`Do number ${i + 1} is an adult, and is ${age} years old`);
    }
  });
};

// checkDogs([3, 5, 2, 12, 7], [4, 1, 15, 8, 3])

const arr = [1, 2, 3, 4, 5];
const arr2 = arr;
console.log(arr);
console.log(arr2);

arr2[1] = 3;
console.log('--------Changed-------');
console.log(arr);
console.log(arr2);
