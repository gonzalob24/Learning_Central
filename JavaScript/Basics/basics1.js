/* JS is case sensitive **********

* different data types: 
    undefined, null, boolean, 
    string, symbol, bigint, number, object

* declared variables have an initial value of undefined --> operation on it are NaN
* const needs to be initializd
*  
* ARRAYS --
    - pop() -- remove from the end
    - push() -- append to the end 
    - shift() -- removed the first element
    - unshift() -- add element to front of array

* FUNCTIONS -- recall return ends execution

* IF / ELSE IF / ELSE --> use logical statements

* == and === (strictly) value and type !== (strictly not equal to)
* && --- ||

* switch code -- somse cases can have the same values
    switch(case) {
        case '':
            stment
            break;
        . :
        . :
        . :
        default:
            stmt;
            break;
    }

* 
*/
// The variables ar GLOBAL SCOPE
var var1;
// const var2;

var num1 = 4;
const str1 = 'Gonzalo';
console.log(var1)
console.log(num1--)
console.log(2.0 * 1.55)
console.log(str1.split('').join('-'))

// FUNCTIONS --> make them reusable should do one specific task not many
function name(arg1, arg2) {
    // Local scope variables declared inside functions
    var num1 = 0;
    // code in here

    // return values if applicable
    return num1
}

// Returns undefined because the functions does not have anything to return
function nothing(num) {
    var sum  = 1 + num;
}

console.log(nothing(3))