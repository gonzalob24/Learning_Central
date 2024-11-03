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

console.log('Binary Search');

const binary_search = (sorted_array, item) => {
	let left = 0;
	let right = sorted_array.length - 1;
	return _bs(sorted_array, left, right, item);
};

const _bs = (sorted_array, l, r, item) => {
	if (l <= r) {
		let mid = Math.floor((l + r) / 2);
		console.log(l, r, mid);
		if (sorted_array[mid] === item) {
			return mid;
		} else if (sorted_array[mid] < item) {
			return _bs(sorted_array, mid + 1, r, item);
		} else {
			return _bs(sorted_array, l, mid - 1, item);
		}
	}
	return -1;
};

const binarySearch = (nums, left, right, target) => {
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		const foundVal = nums[mid];
		if (foundVal === target) {
			return mid;
		} else if (foundVal < target) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}

	return -1;
};

const custom_bs = (sorted_array, item) => {
	let mid = _bs(sorted_array, 0, sorted_array.length - 1, item);
	if (mid === -1) {
		return [-1, -1];
	}
	let start_pos = mid;
	let end_pos = mid;
	let l_temp = null;
	let r_temp = null;

	while (start_pos !== -1) {
		l_temp = start_pos;
		// start_pos = binarySearch(sorted_array, 0, start_pos - 1, item);
		start_pos = _bs(sorted_array, 0, start_pos - 1, item);
	}
	start_pos = l_temp;

	while (end_pos !== -1) {
		r_temp = end_pos;
		// end_pos = binarySearch(sorted_array, end_pos + 1, sorted_array.length - 1, item);
		end_pos = _bs(sorted_array, end_pos + 1, sorted_array.length - 1, item);
	}
	end_pos = r_temp;
	return [start_pos, end_pos];
};

const arr = [10, 12, 13, 14, 15, 16, 71];
const arr2 = [1, 3, 3, 5, 5, 5, 8, 9];
// console.log(binary_search(arr, 13));

console.log('custom BS');

console.log(custom_bs(arr2, 3));
