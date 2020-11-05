"use strict";

/*

*/
// Class Declaration
// const Person = class {

// }

// Expression
class Person {
  constructor(fName, birthYear) {
    this.fName = fName;
    this.birthYear = birthYear;
  }

  // these become part of the prototype property of the
  // Person class
  calcAge() {
    console.log(2037 - this.birthYear);
  }

  greet() {
    console.log(`Hey ${this.fName}`);
  }

  get age() {
    return 2037 - this.birthYear;
  }

  set fullName(name) {
    if (name.includes(" ")) {
      this._fName = name;
    } else alert(`${name} is not a ful name`);
  }

  static hey() {
    console.log("Hey there!!");
  }
}

const fonzi = new Person("Fonzi", 1996);
console.log(fonzi);

fonzi.calcAge();
console.log(fonzi.age);
console.log(fonzi.__proto__ == Person.prototype);

// recall we can add methods this way
Person.prototype.greet = function () {
  console.log(`Hey ${this.fName}`);
};

fonzi.greet();

fonzi.fullName = "Fonzi Great";
console.log(fonzi);

const gonzalo = new Person("Gonzaloeww", 1990);
console.log(gonzalo);
// 1. Classes are not hoisted -- need to declare them before using
// 2. Classes ae first-class citizens
// 3 . Classes are executed in strict mode

// Getters and Setters --> Accessors

const account = {
  owner: "Jonas",
  movements: [200, 530, 120, 300],

  // without calling the function
  get latest() {
    return this.movements.slice(-1).pop();
  },

  set latest(mov) {
    this.movements.push(mov);
  },
};

console.log(account.latest);
account.latest = 50;
console.log(account.movements);

Person.hey();

// object.create

const PersonProto = {
  calcAge() {
    console.log(2037 - this.birthYear);
  },

  init(fName, birthYear) {
    this.fName = fName;
    this.birthYear = birthYear;
  },
};

// linked PersonProto object
// Creates a new object
const steve = Object.create(PersonProto);

console.log(steve);
steve.name = "steve";
steve.birthYear = 1990;

steve.calcAge();
console.log(steve.__proto__ == PersonProto);

const james = Object.create(PersonProto);
james.init("James", 1979);
console.log(james);
james.calcAge();

//
class Car2 {
  constructor(model, speed) {
    this.model = model;
    this.speed = speed;
  }

  accelerate() {
    this.speed += 10;
  }

  break() {
    this.speed -= 10;
  }
  get speedUS() {
    return this.speed / 1.6;
  }

  set speedUS(speedUS) {
    this.speed = speedUS * 1.6;
  }
}

const ford = new Car2("Ford", 120);
console.log(ford.speedUS);
ford.speedUS = 50;
console.log(ford.speed);

// ************* INHERITANCE ******* ////
// extends links prototypes
class Student extends Person {
  constructor(fName, birthYear, major) {
    // super is responsible for the this keyword
    super(fName, birthYear);
    this.major = major;
  }

  introduce() {
    console.log(`My name is ${this.fName} and my major is ${this.major}.`);
  }
}

const mike = new Student("Mike Jones", 1990, "Bio");
console.log(mike);
mike.introduce();
mike.calcAge();
