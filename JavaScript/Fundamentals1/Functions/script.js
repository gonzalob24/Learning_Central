'use strict'

const bookings = []

// default parameters 
const createBooking = function(flightNum, numPassengers= 1, price=199) {
    
    const booking = {
        flightNum,
        numPassengers,
        price,
    }
    console.log(booking);
    bookings.push(booking)
}

createBooking('LH123')
createBooking('LH123', 2, 800)

// Value vs References

// const flight = 'LH234'

// const name = {
//     name: 'Gonzalo B',
//     passport:2473954654
// }

// const checkIn = function(flightNum, passenger) {
//     flightNum = 'LH777'
//     passenger.name = 'Mr. Gonzalo B'

//     if(passenger.passport === 2473954654) {
//         alert('Checking In')
//     } else {
//         alert('Wrong passport')
//     }
// }   

// checkIn(flight, name)
// console.log(flight);
// console.log(name);

// passing in the reference, location in memory heap

// First class and higher order functions
const oneWord = function(str) {
    return str.replace(/ /g, '').toLowerCase()
}

const upperWord = function(str) {
    const [first, ...others] = str.split(' ')
    return [first.toUpperCase(), ...others].join(' ')
}

const transformer= function(str, uw) {
    console.log(`original: ${str}`);
    console.log(`Transformed string: ${uw(str)}`);
    console.log(`Transformed by: ${uw.name}`);
}

transformer('js is the best', upperWord)

const hi5 = function() {
    console.log('\u{1FA96}');
}

// document.body.addEventListener('click', hi5)
const greeting1 = function(greeting) {
    return function(name) {
        console.log(`${greeting} ${name}`);
    }
}


// Functions that return other function
const greetArr = greeting => (name) => {
    return console.log(`${greeting} ${name}`);
}

greetArr('HELLO')('Merry')

// Call and Apply

const seattle = {
    airline: 'Seattle',
    code: 'SA',
    bookings: [],
    book(flightNum, name) {
        console.log(`${name} booked a seat on ${this.airline} flight ${this.code}${flightNum}`);
        this.bookings.push({flight: `${this.code}${flightNum}`, name})
    }
}

seattle.book(236, 'Gonzalo')
seattle.book(201, 'Merry')
console.log(seattle);

const euroWings = {
    airline: 'Eurowings',
    code: 'EU',
    bookings: [],
}

// store the function in a new variable to be reused later. So its a regular function call and the this keyword is now undefined 
// when used on its own
// tell js explicity where the this keyword should look like: call, apply and bind
const book = seattle.book;

// This does not work
// book(23, 'Alison')

// first argument is where the this keyword should point to
book.call(euroWings, 23, 'Alexa Torres');
console.log(euroWings);

book.call(seattle, 158, 'NZO')
console.log(seattle);

const mexico = {
    airline: 'Mexico',
    code: 'MX',
    bookings: [],
}

book.call(mexico, 658, 'Gonzalo')
console.log(mexico);

// Apply method --> doe not reciev arguments it receives an array of arguments
book.apply(mexico, [789, 'Merry Carrillo'])
console.log(mexico);

const bookingInfo = [745, 'Alexa Torres']
//
book.call(mexico, ...bookingInfo)

// Bind method --> returns a new function I like this method the most and easier to reuse
const bookEU = book.bind(euroWings)
bookEU(68, 'Gonzalo Bind')
bookEU(77, 'Merry Bind')
console.log(euroWings);

// preset the first argument for a specific flight number
const bookEU77 = book.bind(euroWings, 77)
bookEU77('Alison Preset')
console.log(euroWings);

// with event listeners
seattle.planes = 300
seattle.buyPlane = function() {
    console.log(this);
    this.planes++
    console.log(this.planes);
}

// use call or bind method. Recall that call, calls a function and bind returns a function. We need a call back function so use bind.
// document.querySelector('.buy').addEventListener('click', seattle.buyPlane.bind(seattle))

// Partial application --> means preset parameters
const addTax = (rate, value) => value + value * rate;

console.log(addTax(0.10, 200));

// Dont care about the this keyword
const addVAT = addTax.bind(null, 0.23)
// addVAT = value => value + value * 0.23

console.log(addVAT(100));


// Challenge create a function that returns a function like the example above
const funcAddTax = function(rate) {
    return function(value) {
        console.log(value + value * rate);
    }
}

const funcAddVAT = funcAddTax(0.23)
funcAddVAT(100);

// Coding challenge --> poll application
const poll = {
    question: 'What is your favorite progamming language? ',
    options: ['0: JS', '1: Python', '2: C++', '3: Java'],
    answers: new Array(4).fill(0),

    registerNewAnswer() {
        // console.log(this);
        let pollQuestion = `${this.question}`
        for(let i=0; i<this.options.length; i++) {
            pollQuestion += `\n${this.options[i]}`
        }
    
        let ans = Number(prompt(pollQuestion+="\nWrite option number"))
        while (typeof ans !== 'number' && ans >= this.answers.length) {
            ans = Number(prompt(pollQuestion))
        }
        this.answers[ans]++

        this.displayResults()
        this.displayResults('tring')
    },

    displayResults(type = 'array') {
        if (type === "array") {
            console.log(`Poll results are ${[...this.answers]}`);
        } else if (type === 'string'){
            console.log(`Poll results are ${type}`);
        }
    }
}

// poll.registerNewAnswer = function() {
//     // console.log(this);
//     let pollQuestion = `${this.question}`
//     for(let i=0; i<this.options.length; i++) {
//         pollQuestion += `\n${this.options[i]}`
//     }

//     let ans = Number(prompt(pollQuestion+="\nWrite option number"))
//     while (typeof ans !== 'number' && ans >= this.answers.length) {
//         ans = Number(prompt(pollQuestion))
//     }
//     this.answers[ans]++
// }

// poll.displayResults = function(type = 'array') {
//     if (type === "array") {
//         console.log(`Poll results are ${[...this.answers]}`);
//     } else if (type === 'string'){
//         console.log(`Poll results are ${type}`);
//     }
// }
// poll.registerNewAnswer()
console.log(poll);

// document.querySelector('.poll').addEventListener('click', poll.registerNewAnswer.bind(poll))

const testArray1 = [5,2,3]
const testArray2 = [1,5,3,9,6,1]

poll.displayResults.call({answers: testArray1})
poll.displayResults.call({answers: testArray2})