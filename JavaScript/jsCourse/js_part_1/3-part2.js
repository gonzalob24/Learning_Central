// activate strict mode to help avoid errors
'use strict';

let hasDriversLicense = false;

const passTest = true;

// if (passTest) hasDriverLicense = true;

// Functions --> are ust values. function(){} returns an anonymous function that we can assign to a variable
// can hold 1 or more lines of code

// function declaration --> I can call these functions before they are declared. These are hoisted
function logger() {
  console.log('My name is Gonzalo');
}

logger(); // calling the functions, invoking, running

// pass parameters to the function
function fruitProcessor(apples, oranges) {
  console.log(apples, oranges);
  const juice = `Juice with ${apples} apples and ${oranges} oranges`;

  return juice;
}

console.log(fruitProcessor(2, 3));

function calAge1(birthYear) {
  const age = 2037 - birthYear;
  return age;
}

// I PREFER THIS
// function expressions --> cannot be accessed before they are initialized
const calcAge2 = function (birthYear) {
  const age = 2037 - birthYear;
  return age;
};

// OR THIS --> Arrow functions doe not bind to the this keyword. Function declarations bind to the this keyword
const calcAge3 = (birthYear) => 2037 - birthYear;

const calcAge4 = (birthYear) => {
  const age = 2037 - birthYear;
  return age;
};

const yearsUntilRetirement = (birthYear, firstName) => {
  const age = 2037 - birthYear;
  const retirementAge = 65 - age;

  // return retirementAge;
  return `${firstName} retires in ${retirementAge} years`;
};

console.log(yearsUntilRetirement(1991, 'Gonzalo'));

// function calling other Functions

// Challenge
const calAverage = (score1, score2, score3) => {
  return (score1 + score2 + score3) / 3;
};

const dolphinsAvg1 = calAverage(44, 23, 71);
const koalasAvg1 = calAverage(65, 54, 59);

if (dolphinsAvg1 >= koalasAvg1 * 2) {
  console.log('dolphins win');
} else if (koalasAvg1 >= dolphinsAvg1 * 2) {
  console.log('Koalas win');
} else {
  console.log('No one wins!');
}

// Arrays

const friends = ['Mike', 'Jones'];

// I don't have to create an array this way, I can use the literal syntax
const years = new Array(1991, 1992, 1993);
const year2 = [1991, 1992, 1993];

// Array methods
// add to the end
years.push(2037); // push is a method on any array
// add to the beginning
years.unshift(1986);

console.log(years);

// Remove
years.pop(); // last element
years.shift(); // first element

console.log(years);

console.log(years.indexOf(1992));
console.log(year2.includes(1991));

// Challenge

const calcTip = (bill) => {
  return bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
};

console.log(calcTip(400));

const bill = [125, 555, 44];
const tips = [];

tips.push(calcTip(125));
tips.push(calcTip(555));
tips.push(calcTip(44));

console.log(tips);

// Objects
const myArray = [
  'Gonzalo',
  'Bet',
  2037 - 1993,
  'SWENG',
  ['Maria', 'Alexa', 'Alison'],
]; // order matters
const myObject = {
  firstName: 'Gonzalo',
  lastName: 'Bet',
  age: 2037 - 1993,
  job: 'SWENG',
  family: ['Maria', 'Alexa', 'Alison'],
  hasDL: true,
  birthYear: 1993,
  // dont need to pass in the birthYear I can access the myObject using "this" keyword
  // calcAge: function (birthYear) {
  // 	return 2037 - birthYear;
  // },
  //
  // this function has the this keyword, arrow functions don't
  // calcAge: function () {
  // 	console.log('this is the object: ', this);
  // 	return 2037 - this.birthYear;
  // },
  // I can create new properties as well
  calcAge: function () {
    console.log('this is the object: ', this);
    this.ageCreated = 2037 - this.birthYear;
    return this.ageCreated;
  },

  summary: function () {
    return `${this.firstName} is a ${this.age}-year old ${this.job}, and ${
      this.hasDL ? 'has' : "doesn't have"
    } a DL.`;
  },
}; // order does not matter
console.log(myObject);

// access with dot or bracket notation
myObject.location = 'MI, USA';

console.log(myObject.calcAge());
console.log(myObject.summary());

const john = {
  fullName: 'John Doe',
  mass: 92,
  height: 1.95,
  calcBMI: function () {
    this.bmi = this.mass / this.height ** 2;
    return this.bmi;
  },
};

const mark = {
  fullName: 'Mark Doe',
  mass: 78,
  height: 1.69,
  calcBMI: function () {
    this.bmi = this.mass / this.height ** 2;
    return this.bmi;
  },
};

const higherBMI =
  john.calcBMI() > mark.calcBMI()
    ? `John has the higher BMI with ${john.bmi}`
    : `Mark has the higher BMI with ${mark.bmi}`;

console.log(higherBMI);

function test() {
  let sum = 3 + 3;
}

const testHere = test();

console.log(testHere); // this will be undefined because it does not have a return statement
console.log(Number('007'));
console.log(parseInt('007'));
console.log(parseInt('10011', 2));

BUG: FIXME: TODO:;

// copy. This only works on the first level
// inner objects will not copy --> this creates a shallow copy
mark.family = ['Alison', 'Alexa'];
const copyMark = Object.assign({}, mark);
copyMark.isMarried = true;
copyMark.family.push('Mary');
console.log(mark);
console.log(copyMark);

// deep copy --> copy all levels use lodash external library
//
// const deepCopMark = { ...mark };
const deepCopMark = JSON.parse(JSON.stringify(mark));
mark.family.push('Test');
console.log(deepCopMark);
