let array = ['today', 'was', 'not', 'so', 'great'];

// const splice_idx2_2items = array.splice(2, 2);
//
// const splice_idx2_2items_replace2 = array.splice(2, 2, 'yes', 'way');
//
// console.log('splice1', splice_idx2_2items);
// console.log(array);


// copy with slice

const copy2 = array.slice(0, 2);
const copyAll = [...array]
console.log(copy2)
console.log('Copy all: ', copyAll)

const combine = ['what', ...array, 'ney']
console.log(combine)


const foods = {
    apples: 25,
    oranges: 32,
    plums: 28,
    bananas: 13,
    grapes: 35,
    strawberries: 27
};

console.log(foods);

delete foods.plums;
console.log(foods);

console.log(foods.hasOwnProperty('apples'));

const objectKeys = Object.keys(foods);
const objentries = Object.entries(foods);
console.log('keys: ', objectKeys);
console.log('objCreate: ', objentries);

function Cat(name) {
    this.name = name;
}

Cat.prototype = {
    constructor: Cat,
};

function Bear(name) {
    this.name = name;
}

Bear.prototype = {
    constructor: Bear,
};

function Animal() { }

Animal.prototype = {
    constructor: Animal,
    eat: function() {
        console.log("nom nom nom");
    }
};

const bear1 = new Animal("bear1");
bear1.eat();

//  compare the two methods of creating an instance
let animal1 = new Animal();
let animal2 = Object.create(Animal.prototype);

// set prototype of Bird to instance of Animal
Bear.prototype = Object.create(Animal.prototype);

const brownBear = new Bear("Brown");
brownBear.eat();
// should be Bear
console.log(brownBear.constructor);


// set the constructor property of Bear
Bear.prototype.constructor = Bear;

console.log(brownBear.constructor);

/*
function Animal() { }
Animal.prototype.eat = function() {
  console.log("nom nom nom");
};
function Bird() { }
Bird.prototype = Object.create(Animal.prototype);
Bird.prototype.constructor = Bird;

// add methods to Bird
Bird.prototype.fly = function() {
  console.log("I'm flying!");
};
 */
