function addTo80(n) {
	return n + 80;
}
// if this operation takes a long time we have to wait for it every time we use it
// this is a good way to use memoization
// console.log(addTo80(5));

// don't add the cache to global scope. Use closures instead
// let cache = {};

function memoizedAddTo80() {
	let cache = {};
	// closures, function returns a function
	return function (n) {
		// check if solution was cached, saved, added to cache object
		if (n in cache) {
			return cache[n];
		} else {
			console.log('Long time');
			cache[n] = addTo80(n);
			return cache[n];
		}
	};
}

const memoized = memoizedAddTo80();
// console.log('One: ', memoizedAddTo80(5));
// console.log('Two', memoizedAddTo80(5));
console.log(memoized(5));
console.log(memoized(5));

// example: O(2^n) for fib due to recursion
// make it more efficient: O(n) with dynamic programming
var calculations = 0;
const fib = (n) => {
	calculations++;
	if (n < 2) {
		return n;
	}
	return fib(n - 1) + fib(n - 2);
};

// top down approach
var mem_calc = 0;
const memoized_fib = () => {
	let cache = {};
	return function fib2(n) {
		mem_calc++;
		if (n in cache) {
			return cache[n];
		} else {
			if (n < 2) {
				return n;
			} else {
				cache[n] = fib2(n - 1) + fib2(n - 2);
				return cache[n];
			}
		}
	};
};

// bottom up approach
// this avoids recursion
const fib_master = () => {
	// start with a simple solution and work your way up
	let answer = [0, 1];
	for (let i = 2; i <= n; i++) {
		answer.push(answer[i - 2] + answer[i - 1]);
	}
	return answer.pop();
};

console.log('FIB');
console.log(fib(35), calculations);
// console.log(fib(7), calculations);
// console.log(fib(30), calculations);
console.log('MEM FIB');
const mem_fib = memoized_fib();
console.log(mem_fib(35), mem_calc);
