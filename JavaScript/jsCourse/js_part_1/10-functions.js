'use strict';

// Default parameters
const bookings = [];
const createBooking = function (
  flightNum,
  numPassengers = 1,
  price = 199 * numPassengers
) {
  const booking = {
    flightNum,
    numPassengers,
    price,
  };
  bookings.push(booking);
};

createBooking('LH123');
createBooking('LH123', 2, 800);
createBooking('LH123', 3);

console.log(bookings);

// values vs reference
// JS is all pass by value
/**
 * primitives vs objects
 */

const oneWord = function (str) {
  return str.replace(/ /g, '').toLowerCase();
};

const upperFirstWord = function (str) {
  const [first, ...others] = str.split();
  return [first.toUpperCase(), ...others].join();
};

const transformer = function (str, fn) {
  console.log(`Transformed sting: ${fn(str)}`);
};

transformer('JS is the best', upperFirstWord);

const high5 = function () {
  console.log('👋');
};

document.body.addEventListener('click', high5);

// functions that return a function
const greet = function (greeting) {
  return function (name) {
    console.log(`${greeting} ${name}`);
  };
};

const greeterHey = greet('Hey');
greeterHey('Gonzalo');

// Call and Apply
const lufthansa = {
  airline: 'Lufthansa',
  iataCode: 'LH',
  bookings: [],
  // book: function() {}
  book(flightNum, name) {
    console.log(
      `${name} booked a seat on ${this.airline} flight ${this.iataCode}${flightNum}`
    );
    this.bookings.push({ flight: `${this.iataCode}${flightNum}`, name });
  },
};

lufthansa.book(239, 'Alexa Betancourt');
lufthansa.book(239, 'Alison Betancourt');

// need to add the booking method, copy paste is not good practice
const eurowings = {
  airline: 'Eurowings',
  iataCode: 'EW',
  bookings: [],
};

const book = lufthansa.book;
// this does not work because there is no object calling the method, its a regular function call
// and regular function don't have a this keyword
// book(434, 'John Smith');

// Use CALL method --> the this keyword will now point to the correct object with Call method
book.call(eurowings, 23, 'John Doe');
console.log(eurowings);
book.call(lufthansa, 444, 'Jake Smith');
console.log(lufthansa);

const swiss = {
  airline: 'Swiss Air Lines',
  iataCode: 'LX',
  bookings: [],
};

book.call(swiss, 583, 'Mary Cooper');
console.log(swiss);

// Apply method --> receives an array of arguments
const flightData = [583, 'George Cooper'];
book.apply(swiss, flightData);
console.log(swiss);

book.call(eurowings, ...flightData);

// BIND method
// this does not call the book function
// the this keyword will always be set with eurowings
const bookEW = book.bind(eurowings);

bookEW(444, 'James Peach');
console.log(eurowings);

// can bind to specific airlines
const bookEW23 = book.bind(eurowings, 23); // when calling this we only need to pass in 1 parameter.

// with event listeners
lufthansa.planes = 300;
lufthansa.buyNewPlane = function () {
  console.log(this);
  this.planes++;
  console.log(this.planes);
};

// this does not work because the this keyword is the button
// because it it being called by the querySelector
// FIX: we need to bind to lufthansa
document
  .querySelector('.buy')
  .addEventListener('click', lufthansa.buyNewPlane.bind(lufthansa));

// partial application --> preset params

const addTax = (rate, value) => value + value * rate;

console.log(addTax(0.1, 200));

// preset the rate. First argument is the this keyword, normally it is always null
const addVAT = addTax.bind(null, 0.23);

console.log(addVAT(200));

const poll = {
  question: 'What is your favourite programming language?',
  options: ['0: JavaScript', '1: Python', '2: Rust', '3: C++'],
  // This generates [0, 0, 0, 0]. More in the next section 😃
  answers: new Array(4).fill(0),
  registerNewAnswer: function () {
    const answer = Number(
      prompt(
        `${this.question}\n ${this.options.join(
          '\n '
        )} \n (write option number)`
      )
    );
    if (typeof answer === 'number' && answer < this.answers.length) {
      this.answers[answer]++;
    }
    this.displayResults();
  },
  displayResults: function (type = 'array') {
    if (typeof type === 'string') {
      console.log(`Poll results are ${this.answers.join(', ')}`);
    } else {
      console.log(this.answers);
    }
  },
};

document
  .querySelector('.poll')
  .addEventListener('click', poll.registerNewAnswer.bind(poll));
console.log(poll.answers);

// IIFE
// this data is encapsulated
// data privacy
(function () {
  const isInThisFunctionScope = 'I am inside of IIFE';
  console.log('IIFE just ran');
})();

// console.log(isInThisFunctionScope);

// CLOSURES
/**
 * makes a function remember variables that existed after being removed from call stack
 * a function has access to the variable environment of the execution context in which it was created
 *
 * closures: the VE attached to the function
 */

const secureBooking = function () {
  let passengerCount = 0;

  return function () {
    passengerCount++;
    console.log(passengerCount);
  };
};

const booker = secureBooking();

booker();
booker();

console.dir(booker);

let f;

const g = function () {
  const a = 23;
  f = function () {
    console.log(a * 2);
  };
};

const h = function () {
  const b = 777;
  f = function () {
    console.log(b * 2);
  };
};

g();
f();
h();
console.dir(f);
f();

const boardPassengers = function (n, wait) {
  const perGroup = n / 3;
  console.log(`start boarding in ${wait} seconds`);
  setTimeout(() => {
    console.log(`we are now boarding all ${n} passengers`);
    console.log(`there are 3 groups each with ${perGroup} passengers`);
  }, wait * 1000);
};

const perGroup = 1000;
boardPassengers(180, 3);

(function () {
  const header = document.querySelector('h1');
  header.style.color = 'red';

  document.body.addEventListener('click', function (parameters) {
    header.style.color = 'blue';
  });
})();
