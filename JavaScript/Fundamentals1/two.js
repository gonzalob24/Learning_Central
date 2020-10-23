'use strict'

// forbids us to do certain things
// creates visible errors

// let hasDriversLicense = false

// const pastTest = true;

// if (pastTest) {
//     hasDriversLicens = true;
// }
// console.log(hasDriversLicense)

test()

// test2()

function test() {
    console.log('Declaration')
}

const test2 = function () {
    console.log('can\'t use before declaring')
}


// Arrays
// pop(), push(), shift() unshift(), name.indexOf('something'), name.includes('something')

// Objects

if(true) console.log('True')

const calcAge = birthYear => {
    return 2037 - birthYear;
}

console.log();