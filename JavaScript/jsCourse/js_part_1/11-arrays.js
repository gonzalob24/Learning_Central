'use strict';

// array methods
let arr = ['a', 'b', 'c', 'd', 'e'];

// SLICE
console.log(arr.slice(2));
console.log(arr.slice(2, 4));
console.log(arr.slice(-2));

// SPLICE, (position, how many elements)
// mutates array
// console.log(arr.splice(2));
arr.splice(-1);
arr.splice(1, 2);
console.log(arr);

// REVERSE
arr = ['a', 'b', 'c', 'd', 'e'];
const arr2 = ['j', 'i', 'h', 'g', 'f'];
console.log(arr2.reverse()); // mutates array
console.log(arr2);

// CONCAT array
const letters = arr.concat(arr2);
console.log(letters);
// another to do this with
console.log([...arr, ...arr2]);

// JOIN
console.log(letters.join('-'));

// The new at Method
const arr3 = [23, 11, 64];
console.log(arr3[0]);
console.log(arr3.at(0));
console.log(arr3.at(-1));

///////////////////////////////////////
// Looping Arrays: forEach
// continue and breaks don't work here
// will need to use for of or regular for loop
const movements = [200, 450, -400, 3000, -650, -130, 70, 1300];

movements.forEach(function (movement, i) {
  if (movement > 0) {
    console.log(`Movement ${i + 1} you deposited ${movement}`);
  } else {
    console.log(`Movement ${i + 1} You withdrew ${Math.abs(movement)}`);
  }
});

///////////////////////////////////////
// forEach With Maps and Sets
// Map
const currencies = new Map([
  ['USD', 'United States dollar'],
  ['EUR', 'Euro'],
  ['GBP', 'Pound sterling'],
]);
const [i, j, k] = currencies.entries(); // can use a for of
console.log(i, j, k);

currencies.forEach(function (value, key, map) {
  console.log(`${key}: ${value}`);
});

const currenciesUnique = new Set(['USD', 'GBP', 'USD', 'EUR', 'EUR']);
console.log(currenciesUnique);

// _ means a throw away variable, variable that is not needed
currenciesUnique.forEach(function (value, _, set) {
  // key and value are the same because Sets don't have keys
  // console.log(`${key}: ${value}`);
});
