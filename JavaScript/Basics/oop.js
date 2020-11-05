// ES5 DRY eliminates errors and less work for programmers

/* 
* Own properties -- are defined directly on the object 
* Prototype properties --- are defined on the prototype 
    - The construtor propperty is a reference to the constructor function that created the instance. 
    - We can check what type of constructor it is to find out what kind of object it is. 
* 
*/

const { allowedNodeEnvironmentFlags } = require("process");
const { brotliDecompress } = require("zlib");

// this --> refers to the object that the method is associated with

let dog = {
    name: "Canelo",
    numLegs: 4,
    sayName: function() {
        return "My name is " + this.name;  // isntead of dog.name use this
    }
}

console.log(dog.sayName())

/* 
* Constructor funcion --> 
    - used to create new objects
    - define properties and behaviors that will belong to the new object -- Blueprint 
*/

// need capital letter in name
function Auto() {
    // properties
    this.model = "GMC",
    this.colo = "Red",
    this.transmission = "manual"
}

let car1 = new Auto(); // without new the this keyword would not point to the new object

// Constructors can receive names
function Dogz(name, color) {
    this.name = name;
    this.color = color;
    // this.numLegs = 4; // added this via the prototype
}

Dogz.prototype.numLegs = 4;

let bullDog = new Dogz('Canel', 'black')
console.log(bullDog.numLegs)
// Verify an objects constructor
console.log( bullDog instanceof Dogz)

// Own propertyies
console.log("Bullddog has own property name: " + bullDog.hasOwnProperty("name"))

// use prototype ro reduce duplciate code to share among instances
// So added it to the prototype 
// Dogz.prototype.numLegs = 4;
// now all instances of Dogz will not have duplicate variables numLegs and instead have access to it via the prototype

// Add prototypes in the form of an object
// Doing this manually will erase the constructor property
Dogz.prototype = {
    numLegs: 6,
    eat() {
        console.log('nom nom nom')
    },
    describe() {
        console.log("My name is " + this.name)
    }
}

const allien = new Dogz("Capi", 'Charcoal')
allien.describe()
console.log("and I like to ")
console.log(allien.constructor === Dogz)

Dogz.prototype = {
    constructor: Dogz, // set the constructor property otherwise it will be false.
    numLegs: 6,
    eat() {
        console.log('nom nom nom')
    },
    describe() {
        console.log("My name is " + this.name)
    }
}

const allien2 = new Dogz('CPI', 'Green')
console.log(allien2.constructor === Dogz)


// allien2 inherits its prototype from Dogz -- inheritance. 
console.log('Is prototype of: ' + Dogz.prototype.isPrototypeOf(allien2));

// Object.prototype is the super class for all instnace that inherit it
console.log("\n\nInheritance")

function Animal() {} // empty constructor

Animal.prototype = {
    constructor: Animal,
    eat() {
        console.log("nom nom nom")
    },
    describe() {
        console.log("My name is " + this.name)
    }
}


const animal1 = Object.create(Animal.prototype) // create an instance and inherits animals prototype
animal1.eat()
console.log(Animal.prototype.isPrototypeOf(animal1))

function Dog() {} // dog will inherit all of animals properties

Dog.prototype = Object.create(Animal.prototype)

const shep = new Dog()
console.log("Shep")
shep.eat()

// look at the constructor for shep -- comes from animal
console.log(shep.constructor)

// change shep constructor to come from Dog()
Dog.prototype.constructor = Dog;
console.log("Shep constructor now comes from: " + shep.constructor)

// Adding methods after inheritance
Dog.prototype.color = "Gray";
Dog.prototype.talk = function() {
    console.log("Bark Bark")
    
}

const shep2 = new Dog()
console.log("color: " + shep2.color)
shep2.eat()
shep2.talk();

// Override methods
Dog.prototype.eat = function() {
    return "Chop Chop Chop";
}

console.log(shep2.eat())

// Closures -- declare a variable within the constructor

function Cat() {
    let kittens = 7; // private variable

    this.getKittens = function() {
        return kittens;
    }
}

let momCat = new Cat();
console.log(momCat.getKittens());

// IIFE
(function() {
    console.log("I am executed without being called")
})();