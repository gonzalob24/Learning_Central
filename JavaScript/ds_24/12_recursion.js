//

let counter = 0;
function recursion_1() {
	if (counter > 3) {
		console.log('DONE');

		return 'done';
	}
	counter++;
	return recursion_1();
}
// why does it log undefined? because after the last call we return once the value DONE.
// the next calls don't return anything
// so return the call
console.log(recursion_1());

const factorial = (num) => {
	// base case
	if (num === 1) {
		return 1;
	}
	// recursive case
	return num * factorial(num - 1);
};

console.log(factorial(5));

// 0,1,1,2,3,5,8,13,21,34,55,89,144
// Given a number n, return the index of the Fib sequence, where the sequence is
// 8 --> 21
let counter_fib = 0;
// O(2^n)
const fib = (n) => {
	// base case
	if (n === 0) {
		return 0;
	}
	if (n === 1) {
		return 1;
	}
	if (n === 2) {
		return n - 1;
	}
	// recursive case
	return fib(n - 1) + fib(n - 2);
};

console.log(fib(3));
