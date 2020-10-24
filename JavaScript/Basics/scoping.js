'use strict';

var firstName = 'Gonzalo'

// function calcAge(birthYear) {
//     const age = 2037 - birthYear;
//     console.log(firstName);
    
//     function printAge() {
//         const output = `${firstName}, ${age}, born in ${birthYear}`;
//         console.log(output);

//         if(birthYear >= 1981 && birthYear <= 1996) {
//             var millenial = true; // var variables dont care about block scope, only const and let
//             const firstName = 'Steven'
//             const str = `Oh, and you are a millenial, ${firstName}`
//             console.log(str);

//             function add(a,b) {
//                 return a+ b;
//             }
//         }
//         // output = 'new output'
//         // console.log(str);
//         console.log(millenial);
//         // console.log(add(2,3));
//     }
//     printAge();
//     return age;
// }

// calcAge(1991);
// console.log(firstName);

const merry = {
    firstName: 'Merry',
    year: 1986,
    calcAge: function() {
        // console.log(this)
        console.log(2032 - this.year)

        // const self = this; // I can preserve the this keyword and use it in my function
        // const isMillenial = function() {
        //     console.log(self.year >= 1981 && self.year <= 1996)
        // }
        // isMillenial(); // this key is undefined here

        const isMillenial = ()=> {
            console.log(this.year >= 1981 && this.year <= 1996)
        }
        isMillenial(); // but not with arrow keys because arrow keys dont have their own this keyword
    },
    
    greet: () => {
        // console.log(this)
        console.log(`Hey ${this.firstName}`)
    }
};

merry.greet();
merry.calcAge();


const addExpr = function(a, b){
    console.log(arguments)
}   

const addArrow = (a,b) => {
    console.log(arguments);
}

// addExpr([1,2,3,4])
// addArrow([1,2,3,4,5])

let age = 30;
let oldAge = 40
age = 32

console.log(age)
console.log(oldAge);

const me = {
    age: 20,
    name: 'Gonzalo'
}

const merry1 = me;

merry1.age = 30;
console.log(me);
console.log(merry1);

let lastName = 'William'
let oldLastName = lastName
lastName = 'Davis'
console.log(lastName, oldLastName)

const jessica = {
    fName: 'Jess',
    lName: 'Williams',
    age: 27,
    family: ['Alexa', 'Aliso']
}

const marriedJess = jessica; // not a new object in heap, they both point to the same memory address reference
// marriedJess.lName = 'Davis'

console.log('Before marriage', jessica);
console.log('After marriage', marriedJess);

// copy an object --> shallow not deep copy. if I have inner objects they wont copy
const marriedJess2 = Object.assign({}, jessica)
marriedJess2.lName = 'Davis'
marriedJess2.family.push('Gonzalo')
console.log('Before marriahe', jessica);
console.log('After marriage', marriedJess2);

// Deep copy
const jessica3 = {
    fName: 'Jess',
    lName: 'Williams',
    age: 27,
    family: ['Alexa', 'Aliso']
}

