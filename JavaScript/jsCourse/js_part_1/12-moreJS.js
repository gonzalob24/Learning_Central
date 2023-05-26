'use strict';

// Numbers are all stored as floating point numbers
console.log(0.1 + 0.2);

console.log(Number.parseInt('03'));
console.log(Number.parseInt('10px'));
console.log(Math.trunc(23.6));
console.log(Math.round(23.5));

// DATES
const now = new Date();
console.log(now);

console.log(new Date('Aug 04 2020 18:05:41'));
console.log(new Date('December 24, 2015'));

// UTC
console.log(new Date('2019-11-18T21:31:17.178Z'));

const future = new Date(2037, 10, 19, 15, 23);
console.log(future);
console.log(future.getFullYear());
