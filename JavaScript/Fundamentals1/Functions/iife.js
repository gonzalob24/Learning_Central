'use strict'

const one = function() {
    console.log('Execute once');
}

one();

// runs without calling it, it immediately runs
(function() {
    console.log("IIFE");
    const isPrivate = 23;
})();

(() => console.log('Arrow IIFE'))();

// can't access anythhing inside of the IIFE, creates encapsulation
//

// Closure makes the function remember the variables that were origianlly created even after parent function has been executed
const secureBooking = function() {
    let passengerCount = 0

    return function() {
        passengerCount++;
        console.log(`${passengerCount} passengers`);
    }
}

const booker = secureBooking();
booker()
booker()
booker()

console.dir(booker);

let f;
const g = function() {
    const a = 23;
    f = function() {
        console.log(a * 2);
    }
}


const h = function() {
    const b = 777;
    f = function() {
        console.log(b * 2);
    }
}

g()
f()
h()
f()


// Timer example
const boardPass = function(n, wait) {
    const perGroup = n/3;
    setTimeout(function(){
        console.log(`We are now boarding all ${n} passenggers`);
        console.log(`There are 3 groups, each with ${perGroup} passengers`);
    }, wait * 1000)
    console.log(`Will satrt board in ${wait} seconds`);
}

boardPass(180,3)
    