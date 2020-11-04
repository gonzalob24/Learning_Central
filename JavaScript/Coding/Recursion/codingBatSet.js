// Factorial

/*
    inputs: integers
    output: a product of numbers
        // Tes Cases
            4! = 4*3*2*1 = 24
            3! = 3*2*1 = 6
            1! = 1
            0! = 1
    Algorthm:
        - Get user input: Enter positive integer into function
        - make sure that the value is an int 
        - recursively compute factoria --> use test cases
    Base:
        when n is 1 or 0: return 1
    Recusrsive Case:
        when n > 1: return n * factorial (n-1)
*/

const factorial = (numb) => {
    // Base case
    if(numb === 0 || numb === 1) {
        return ;
    } else {
        return numb * factorial(numb - 1)
    }
}

// console.log(factorial(400));
// console.log(factorial(3));
// console.log(factorial(0));
// console.log(factorial(1));

/*
    BUNNY EARS
    - Each bunny has two ear --> compute total number of ears recursively
    - Input: integer --> # of bunnies

    - Output: total number of ears

    Algo:
    - enter an integer to bunnyEars(numb)
    - recursively return total number of ears
        - Base:
            // Test data
            0B = 0 ears --> base case --> return 0
            1B = 2 ears
            2B = 4 ears

        - Recursive:
            return 2 + bunnyEars(n - 1)
*/

const bunnyEars = (numb) => {
    // base case
    if(numb === 0) {
        return 0
    } else { // recursive case
        return 2 + bunnyEars(numb - 1)
    }
}

// console.log(bunnyEars(0));
// console.log(bunnyEars(2));
// console.log(bunnyEars(4));
// console.log(bunnyEars(10));

/*
    Fibonacci
    first values are 0 and 1.
    Next number is sum of previous 2 numbers.
    -input: +integer >= 1

    -Output: nth fib in the sequence
        4th number = 2 --> 0,1,1,2,3,
    Algo:
        base:
            - 1 or 2  -- return n - 1
        recursive:
            - 4 --> return fib(n-1) + fib(n-2) : previous two numbers
*/

const fibonacci = (num) => {
    // base
    if (num === 0) {
        return 0
    }
    if (num === 1) {
        return 1
    } 
    if (num === 2) {
        return num - 1
    } else {
        return fibonacci(num-1) + fibonacci(num-2)
    }
}

// console.log(fibonacci(1));
// console.log(fibonacci(2));
// console.log(fibonacci(7));

/*
    bunnyEars2
    - standing in line: even-->3 ears, odd --> 2 ears

    -input: integer value >=0
    -output: number of ears

    Algo:
        base:
            0b --> return 0
        recursive
            check if even or odd
                even --> return 3 * bunnyEars2(n - 1)
                odd -->  return 2 * bunnyEars2(n - 1)
*/

const bunnyEars2 = (num) => {
    // base
    if (num === 0) {
        return 0
    } else {
        if(num % 2 === 0) {
            return 3 + bunnyEars2(num - 1)
        } else {
            return 2 + bunnyEars2(num - 1)
        }
    }
}
// console.log(bunnyEars2(3));
// console.log(bunnyEars2(4));
// console.log(bunnyEars2(10));


/*
    Triangle
    - topmost --> 1 second --> 2, third --> 3 ...etc
    
    -input: integer >= 0 

    -output blocks in given row

    Algo:
        Base:
        - 0 --> return 0
        - 1 --> return 1
        - 2 --> return 2

        Recursive:
        - return 1 + triangle(n - 1)
*/

const triangle = (num) => {
    //base
    if (num === 0 || num === 1) {
        return num
    } else {
        return 1 + triangle(num - 1)
    }
}

// console.log(triangle(3));
// console.log(triangle(0));
// console.log(triangle(5));

/*
    sum of digits in a number 
    -input: +integer
        122
    -output: sum of indivdual integers
        --> 5

    Algo:
        - enter +integer
        - recursively compute sum
            - Base:
                0 --> return 0
                1 --> return 1
                0 to 9 --> return n
            - Recur:
                122
                return lastDigit + sumDigists(num / 10)
*/

const sumDigits = (num) =>{
    //
    if(num <= 9) {
        return num
    } else{
        return num % 10 + sumDigits(Math.trunc(num/10))
    }
}

// console.log(sumDigits(126));
// console.log(sumDigits(113));
// console.log(sumDigits(12));

const count7 = (positiveInt) => {
    // Base case
    if(positiveInt === 0) {
        return 0
    } else { // Recursion
        if(positiveInt % 10 === 7) {
            return 1 + count7(Math.trunc(positiveInt/10))
        } else {
            return count7(Math.trunc(positiveInt/10))
        } 
    }
}

// console.log(count7(1));

const count8 = (posInt) => {
    // Base case
    if(posInt === 0) {
        return 0
    } else {
        if(posInt % 100 === 88) {
            return 2 + count8(Math.trunc(posInt/10))
        } else if(posInt % 10 === 8) {
            return 1 + count8(Math.trunc(posInt/10))
        } else {
            return count8(Math.trunc(posInt/10))
        }
    }
}

// console.log(count8(8818));


const powersN = (base, n) => {
    // base
    if(n === 1) {
        return base
    } else { // recursion
        return base * powersN(base, n - 1)
    } 
}


// console.log(powersN(4, 2));
// console.log(powersN(3, 3));
// console.log(powersN(5, 5));

const countLowerX = (str) => {
    // base
    if(str === "") {
        return 0
    } else {
        if(str.charAt(0) === 'x') {
            return 1 + countLowerX(str.slice(1))
        } else {
            return countLowerX(str.slice(1))
        }
    }
    //recursion
}



// var s = 'Gonzalo'
// console.log(s.charAt(0))
// console.log(s.slice(1))

console.log(countLowerX('XxxrsxxxhgtQX'));

