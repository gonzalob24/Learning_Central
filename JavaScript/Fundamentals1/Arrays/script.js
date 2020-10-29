'use strict';

const hours = {
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
};

const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],
  hours,
  order: function (startIndex, mainIndex) {
    return [this.starterMenu[startIndex], this.mainMenu[mainIndex]];
  },

  orderDelivery: function ({ startIndex, mainIndex, time, address }) {
    console.log(
      `Order received! ${this.starterMenu} and ${
        (this, this.mainMenu[mainIndex])
      } will be delivered at ${address} at ${time}`
    );
  },
  orderPizza: function (mainIngredients, ...otherIngredients) {
    console.log(mainIngredients);
    console.log(otherIngredients);
  },
};

restaurant.orderDelivery({
  time: '23:30',
  address: 'Via del Sole 21',
  mainIndex: 2,
  strterIndex: 2,
});

const arr = [1, 2, 3, 4];

const [w, , x] = arr;

let [first, , second] = restaurant.categories;

console.log(`${first} , ${second}`);
[first, second] = [second, first];
console.log(`${first} , ${second}`);

const [starter, mainCourse] = restaurant.order(2, 0);
console.log(`${starter} ${mainCourse}`);

const nested = [1, 2, [3, 4]];
const [i, , j] = nested;
console.log(i, j);

// destructure inside destructure
const [l, , [m, n]] = nested;
console.log(l, m, n);

// Defualt values can be indefined of not enough values to destructure

// destructure objects with {}

const { name, openingHours, categories } = restaurant;
console.log(name, openingHours, categories);

// change variable names
const { name: restName, openingHours: hours1, categories: tags } = restaurant;

console.log(restName, hours1, tags);

//
const { menu = [], starterMenu: starters = [] } = restaurant;
console.log(menu, starters);

// mutating variable while destructuing
let a = 111;
let b = 999;

const obj = { a: 23, b: 7, c: 14 };

({ a, b } = obj);
console.log(a, b);

// nested objects
const {
  fri: { open: o, close: c },
} = hours;
console.log(o, c);

// Array spread operator --> works on all iterabels --? arrays, string, maps, sets NOT Objects
const arr2 = [7, 8, 9];

const arr3 = [1, 2, ...arr2];

console.log(arr3);
console.log(...arr3);

const newMenu = [...restaurant.mainMenu, 'Gnocci'];
console.log(newMenu);

// copy array
const mainMenuCopy = [...restaurant.mainMenu];

// join 2 arrays
const joinedArray = [...restaurant.mainMenu, ...restaurant.starterMenu];
console.log(joinedArray);

const str = 'Gonzalo';
const letters = [...str, 'GG'];
console.log(letters);
const letter2 = str.split('').join();
console.log(letter2);

// Rest Pattern and Parameters --> opposite of spread--> this packs elements into an array

const [az, bz, ...others] = [1, 2, 3, 4, 5];
console.log(a, b, others);

const [pizza, , risoto, ...otherFood] = [
  ...restaurant.mainMenu,
  ...restaurant.starterMenu,
];

console.log(pizza, risoto, otherFood);

//Objects
const { sat, ...weekends } = restaurant.hours;
console.log(weekends);

const add = function (...numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
};

console.log(add(5, 3, 7, 2));

restaurant.orderPizza('mushrooms', 'onions', 'spinach');

const guests1 = restaurant.numGuests ? restaurant.numGuests : 10;
console.log(guests1);

// Nullish: null and undefined
// restaurant.numGuests = 0;
// const guestCorrect = restaurant.numGuests ?? 10
// console.log(guestCorrect);

// Looping
const menu1 = [...restaurant.starterMenu, ...restaurant.mainMenu];

for (const item of menu1) {
  console.log(menu1);
}

for (const [i, el] of menu1.entries()) {
  // console.log(item); // entries contianes the index of the current element its an iterator
  console.log(`${i + 1}: ${el}`);
}

for (const day of Object.keys(hours)) {
  console.log(day);
}

for (const day of Object.values(hours)) {
  console.log(day);
}

for (const [day, { open, close }] of Object.entries(hours)) {
  console.log(`On ${day} we are open from ${open} to ${close}.`);
}

// SETS and MAPS --> are also iterable

// Sets collection of unique values
const ordersSet = new Set(['Pasta', 'Pizza', 'Pasta', 'Risotto']);
console.log(ordersSet);
console.log(ordersSet.size);
console.log(ordersSet.has('Pizza'));
ordersSet.add('Bread');
console.log(ordersSet);

for (const i of ordersSet) {
  console.log(i);
}

//
const staff = ['Waiter', 'Chef', 'Waiter', 'manager'];

const staffUnique = new Set(staff);
console.log(staffUnique);

const staffArray = [...staffUnique];

console.log(staffArray);

// MAPS --> map key value pairs. The key can be anything

const rest = new Map();
rest.set('name', 'Classico Italiano');
rest.set(1, 'Firenze, Italy');
rest.set(2, 'Lisbon, Portugal');

rest
  .set('categories', ['italian', 'Pizzeria', 'Vegetariano', 'Organic'])
  .set('Open', 11)
  .set('close', 23)
  .set(true, 'We are open')
  .set(false, 'We are close');

console.log(rest.get('name'));
console.log(rest.get(true));
console.log(rest.get(1));

// console.log(rest);

const time = 21;
console.log(rest.get(time < rest.get('close')));

console.log(rest.has('categories'));
rest.delete(2);
// rest.clear()
const arr33 = [1, 2];
rest.set(arr33, 'Test');

const question = new Map([
  ['question', 'What is the best progamming language in the world?'],
  [1, 'C'],
  [2, 'Java'],
  [3, 'JS'],
  ['correct', 3],
  [true, 'correct \u{1F973}'],
  [false, 'incorrect \u{1F625}'],
]);

console.log(question);

// Object to map

const mapHours = new Map(Object.entries(hours));
console.log(mapHours);

for (const [key, value] of question) {
  if (typeof key === 'number') {
    console.log(`Answer ${key}: ${value}`);
  }
}

// const answer = Number(prompt('Your answer'));
// console.log(question.get(question.get('correct') === answer))

// map to array
console.log([...question]);

const airline = 'TAP Air Seattle';
const plane = 'SEA2021';

console.log(airline.indexOf('r'));
console.log(airline.slice(4, 7));

const checkMiddleSeat = function (seat) {
  // B and E are middle seats
  if (seat.slice(-1) === 'B' || seat.slice(-1) === 'E') {
    console.log('Middle seat');
  } else {
    console.log('Not middle seat');
  }
};

checkMiddleSeat('11B');
checkMiddleSeat('23C');
checkMiddleSeat('3E');

// behind the scenes js converts string to Object string
console.log(typeof new String('Gonzalo').slice(1));

console.log(airline.toLowerCase());
console.log(airline.toUpperCase());

const passanger = 'gonZAlo';

const email = 'hello@me.com';
const loginEmail = ' Hello@Me.Io \n';

const lowerEmail = loginEmail.toLowerCase();
const trimmedEmail = lowerEmail.trim();
console.log(trimmedEmail);

const price = '288,97l';
const priceUS = price.replace('l', '$').replace(',', '.');
console.log(priceUS);

const announcement = 'All passenger come to boarding door 23, boarding door 23';
// console.log(announcement.replaceAll('door', 'gate'));

const newAnnouncement = announcement.replace(/door/g, 'gate');
console.log(newAnnouncement);

const plane2 = 'A320';
console.log(plane2.includes('A320'));
console.log(plane2.startsWith('A'));
console.log(plane2.padEnd(20, '-'), '\u{1F197}');
console.log('a'.repeat(4));
