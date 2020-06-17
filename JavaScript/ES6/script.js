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

/*
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
*/

//////////////////////////////////////////
// Classes                              //
//////////////////////////////////////////

/*

// Class definitions are not hoisted.
// can only add methods not properties, to classes
// ES5
// I can create this as a function expression or function declaration. It works the same way
var Person5 = function (name, birthYear, job) {
    this.name = name;
    this.birthYear = birthYear;
    this.job = job;
}

Person5.prototype.calculateAge = function () {
    var age = new Date().getFullYear() - this.birthYear;
    console.log(age);
}

var john5 = Person5('John', 1990, 'Teacher');

//////////////////////////////////////////

// ES6 using classes
class Person6 {
    constructor(name, birthYear, job) {
        this.name = name;
        this.birthYear = birthYear;
        this.job = job;
    }

    calculateAge() {
        var age = new Date().getFullYear() - this.birthYear;
        console.log(age);
    }

    // static methods are not inherited by objects that are created.
    static greeting() {
        console.log('Hey there!');
    }
}

const john6 = new Person6('John6', 1990, 'Teacher');
Person6.greeting();

*/

//////////////////////////////////////////
// Inheritance                          //
//////////////////////////////////////////

/*
// ES5
var Person5 = function (name, birthYear, job) {
    this.name = name;
    this.birthYear = birthYear;
    this.job = job;
}

Person5.prototype.calculateAge = function () {
    var age = new Date().getFullYear() - this.birthYear;
    console.log(age);
}

var Athlete5 = function (name, birthYear, job, olimpicGames, medals) {
    Person5.call(this, name, birthYear, job);
    this.olimpicGames = olimpicGames;
    this.medals = medals;
}

// Connects the two data structures
Athlete5.prototype = Object.create(Person5.prototype);

Athlete5.prototype.wonMedals = function () {
    this.medals++;
    console.log(this.medals);
}

var johnAthlete5 = new Athlete5('John', 1990, 'Swimmer', 3, 10);

johnAthlete5.calculateAge();
johnAthlete5.wonMedals();

// ES6

class Person6 {
    constructor(name, birthYear, job) {
        this.name = name;
        this.birthYear = birthYear;
        this.job = job;
    }

    calculateAge() {
        var age = new Date().getFullYear() - this.birthYear;
        console.log(age);
    }
}

class Athlete6 extends Person6 {
    constructor(name, birthYear, job, olimpicGames, medals) {
        super(name, birthYear, job);

        this.olimpicGames = olimpicGames;
        this.medals = medals;
    }

    wonMedals() {
        this.medals++;
        console.log(this.medals);
    }
}

const johnAthlete6 = new Athlete6('John', 1990, 'Swimmer', 3, 10);

johnAthlete6.calculateAge();
johnAthlete6.wonMedals();

*/

//////////////////////////////////////////
// Coding Challenge                     //
//////////////////////////////////////////

/*

Im in a small town and I am in charge of two elements
1. Parks
2. Streets

There are 3 parks and 4 streets.
All parks and streets have a name and a build year.

Boss wants a final report at the end of the year meeting.

1. Tree density of each park in the town (number of trees / park area)
2. Avg age of each towns park (sum of all ages / number of parks)
3. Name of the park that has more than 1000 tress
4. Total and avg length of the town's streets.
5. Size classification of all sreets: tiny, small, normal, big, huge. If the
    sise is unknown the default is normal
print all of the report to the console

---------PARKS REPORT------------


---------STREETS REPORT----------
*/

class Basic {
    constructor(name, yearBuilt) {
        this.name = name;
        this.yearBuilt = yearBuilt;
    }
}

class Parks extends Basic {
    constructor(name, yearBuilt, numTrees, parkArea) {
        super(name, yearBuilt);

        this.numTrees = numTrees;
        this.parkArea = parkArea;
    }
    parkName() {
        return this.name;
    }
    treeDensity() {
        return this.numTrees / this.parkArea;
    }
    parkAge() {
        let year = new Date().getFullYear();
        return year - this.yearBuilt;
    }
    trees() {
        return this.numTrees;
    }
    static avgParkAge(ages) {
        let avgAge = 0;
        for (const age of ages) {
            // console.log(age);
            avgAge += age;
        }
        return (avgAge / ages.length);
    }

    static moreTrees(number) {
        if (number.trees() > 1000) {
            return number.parkName() + ' has more than 1000 trees.';
        }
    }
}

class Streets extends Basic {
    constructor(name, yearBuilt, stLength, size = 'normal') {
        super(name, yearBuilt);

        this.stLength = stLength;
        this.size = size;

    }

    sizeClass() {
        return this.size;
    }
    static totalLength(lengthStreets) {
        let totalLength = 0;
        lengthStreets.forEach((street) => totalLength += street);

        return [totalLength, totalLength / lengthStreets.length];
    }
}

const park1 = new Parks('Green Park', 1910, 204, 0.190202);
const park2 = new Parks('National Park', 1923, 5500, 12.37);
const park3 = new Parks('Oak Park', 2007, 900, 12.17);

let ages = [park1.parkAge(), park2.parkAge(), park3.parkAge()];
let avgAge = Parks.avgParkAge(ages);

console.log(`Our 3 parks have an average age of ${avgAge} years.`);
console.log(`${park1.parkName()} has a tree density of ${park1.treeDensity()} trees per sqaure km.`);
console.log(`${park2.parkName()} has a tree density of ${park2.treeDensity()} trees per sqaure km.`);
console.log(`${park3.parkName()} has a tree density of ${park3.treeDensity()} trees per sqaure km.`);

console.log(Parks.moreTrees(park2));