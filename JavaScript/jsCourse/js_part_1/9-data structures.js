'use strict';

const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],
  order: function (starterIndex, mainIndex) {
    return [this.starterMenu[starterIndex], this.mainMenu[mainIndex]];
  },
  // I can destructure here and provide default values
  orderDelivery: function ({
    starterIndex = 1,
    mainIndex = 0,
    time = '20:00',
    address,
  }) {
    console.log(
      `Order received, ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`
    );
  },
  orderPasta: function (ing1, ing2, ing3) {
    console.log(ing1, ing2, ing3);
  },
  orderPizza: function (mainIngredients, ...otherIngredients) {
    console.log(mainIngredients);
    console.log(otherIngredients);
  },
  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
};

restaurant.orderDelivery({
  time: '22:30',
  address: 'Via del Sole, 21',
  mainIndex: 2,
  starterIndex: 2,
});

const [a, b, c] = [1, 2, 3];

const [first, second] = restaurant.categories;
console.log(first, second);

const [main, , secondary] = restaurant.categories;
console.log(main, secondary);

console.log(a);

const [starter, main2] = restaurant.order(2, 0);
console.log(starter, main2);

const nested = [2, 4, [5, 6]];
const [i, , [j, k], m = 1] = nested;
console.log(i, j, k, m);

// Destructure Objects

const { name, openingHours, categories } = restaurant;

const {
  name: restaurantName,
  openingHours: hours,
  categories: tags,
} = restaurant;

console.log(restaurantName);

const { menu = [], starterMenu, starters = [] } = restaurant;
console.log(menu, starter);

// mutating variables
let a1 = 111;
let b1 = 999;
const obj = { a1: 23, b1: 7, c: 14 };

({ a1, b1 } = obj);

console.log(a1, b1);

// nested objects
const {
  fri: { open: o, close },
} = hours;
console.log(o, close);

// Spread operator: works on all iterables, even objects
const arr3 = [7, 8, 9];

const arr4 = [...arr3, 10, 11]; // array unpacking
console.log(arr4);
console.log(...arr4);

const newMenu = [...restaurant.mainMenu, 'Gnocci'];

console.log(newMenu);

// shallow copy this is like Object.assign({}, restaurant.mainMenu)
const mainMenuCopy = [...restaurant.mainMenu];

const menu2 = [...restaurant.starterMenu, ...restaurant.mainMenu];
// console.log('fItem', fItem);
console.log('menu2', menu2);

const me = 'Gonzalo';
const letters = [...me, '', 'B.'];
console.log(letters);
console.log(`${[...letters]}`);

const ingredients = ['peppers', 'Pepperoni', 'Sausage'];
restaurant.orderPasta(...ingredients);

const restaurant2 = { ...restaurant, founder: 'Maria', foundingYear: 2023 };
console.log(restaurant);
console.log(restaurant2);

// Rest operator - packs elements into an array.
const [a3, b3, ...others] = [1, 2, 3, 4, 5];
console.log(a3);
console.log(b3);
console.log(others);

const [pizza, , risotto, ...otherFood] = [
  ...restaurant.mainMenu,
  ...restaurant.starterMenu,
];

console.log(pizza);
console.log(risotto);
console.log(otherFood);

const { sat, ...weekdays } = restaurant.openingHours;
console.log(sat, weekdays);

const add = function (...numbers) {
  console.log(numbers);
  console.log(arguments);
};

add(2, 3);
add(2, 3, 4, 5);

const x = [23, 5, 7];
add(...x); // spread them

restaurant.orderPizza('mushrooms', 'onions', 'olives', 'peperoni');
restaurant.orderPizza('meat');

restaurant.numGuests = 0;
const guests = restaurant.numGuests || 10;
console.log('Guests: ', guests);

// nullish coalescing  operator
const guestCorrect = restaurant.numGuests ?? 10;
console.log('Guests 2: ', guestCorrect);

const rest1 = {
  name: 'Capri',
  numGuests: 20,
};

const rest2 = {
  name: 'La Piazza',
  owner: 'Giovanni Rossi',
};

rest1.numGuests = rest1.numGuests || 10;
rest2.numGuests = rest2.numGuests || 10;

rest2.numGuests ||= 10;
rest2.numGuests ??= 10;

console.log(rest1);
console.log(rest2);

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
  // new syntax to write methods
  printGoals(...playersThatScoreAGoal) {
    for (let i = 0; i < playersThatScoreAGoal.length; i++) {
      console.log(`${playersThatScoreAGoal[i]} scored a goal`);
    }
    console.log(`There were ${playersThatScoreAGoal.length}`);
  },
};

const [players1, players2] = game.players;
console.log(players1, players2);

const [gk, ...fieldPlayers] = players1;
console.log('gk', gk);
console.log('players: ', fieldPlayers);

const allPlayers = [...players1, ...players2];
console.log('all: ', allPlayers);

const players1Final = [...players1, ' Thiago', 'Coutinho', 'Perisic'];
console.log('final: ', players1Final);

const lowerOdd =
  game.odds.team1 < game.odds.team2 ? game.odds.team1 : game.odds.team2;

console.log('lowerOdds: ', lowerOdd);

// Loops: I can use the break and continue in for of loop
for (const item of arr3) {
  console.log(item);
}

for (const item of menu2.entries()) {
  console.log('item:---> ', item);
}

for (let i = 0; i < arr3.length; i++) {
  if (arr3[i] === 8) {
    console.log('item is 8');
    break;
  }
  console.log('item: ', arr3[i]);
}

// enhanced object literals
const thu = {
  open: 12,
  close: 22,
};

const openingHours3 = {
  thu, // I don't have to write thu: thu since key and value are the same
  fri: {
    open: 11,
    close: 23,
  },
  sat: {
    open: 0, // Open 24 hours
    close: 24,
  },
  what: {
    open: 10,
    close: 22,
  },
};

console.log(openingHours3);

// OPTIONAL CHAINING --> we do't know if mon exists ES2020
// only if it is null or undefined

// mon is undefined and to undefined.open gives an error
// we can use an if statement
if (restaurant.openingHours.mon) {
  console.log(restaurant.openingHours.mon.open);
}
// only if monday exist then get open
console.log(restaurant.openingHours.mon?.open);
console.log(restaurant.openingHours.mon?.open);

const days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];

for (const day of days) {
  // console.log(day);
  // use bracket notation because we don't have a .day attribute
  const open = restaurant.openingHours[day]?.open ?? 'closed'; // use nullish coalescing operator
  console.log(`On ${day} we open at ${open}`);
}

console.log(restaurant.order?.(0, 1)) ?? 'Method does not exists';

const users = [{ name: 'test', email: 'me@me.com' }];

console.log(users[0]?.name ?? 'User array is empty');

// Looping over objects, keys or values or both
const properties = Object.keys(openingHours);
console.log(properties);

// loop over with keys
for (const day of Object.keys(openingHours)) {
  console.log('key: ', day);
}

// Object values
const values = Object.values(openingHours);
console.log(values);

// entries
const entries = Object.entries(openingHours);
console.log('entries: ', entries);
// we can use destructuring here to get day and the destructure day as well to get open and close
for (const [day, { open, close }] of Object.entries(openingHours)) {
  console.log(`On ${day} we open at ${open} and close at ${close}`);
}

///////////////////////////////////////
// Coding Challenge #2

/* 
Let's continue with our football betting app!

1. Loop over the game.scored array and print each player name to the console, along with the goal number (Example: "Goal 1: Lewandowski")
2. Use a loop to calculate the average odd and log it to the console (We already studied how to calculate averages, you can go check if you don't remember)
3. Print the 3 odds to the console, but in a nice formatted way, exaclty like this:
      Odd of victory Bayern Munich: 1.33
      Odd of draw: 3.25
      Odd of victory Borrussia Dortmund: 6.5
Get the team names directly from the game object, don't hardcode them (except for "draw"). HINT: Note how the odds and the game objects have the same property names 😉

BONUS: Create an object called 'scorers' which contains the names of the players who scored as properties, and the number of goals as the value. In this game, it will look like this:
      {
        Gnarby: 1,
        Hummels: 1,
        Lewandowski: 2
      }

GOOD LUCK 😀
*/

for (let i = 1; i <= game.scored.length; i++) {
  console.log(`Goal ${i}: ${game.scored[i]}`);
}

const odds = Object.values(game.odds);
let avg = 0;
for (const odd of odds) {
  avg += odd;
}

avg /= odds.length;

console.log('avg: ', avg);

for (const [key, odd] of Object.entries(game.odds)) {
  if (key !== 'x') {
    console.log(`Odd of victory`);
  }
}

const scorers = {};

for (const player of game.scored) {
  if (player in scorers) {
    scorers[player] += 1;
  } else {
    scorers[player] = 1;
  }
}

console.log(scorers);

// SETS

const ordersSet = new Set(['pasta', 'pizza', 'pizza', 'risotto', 'pasta']);

console.log(ordersSet);
console.log(ordersSet.has('pizza'));

for (const order of ordersSet) {
  console.log(order);
}

const ordersArray = [...ordersSet];
console.log(ordersArray);

// MAPS
// map values to keys
// keys can be any type, even arrays
// are iterable

const rest = new Map();
rest.set('name', 'Risotto Italiano');
rest.set(1, 'Italy ');
rest.set(2, 'Portugal');
console.log(rest);
console.log(rest.set(3, 'Michigan'));

rest.delete(2);

const question = new Map([
  ['question', 'What is best programming language in thw world?'],
  [1, 'C'],
  [2, 'Java'],
  [3, 'JS'],
  ['correct', 3],
  [true, 'correct'],
  [false, 'try again'],
]);

console.log(question);
console.log(Object.entries(openingHours3));
const hoursMap = new Map(Object.entries(openingHours3));
console.log(hoursMap);

for (const [key, value] of question) {
  console.log(key, value);
}

// map to array
console.log([...question]);
console.log([...question.keys()]);
console.log([...question.values()]);
console.log([...question.entries()]);

//

const gameEvents = new Map([
  [17, '⚽️ GOAL'],
  [36, '🔁 Substitution'],
  [47, '⚽️ GOAL'],
  [61, '🔁 Substitution'],
  [64, '🔶 Yellow card'],
  [69, '🔴 Red card'],
  [70, '🔁 Substitution'],
  [72, '🔁 Substitution'],
  [76, '⚽️ GOAL'],
  [80, '⚽️ GOAL'],
  [92, '🔶 Yellow card'],
]);

const events = new Set(gameEvents.values());

console.log(events);

gameEvents.delete(64);
console.log(gameEvents);

// strings
// access using index notation
// string methods
//
const airline = 'TAP Air Portugal';
const plane = 'A320';

// methods
console.log(airline.indexOf('r'));

console.log(airline.slice(4));
console.log(airline.slice(4, 6));

const checkMiddleSeat = function (seat) {
  return seat.slice(-1) === 'B' || seat.slice(-1) === 'E';
};

console.log(checkMiddleSeat('11B'));
console.log(checkMiddleSeat('11C'));

// create a String object
const str = new String('Jonas');
console.log(typeof str);

const meTo = 'GoNzALO';

console.log(meTo.toLocaleLowerCase()[0].toLocaleUpperCase());

const email = '    gonzALO@me.com \n';
console.log(email.toLocaleLowerCase().trim()); // remove white spaces

const priceGB = '288,97';
const priceUS = priceGB.replace(',', '.');
console.log(priceUS);

const capitalizeName = function (name) {
  const [fName, lName] = name.split(' ');
  console.log(
    fName.replace(fName[0], fName[0].toLocaleUpperCase()),
    lName.replace(lName[0], lName[0].toLocaleUpperCase())
  );
};

capitalizeName('gonzalo betancourt');

// convert number to String
const str5 = 12 + '';
console.log(typeof str5);
