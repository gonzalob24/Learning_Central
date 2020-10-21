/*
* var vs let:
    - var allows replacing declared variable without an error let does not
    - let is block scope and its scope is only available where it was created. 

* const -- Read only variables 

* Object.freeze(obj_name) prevents adding or deleting items to object

* rest parameter (...args) --Variable number of argument
    - stored in an array

* Spread --> apply()
    - unpacks an array
    - only works in-palce

* Destructuring --> extracting values from object. Similar to tuple unpacking
    - const {key1, key2, ...} = obj_name

    - cahange variable names
    const {key1; newName, key2; newName2, ...} = obj_name

    - can be used with array to 
    - const [a,b,,,c] = [1,2,3,4,5,6,7,8,9]
    - const [f,b, ...arr] = [1,2,3,4,5,6,7,8]
    - applied direclty in function as well

* template literal `${variable}`

* funcitons inside of objects, I can remove the color

* export const add = (x,y) => {
    return x + y
}

* OR export {add, subtract} can export many at the same time

* ES5 Object and construsctors

* import {add, subtract} form './path'

* import * as name from 'path' to import everything

* export default function(x,y) { // use this if only exporting one thing, the function name is not needed
    return x + y 
}

* PROMISE
    - promise to do something, usually asynchhronously like a server request. When the request is fulfilled use the then.
    - when task completes I either fulfill the promise or fail
    - Promise is a constructor function so use new keyword to create one and takes a function as a parametes

    - HAS 3 STATES
    - 1) pending -- stuck here if I dont add a way to complete it
    - 2) Fullfilled
    - 3) rejected

    - then is executed when promise is fulfilled

*/

const { rejects } = require("assert");
const { on } = require("process");

var name = 'Gonzalo'
var name = "mary";

console.log(name)

let name2 = "Gonzalo"

// throws an error that name2 has been declared
// let name2 = "Gonzalo"

const obj = {
    key: "val",
    key2: "val2"
}

console.log(obj)
obj["key3"] = "new";
console.log(obj)

const newFunc = (arg1, arg2) => {
    console.log("New ES6")
    console.log(arg1 + " y " + arg2)
}

newFunc('Gonzalo', 'mary')

// REST
const howMany = (...args) => {
    console.log(args)
}
howMany(0,1,2,3)

// Spread()
var arr = [1,2,3,4]
var max = Math.max.apply(null, arr)
console.log(max)
// easier to write
const maxim = Math.max(...arr)
console.log(maxim)


const person = {
    name: "Me",
    sayHello() {
        return 'Hello all'
    }
}
console.log(person.sayHello())

// ES5 classes and constructor
var Space = function(name) {
    this.name = name
}
var zeus = new Space("Giant")

console.log(zeus.name)


// ES6 classes, getter, setter
class Space2 {
    constructor(name, age, symbol) {
        this.name = name;
        this.age = age;
    }
    // getter
    get god() {
        return this.name;
    }

    //setter
    set god(updateName) {
        this.name = updateName;
    }
}

const newZeus = new Space2('Golden', 3000, 'fire') // new invokes the constructor
console.log(newZeus.name)
console.log(newZeus.age)
newZeus.god = 'Gonzalo'
console.log(newZeus.name)

// PROMISE
const myPromise = new Promise((resolve, reject) => {
    let responseFroServer = true;
    if (responseFroServer) {
        resolve("Promise resolved")
    } else {
        reject("Promise rejected")
    }
});

myPromise.then(result => {
    console.log(result)
});

myPromise.catch(result => {
    console.log(result)
});