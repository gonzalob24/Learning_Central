'use strict';

///////////////////////////////////////
// Constructor Functions and the new Operator

const Person = function (name, birthYear) {
  console.log(this);
  // instance properties
  this.name = name;
  this.birthYear = birthYear;

  // don't create methods like this
  //because if we create 100, 1000s of objects each object would carry around this object. We would create 100, 1000s of copies
  // this.calcAge = function () {
  //   console.log(2037 - this.birthYear);
  // };

  console.log(this);
};

const me = new Person('Gonzalo', 1991);

// using the new keyword
// 1. New empty object is created {}
// 2. Function is called, this = {}
// 3. {} is linked to a prototype, this creates __proto__ value and sets it equal to Person.prototype
// 4. function automatically returns {} at this point {} may no longer be empty

const matilda = new Person('Matilda', 2017);

const jack = new Person('Jack', 1975);

console.log(me instanceof Person);

///////////////////////////////////////
// Prototypes
// each function in js has a prototype
// every object created by constructor function will have access to prototype
// will have access to all methods to prototype property
console.log('========= PROTOTYPES ========');
console.log(Person.prototype);

// the calcAge instance method is created only once and all instances of Person will have access to this method and any method that we create
Person.prototype.calcAge = function () {
  console.log(2037 - this.birthYear);
};
// all instances have access to __proto__
console.log('me __prop__: ' + me.__proto__);
// prototype of Person.prototype is not the prototype of person
// but Person.prototype is what we use and will be the prototype of any
// instance that is created.
console.log(
  'me.__proto__ == Person.prototype: ',
  me.__proto__ === Person.prototype
);

Person.prototype.species = 'Homo Sapiens';

console.log(me.hasOwnProperty('name'));
console.log(me.hasOwnProperty('species'));

console.log(me.__proto__);
console.log(me.__proto__.__proto__);
console.log(me.__proto__.__proto__.__proto__);

console.dir(Person.prototype.constructor);

const arr = [1, 2, 3, 4];
console.log(arr.__proto__ === Array.prototype);

// adding methods to all instances of Array
Array.prototype.unique = function () {
  return [...new Set(this)];
};

const Car = function (make, speed) {
  this.make = make;
  this.speed = speed;
};

const bmw = new Car('BMW', 120);
const mercedes = new Car('Mercedes', 95);

Car.prototype.accelerate = function () {
  this.speed += 10;
  console.log(`${this.make} is going ${this.speed}m/h`);
};

Car.prototype.break = function () {
  this.speed -= 5;
  console.log(`${this.make} is going ${this.speed}m/h`);
};

bmw.accelerate();
mercedes.accelerate();
console.dir('CAR ----> ');
console.dir(Car);
///////////////////////////////////////
// ES6 Classes

// class expression
const PersonCL = class {};

// class declarations
// 1. classes are not hoisted
// 2. classes are first class citizens
// 3. classes are executed in strict mode

class PersonCl {
  constructor(fullName, birthYear) {
    // Object.defineProperty(this, fullName);
    // Object.defineProperty(this, birthYear);
    this.fullName = fullName;
    this.birthYear = birthYear;
  }

  // these methods will added to the prototype
  // and not on each instance
  calcAge() {
    console.log(2037 - this.birthYear);
  }

  // getters and setters
  get age() {
    return 2037 - this.birthYear;
  }

  // set a property that already exists
  // fullName2(name) {
  //   if (name.includes(' ')) {
  //     this._fullName = name;
  //   } else {
  //     alert('Given name is not a full name');
  //   }
  // }

  get name() {
    return this.fullName;
  }
  // instance methods added to prototype
  nameInstance() {
    return 'I am instance method';
  }
  // static methods not available on instances
  static nameStatic() {
    console.log('static hey');
  }
}

// constructor gets called when we use the new keyword
const jessica = new PersonCl('Jessica Davis', 1996);
console.log(jessica);
jessica.calcAge();
console.log('age: ', jessica.age);
console.log('name: ', jessica.fullName);
console.log('static is on class', PersonCl.nameStatic());
console.log('instance is on instance object: ', jessica.nameInstance());
console.log(jessica.__proto__ === PersonCl.prototype);

PersonCl.prototype.greet = function () {
  console.log(`Hey ${this.fullName}`);
};

jessica.greet();

const account = {
  owner: 'Jonas',
  movements: [200, 530, 120, 300],

  get latest() {
    return this.movements.slice(-1).pop();
  },

  set latest(mov) {
    this.movements.push(mov);
  },
};

console.log(jessica);

console.log(account.latest);
account.latest = 50;
console.log(account.movements);

///////////////////////////////////////
// Object.create
// used to manually set prototype to any object
console.log('---------Object.create---------');

const PersonProto = {
  calcAge() {
    console.log(2037 - this.birthYear);
  },

  init(firstName, birthYear) {
    this.firstName = firstName;
    this.birthYear = birthYear;
  },
};

const steven = Object.create(PersonProto);
console.log(steven);
steven.name = 'Steven';
steven.birthYear = 2002;
steven.calcAge();

const sara = Object.create(PersonProto);
sara.init('Sara', 1979);
console.log(sara);
sara.calcAge();

///////////////////////////////////////
// Coding Challenge #2

class CarCl {
  constructor(type, speed) {
    this.make = type;
    this.speed = speed;
  }

  accelerate() {
    this.speed += 10;
    console.log(`${this.make} is going at ${this.speed} km/h`);
  }

  brake() {
    this.speed -= 5;
    console.log(`${this.make} is going at ${this.speed} km/h`);
    return this;
  }

  get speedUS() {
    return this.speed / 1.6;
  }
  set speedUS(newSpeed) {
    this.speed = 1.6 * newSpeed;
  }
}

const ford = new CarCl('Ford', 120);
console.log(ford.speedUS);
ford.accelerate();
ford.accelerate();
ford.brake();
ford.speedUS = 50;
console.log(ford);

///////////////////////////////////////
// Inheritance Between "Classes": Constructor Functions

const Person2 = function (firstName, birthYear) {
  this.firstName = firstName;
  this.birthYear = birthYear;
};

Person2.prototype.calcAge = function () {
  console.log(2037 - this.birthYear);
};

const Student = function (firstName, birthYear, course) {
  // this student has similar properties as Person2
  Person2.call(this, firstName, birthYear);
  // this.firstName = firstName;
  // this.birthYear = birthYear;
  this.course = course;
};

// Linking prototypes to inherit the methods in Person2 object
Student.prototype = Object.create(Person2.prototype); // at this point Student is {} empty

Student.prototype.introduce = function () {
  console.log(`My name is ${this.firstName} and I study ${this.course}`);
};

const mike = new Student('Mike', 2020, 'Computer Science');
mike.introduce();
mike.calcAge();
console.log('mike: ', mike);

console.log(mike.__proto__);
console.log(mike.__proto__.__proto__);

console.log(mike instanceof Student);
console.log(mike instanceof Person2);
console.log(mike instanceof Object);

Student.prototype.constructor = Student; // to have the correct constructor
console.dir(Student.prototype.constructor);

///////////////////////////////////////
// Coding Challenge #3
const EV = function (make, speed, charge) {
  Car.call(this, make, speed);
  this.charge = charge;
};

// link the prototype and constructor
EV.prototype = Object.create(Car.prototype);
EV.prototype.constructor = EV;
console.log('EV constructor');
console.dir(EV);
console.dir(EV.prototype.constructor);

EV.prototype.chargeBattery = function (chargeTo) {
  this.charge = chargeTo;
};

EV.prototype.accelerate = function () {
  this.speed += 20;
  console.log(
    `Tesla going at ${this.speed} km/h, with a charge of ${this.charge}`
  );
};

EV.prototype.brake = function () {
  this.speed -= 5;
  this.charge -= 1;
  console.log(
    `Tesla going at ${this.speed} km/h, with a charge of ${this.charge}`
  );
};

const tesla = new EV('Tesla', 120, 23);
tesla.chargeBattery(90);
tesla.brake();
tesla.accelerate();
console.log(tesla);

///////////////////////////////////////
// Inheritance Between "Classes": ES6 Classes
console.log('------------Classes------------');

class Persona {
  constructor(fullName, birthYear) {
    this.fullName = fullName;
    this.birthYear = birthYear;
  }

  // Instance methods
  calcAge() {
    console.log(2037 - this.birthYear);
  }

  greet() {
    console.log(`Hey ${this.fullName}`);
  }

  get age() {
    return 2037 - this.birthYear;
  }

  set fullName(name) {
    if (name.includes(' ')) this._fullName = name;
    else alert(`${name} is not a full name!`);
  }

  get fullName() {
    return this._fullName;
  }

  // Static method
  static hey() {
    console.log('Hey there 👋');
  }
}

// inheritance
class Estudiante extends Persona {
  constructor(fullName, birthYear, course) {
    // super is constructor function of parent class
    // this needs to happen first
    super(fullName, birthYear);
    this.course = course;
  }

  introduce() {
    console.log(`My name is ${this.fullName} and I study ${this.course}`);
  }

  // this method was overwritten
  calcAge() {
    console.log(
      `I'm ${
        2037 - this.birthYear
      } years old, but as a student I feel more like ${
        2037 - this.birthYear + 10
      }`
    );
  }
}

const martha = new Estudiante('Martha Jones', 2012, 'Computer Science');
martha.introduce();
martha.calcAge();

// class fields, truly private fields
// fields are always part of the instance
// public fields
// private fields
// public methods
// private methods
// static public
// static private

class Account {
  // public fields
  local = navigator.language;

  // private fields
  #movements = [];
  #pin;

  constructor(owner, currency, pin) {
    this.owner = owner;
    this.currency = currency;
    // _ protects the field, its a convention not truly protected
    this.#pin = pin;
    // this._movements = [];
    // this.local = navigator.language;

    console.log('Thanks for opening an account');
  }

  // public methods
  getMovements() {
    return this.#movements;
  }

  withdraw(value) {
    this.deposit(-value);
    return this;
  }

  deposit(value) {
    this.#movements.push(value);
    return this;
  }

  requestLoan(val) {
    if (this.#approveLoan) {
      this.deposit(val);
      console.log('Loan approved');
    }
    return this;
  }

  getLang() {
    return this.local;
  }

  // static public
  static helper() {
    console.log('static helper');
    this.#helperTwo();
  }

  // static private
  static #helperTwo() {
    console.log('static private helper');
  }

  // private methods, by convention we used _name
  #approveLoan(val) {
    return true;
  }
}

const acc1 = new Account('Jonas', 'EUR', 1111);
Account.helper();
// Account.#helperTwo();
// acc1.#movements.push(-1999);
acc1.deposit(250);
acc1.withdraw(-140);
acc1.requestLoan(1000);
// acc1.approveLoan(1000);
console.log(acc1.getMovements());
console.log('acc1 lang: ' + acc1.getLang());
// for this to work methods must return this (acc)
acc1.deposit(3).deposit(400).withdraw(35).requestLoan(25000).withdraw(230);
console.log(acc1.getMovements());

class EVCl extends CarCl {
  #charge;
  constructor(make, speed, charge) {
    super(make, speed);
    this.#charge = charge;
  }

  chargeBattery(chargeTo) {
    this.#charge = chargeTo;
    return this;
  }

  accelerate() {
    this.speed += 20;
    this.#charge -= 1;
    console.log(
      `${this.make} is going at ${this.speed} km/h, with a charge of ${
        this.#charge
      }`
    );
    return this;
  }
}

const rivian = new EVCl('Rivian', 120, 23);
console.log(rivian);
// console.log(rivian.#charge);
rivian
  .accelerate()
  .accelerate()
  .accelerate()
  .brake()
  .chargeBattery(50)
  .accelerate();

console.log(rivian.speedUS);
