let age;
var num = 10;

// const variables can't be empty
// const two;

// let is block scope and var is function scope
function sum() {
    var sum = 0;
    for (let i = 0; i < 4; i++) {
        sum += i;
    }

    return sum;
}

console.log(sum())

// operator precendence

// template literals 
console.log(`${num}`)

const strng = '1990'
console.log(Number(strng) + 18)

// Truthy and Falsy values
// Falsy --> not false but will be when converted to boolean
    // : 0, '', undefined, null, NaN
    // everything else is true

