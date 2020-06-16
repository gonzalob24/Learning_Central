// let and const


/*
// ES5
var name5 = 'Jane Smith';
var age5 = 23;
name5 = 'Jane Miller';

console.log(name5);

// ES6
const name6 = 'Jane Smith';
let age6 = 23;
name6 = 'Jane Miller';
console.log(name6);


// ES5
function driverLicense5(passedTest) {
    if (passedTest) {
        console.log(firstName)
        var firstName = 'John';
        var BirthYear = 1990;
    }
    console.log(firstName + ', born in ' + BirthYear + ', is now officially allowed to drive a car.')

}
driverLicense5(true);

// ES6
function driverLicense6(passedTest) {
    // console.log(firstName)
    let firstName;
    const BirthYear = 1990;

    if (passedTest) {
        firstName = 'John';
    }
    console.log(firstName + ', born in ' + BirthYear + ', is now officially allowed to drive a car.')
}
driverLicense6(true);


let i = 23;
for (let i = 0; i < 5; i++) {
    console.log(i);
}
console.log('Variable outside of for loop: ' + i);

*/


/*
//////////////////////////////////////////
// Blocks and IIFEs                     //
//////////////////////////////////////////

{
    const a = 1;
    let b = 2;
    var c = 3
}

// console.log(a + b);
console.log(c);
// ESA5

(function () {
    var c = 3;
})();
// console.log(c)

*/

/*
//////////////////////////////////////////
// Strings                              //
//////////////////////////////////////////

let fName = 'John';
let lName = 'Smith';
const born = 1990;

function calcAge(year) {
    return 2020 - year;
}

// ES5
console.log('This is ' + fName + ' ' + lName + '. He was born in ' + born + '. Todday, he is ' + calcAge(born) + ' years old.');

// ES6
console.log(`This is ${fName} $lName. He was born in ${born}. Tpday, he is ${calcAge(born)} years old.`)


const n = `${fName} ${lName}`;
console.log(n.startsWith('J'));
console.log(n.endsWith('Sm'));

console.log(n.includes(' '));
console.log(`${fName} `.repeat(4));

*/


//////////////////////////////////////////
// Arrow Functions                      //
//////////////////////////////////////////

/*

const years = [1990, 1965, 1992, 1937];

// ES5 : returns a new array
var ages5 = years.map(function (current) {
    return 2016 - current;
})

console.log(ages5);


// ES6: the return key word implicit when in the same line
let ages6 = years.map((current) => 2016 - current);
console.log(ages6);

ages6 = years.map((current, index) => `Ages element ${index + 1}" ${2016 - current}`);
console.log(ages6);

ages6 = years.map((current, index) => {
    const now = new Date().getFullYear();

    const age = now - current;
    return `Ages element ${index + 1}" ${age}`;
})

console.log(ages6);

*/

//////////////////////////////////////////
// Arrow Functions 2                    //
//////////////////////////////////////////

/*
// Dont have a this variable

// ES5
var box5 = {
    color: 'Green',
    position: 1,
    clickMe: function () {
        // in method call this keyword points to that object
        // in a regular function call the this keyword points to window object
        var self = this; // use this as a work around in the function call to access the instances
        document.querySelector('.green').addEventListener('click', function () {
            var str = 'This is box number: ' + self.position + ' and it is ' + self.color;
            alert(str);
        });
    }
};
// box5.clickMe();

// ES6
var box6 = {
    color: 'Green',
    position: 1,
    clickMe: function () {
        // By using the arrow function we have access to the this keyword
        // Use this method to preserve access to the this keyword
        document.querySelector('.green').addEventListener('click', () => {
            const str = 'This is box number: ' + this.position + ' and it is ' + this.color;
            alert(str);
        });
    }
};

// box6.clickMe();

var box66 = {
    color: 'Green',
    position: 1,
    // if clickMe uses () => the arrow function will get access to the window object
    clickMe() {
        // By using the arrow function we have access to the this keyword
        // Use this method to preserve access to the this keyword
        document.querySelector('.green').addEventListener('click', () => {
            const str = 'This is box number: ' + this.position + ' and it is ' + this.color;
            alert(str);
        });
    }
};
// box66.clickMe();

function Person(name) {
    this.name = name;
};

// ES5
Person.prototype.myFriends5 = function (friends) {
    var arr = friends.map(function (friend) {
        // this key word does not point to object but to window so use arrow function
        return this.name + ' is friends with ' + friend;
    }.bind(this)); // use bind to get a copy and use the this keyword that will point to the object not window
    console.log(arr);
}

var friends = ['Bob', 'Jane', 'Mark'];

new Person('John').myFriends5(friends);

// ES6

Person.prototype.myFriends6 = function (friends) {
    var arr = friends.map((friend) => `${this.name} is friends with ${friend}`);
    console.log(arr);
}

new Person('Gonzalo').myFriends6(friends);

*/

//////////////////////////////////////////
// Destructuring                        //
//////////////////////////////////////////

/*
// Gives me a convenient way to extract data from a data structure.

// ES5

var john = ['John', 26];
// if i have many elements in an array this way will take longer to accomplish the task
var name = john[0];
var age = john[1];

// ES6
// similar to Python tuple extraction
const [name6, year6] = ['john', 26];
console.log(name6);
console.log(year6);

const obj = {
    fName: 'John',
    lName: 'Smith',
};

const { fName, lName } = obj;
console.log(fName);
console.log(lName);

// change the variable names
const { fName: a, lName: b } = obj;
console.log(a)
console.log(b);


// returns age and retirement age of a person
function calcAgeRetirement(year) {
    const age = new Date().getFullYear() - year;

    return [age, 65 - age];
};

const [age2, retirement] = calcAgeRetirement(1990);

console.log(age2);
console.log(retirement);

*/

//////////////////////////////////////////
// Array                                //
//////////////////////////////////////////

/*
// returns a nodeList
const boxes = document.querySelectorAll('.box');

// ES5
var boxesArr5 = Array.prototype.slice.call(boxes); // this returns an array

boxesArr5.forEach(function (current) {
    current.style.backgroundColor = 'dodgerblue';
})

// ES6
const boxesArr6 = Array.from(boxes); // transforms nodeList in boxes into an array
boxesArr6.forEach(current => current.style.backgroundColor = 'dodgerblue');

// Loops: use for each or map method.
// cant break or continue when using forEach or map

// ES5
// for (var i = 0; i < boxesArr5.length; i++) {

//     if (boxesArr5[i].className === 'box blue') {
//         continue;
//     } else {
//         boxesArr5[i].textContent = 'I changed to blue!'
//     }
// }

// ES6: for of method
for (const current of boxesArr6) {
    if (current.className.includes('blue')) {
        continue;
    } else {
        current.textContent = 'I changed to blue';
    }
}

// ES5

var ages = [12, 17, 8, 21, 14, 11];
var fullAge = ages.map(function (current) {
    return current >= 18;
})

console.log(fullAge);
console.log(fullAge.indexOf(true));
console.log(ages[fullAge.indexOf(true)]);

// ES6: Define index method returns index of array where callback function is true
console.log(ages.findIndex((current) => current >= 18)); // returns index where this is true
console.log(ages.find((current) => current >= 18));
*/


//////////////////////////////////////////
// Spread                               //
//////////////////////////////////////////

/*
// Good wat to expand elements of an array

function addForAges(a, b, c, d) {
    return a + b + c + d;
}

var sum = addForAges(18, 30, 12, 21);
console.log(sum);

// Now lets say I have these 4 numbers in an array
// How to pass the array in the function

// ES5
var ages = [18, 30, 12, 21];  // we can use the bind or call methods. apply method is new

/// first paramater is the this variable as in bind. It can be null since i am not interested in that
var sum5 = addForAges.apply(null, ages);

console.log(sum5);


// ES6 spread operator
const sum6 = addForAges(...ages); // ... expands array into its components

console.log('I am from ES6: ' + sum6);

const smithFamily = ['John', 'Jane', 'Mark'];
const millerFamily = ['Mary', 'Bob', 'Ann'];

const bigFamily = [...smithFamily, 'Lily', ...millerFamily];
console.log(bigFamily);

// using spread on nodeList
const h = document.querySelector('h1'); // is simpy a node
const boxes = document.querySelectorAll('.box');

const all = [h, ...boxes]; // don't need to expand h
Array.from(all).forEach((curr) => curr.style.color = 'purple');

*/

//////////////////////////////////////////
// Rest Parameter                       //
//////////////////////////////////////////

// receive values and converts them to an array
/*
// ES5 
function isFullAge5() {
    // console.log(arguments);  // its an array like structure
    var argsArr = Array.prototype.slice.call(arguments);     // convert it to an array

    argsArr.forEach(function (current) {
        console.log((2016 - current) >= 18);
    });
}

isFullAge5(1990, 1999, 1965);

// ES6 rest parameter
// ... transforms it to an array
function isFullAge6(...years) {
    // console.log(years);
    years.forEach((current) => console.log((2016 - current) >= 18));
}

isFullAge6(1990, 1999, 1965);


// spread is used in the function call
// rest is used in the function declaration



function isFullAge5(limit) {
    // console.log(arguments);  // its an array like structure
    // 1 arguments that where the slice starts, at position 1. It excludes the 0 posstion
    var argsArr = Array.prototype.slice.call(arguments, 1);     // convert it to an array

    argsArr.forEach(function (current) {
        console.log((2016 - current) >= limit);
    });
}

isFullAge5(16, 1990, 1999, 1965);

// ES6 rest parameter
// ... transforms it to an array
function isFullAge6(limit, ...years) {
    // console.log(years);
    years.forEach((current) => console.log((2016 - current) >= limit));
}

isFullAge6(16, 1990, 1999, 1965);

*/

//////////////////////////////////////////
// Default Parameter                    //
//////////////////////////////////////////

/*
// used to have preset parameters

// ES5 

function smithPerson(fName, birthYear, lName, nationality) {

    lName === undefined ? lName = 'Smith' : lName === lName;
    nationality === undefined ? nationality = 'American' : nationality = nationality;

    this.fName = fName;
    this.birthYear = birthYear;
    this.lName = lName;
    this.nationality = nationality;
}

// var john = new smithPerson('John', 1990);
// var emily = new smithPerson('Emily', 1983, 'Diaz', 'Spanish')

// ES6

function smithPerson6(fName, birthYear, lName = 'Smith', nationality = 'American') {
    this.fName = fName;
    this.birthYear = birthYear;
    this.lName = lName;
    this.nationality = nationality;
}

var john = new smithPerson6('John', 1990);
var emily = new smithPerson6('Emily', 1983, 'Diaz', 'Spanish')
*/

//////////////////////////////////////////
// Maps                                 //
//////////////////////////////////////////

// use them as hash maps: key, value data structue. The key can be anything not just strings
// maps are iterable --> can use the for each method. 

const question = new Map();

question.set('question', 'What is the official name of the latest major JavaScript version?');
question.set(1, 'ES5');
question.set(2, 'ES6');
question.set(3, 'ES2015');
question.set(4, 'ES7');
question.set('correct', 3);
question.set(true, 'Correct answer');
question.set(false, 'Wrong please try again');

// get  the value of one of the keys
console.log(question.get('question'));
// get size of the question object
// console.log(question.size);

// delete an item
if (question.has(4)) {
    // question.delete(4);
    // console.log('Key 4 is here')
}


// delete all s
// question.clear();
// question.forEach((value, key) => {
//     console.log(`This is key ${key} and it's set to ${value}`);
// });

for (let [key, value] of question.entries()) { // question returns all entries in question map
    // console.log(`This is key ${key} and it's set to ${value}`);
    if (typeof (key) === 'number') {
        console.log(`Answer ${key}: ${value}`)
    }
};

const ans = parseInt(prompt('Write the correct answer'));

console.log(question.get(ans === question.get('correct')));