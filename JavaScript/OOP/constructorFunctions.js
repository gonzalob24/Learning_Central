"use strict";

// Constructor function for a person
// start with a capital letter; Arrow function will not work b.c they do not have the this keyword
const Person = function (fName, birthYear) {
  this.fName = fName;
  this.birthYear = birthYear;

  // method
  // Never create a methso inside of a constructor function
  // if we create millions of instances each instance will create its own copy
  // this will be using unecessary space
  // this.calcAge = function() {
  //     console.log(2037 - this.birthYear);
  // }
};

// 1. empty object is created with the new keyword
// 2. function is called, this = {}
// 3. new obj is linked to prototype
// 4. the obj automatically returns the  obj

// This one is not inherited b/c it is not in the prototype
Person.hey = function () {
  console.log("Hey there!!");
};
// Create a new person object
const alison = new Person("Alison", 2017);

const alexa = new Person("Alexa", 2013);

console.log("\n", alison, "\n", alexa);
console.log("\n");
// alison.calcAge();
console.log(alison instanceof Person);

// Protypes
console.log(Person.prototype);

// calcAges is added to the protoype
Person.prototype.calcAge = function () {
  console.log(2037 - this.birthYear);
};

// objects inherit via prototypal inheritance
alison.calcAge();
alexa.calcAge();

// Prototype of jonas is the prototype of Person
console.log(alison.__proto__); // where does the proto como from
//
console.log(alison.__proto__ == Person.prototype);

// Person prototype is the protoype of alison
console.log(Person.prototype.isPrototypeOf(alison));
console.log(Person.prototype.isPrototypeOf(Person));

// from alison from step 3 object is lined to protytype

Person.prototype.species = "Homo Sapiens";
console.log(alison.species, alexa.species);

// The inherited prooperties are not own properties from
// creatred objects

console.log(alison.hasOwnProperty("fName"));
console.log(alison.hasOwnProperty("species"));

console.log(alison.__proto__);
// Object.prototype its the top
console.log(alison.__proto__.__proto__);
console.log(alison.__proto__.__proto__.__proto__);

console.dir(Person.prototype.constructor);

const arr = [0, 1, 2, 3, 4, 5, 7, 7, 7, 4, 4];

console.log(arr.__proto__);
console.log(arr.__proto__ === Array.prototype);

console.log(arr.__proto__.__proto__);

// Don't get into the habbit of doing this
// because if an update uses a same name my code will break
// or if another developer uses a similar name with different actions
Array.prototype.unique = function () {
  return [...new Set(this)];
};

console.log(arr.unique());

const h1 = document.querySelector("h2");
console.dir(h1);

// Challenge exercise
const Car = function (make, speed) {
  this.make = make;
  this.speed = speed;
};

Car.prototype.accelerate = function () {
  this.speed += 10;
  console.log(this.speed);
};

Car.prototype.break = function () {
  this.speed -= 5;
  console.log(this.speed);
};

const bmw = new Car("BMW", 120);
const mercedes = new Car("Mercedes", 95);

bmw.accelerate();
mercedes.break();

//**************** INHERITANCE *************/

const Person3 = function (fName, birthYear) {
  this.fName = fName;
  this.birthYear = birthYear;
};

Person3.prototype.calcAge = function () {
  console.log(2037 - this.birthYear);
};

const Student = function (fName, birthYear, major) {
  // This is duplicate code so lets inherit form Person3
  // this.fName = fName;
  // this.birthYear = birthYear;

  // use call to inherit things from Person
  Person3.call(this, fName, birthYear);

  this.major = major;
};

// Linking prototypes to use methods
Student.prototype = Object.create(Person.prototype);

Student.prototype.introduce = function () {
  console.log(`My name is ${this.fName} and my major is ${this.major}`);
};

const james2 = new Student("James", 2020, "CSI");
console.log("James2");
james2.introduce();
console.log(`First name: ${james2.fName}`);
james2.calcAge();

// ****************** Car Class **************//

// Challenge exercise
const Car2 = function (make, speed) {
  this.make = make;
  this.speed = speed;
};

Car2.prototype.accelerate = function () {
  this.speed += 10;
  console.log(this.speed);
};

Car2.prototype.break = function () {
  this.speed -= 5;
  console.log(this.speed);
};

const EV = function (make, speed, charge) {
  // inherit
  Car2.call(this, make, speed);

  this.charge = charge;
};

// Link prototypes
EV.prototype = Object.create(Car2.prototype);

EV.prototype.chargeBattery = function (chargeTo) {
  this.charge = chargeTo;
};

EV.prototype.accelerate = function () {
  this.speed += 20;
  this.charge -= 1;

  console.log(
    `${this.make} going ${this.speed}, with a charge of ${this.charge}%`
  );
};

const tesla = new EV("Tesla", 120, 23);
tesla.accelerate();
