'use-strict';
const strings = ['a', 'b', 'c', 'd'];

strings.splice(2, 0, 'allen');

console.log(strings);

// ≠
var object_1 = { value: 10 };
var object_2 = object_1;
var object_3 = { value: 10 };
console.log(object_1 === object_2);
console.log(object_1 === object_3);
object_1.value = 15;
console.log(object_2.value);
console.log(object_3.value);

// scope vs context (this keyword)
// this refers to the object environment
function b() {
	let a = 4;
}

console.log(this);

const object_4 = {
	name: 'Gonzalo',
	a: function () {
		console.log(this.name);
	},
};

object_4.a();

// classes overview
class Player {
	constructor(name, type) {
		console.log('PLAYER', this);
		this.name = name;
		this.type = type;
	}

	introduce() {
		console.log(`Hi I am a ${this.name}, I'm a ${this.type}`);
	}
}

class Wizard extends Player {
	constructor(name, type) {
		// calls ths constructor of the parent
		// console.log('WIZARD', this);
		super(name, type);
		console.log('WIZARD', this);
	}
}

const wizard_1 = new Wizard('Alexa', 'Teacher');
// const wizard_2 = new Wizard('Alison', 'Warrior');

wizard_1.introduce();
// wizard_2.introduce();

// Building and Array

class SomeArray {
	constructor() {
		this.length = 0;
		this.data = {};
	}

	get(index) {
		return this.data[index];
	}

	push(item) {
		this.data[this.length] = item;
		this.length++;
		return this.length;
	}

	pop() {
		const last_item = this.data[this.length - 1];
		delete this.data[this.length - 1];
		this.length--;
		return last_item;
	}

	delete(index) {
		const item = this.data[index];
		this.shift_items(index);
		this.length--;
	}

	shift_items(index) {
		for (let i = index; i < this.length - 1; i++) {
			this.data[i] = this.data[i + 1];
		}

		delete this.data[this.length - 1];
		this.length--;
	}
}

const ar_1 = new SomeArray();
ar_1.push('Alexa');
ar_1.push('Alison');
console.log(ar_1.get(0));
ar_1.pop();
console.log(ar_1);

function reverse(str) {
	var reversed_string = '';
	if (!str || str.length < 2 || typeof str !== 'string') {
		return `Can't reverse`;
	}

	for (let i = str.length - 1; i >= 0; i--) {
		reversed_string += str[i];
	}
	return reversed_string;
}

function reverse_2(str) {
	return str.split('').reverse().join('');
}

const reverse_3 = (str) => str.split('').reverse().join('');

const reverse_4 = (str) => [...str].reverse().join('');

console.log(reverse('HI My Name is Gonzalo'));
console.log(reverse_2('Hi Alexa. You rock'));

// merge two sorted arrays and keep the new array sorted
function merge_sorted_arrays(arr1, arr2) {
	// checks
	if (arr1.length === 0) {
		return arr2;
	} else if (arr2.length === 0) {
		return arr1;
	}
	// sol
	var j = 1;
	var i = 1;
	var arr_1_value = arr1[0];
	var arr_2_value = arr2[0];

	const sorted_array = [];
	while (arr_1_value || arr_2_value) {
		if (!arr_2_value || arr_1_value < arr_2_value) {
			sorted_array.push(arr_1_value);
			arr_1_value = arr1[i];
			i++;
		} else {
			sorted_array.push(arr_2_value);
			arr_2_value = arr2[j];
			j++;
		}
	}
	return sorted_array;
}

console.log(merge_sorted_arrays([0, 3, 4, 33], [4, 6, 30]));

// two sum
/**
 * Given an array of integers nums and an integer target, return indices of the two numbers
 * such that they add up to target. You may assume that each input would have exactly one solution,
 * and you may not use the same element twice. You can return the answer in any order.
 *
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 */

const two_sum = (arr, target_sum) => {
	// checks
	if (arr.length === 0) {
		return `No sum`;
	}
	// not best solution using nested for loops
	const hashed = new Map();
	for (let i = 0; i < arr.length; i++) {
		const difference = target_sum - arr[i];
		if (!hashed.has(difference)) {
			hashed.set(arr[i], i);
		} else {
			let difference_index = hashed.get(difference);
			return [difference_index, i];
		}
	}
	return null;
	// loop array once
	// current_sum = arr[i] + arr[i + 1]
};

console.log(two_sum([2, 7, 11, 15], 9));
console.log(two_sum([3, 2, 4], 6));
console.log(two_sum([3, 2, 4], 55));

// const hashed = new Map();
// hashed.set(5, 3);
// console.log(hashed);

// max sub array
// given an array find the largest sum and return its sum
function max_subarray(arr) {
	// checks
	if (arr.length === 0) {
		return 0;
	} else if (arr.length === 1) {
		return arr[0];
	}
	let max_sum = -Infinity;
	for (let i = 0; i < arr.length; i++) {
		let current_sum = arr[i];
		for (let j = i + 1; j < arr.length; j++) {
			current_sum += arr[j];
			if (current_sum > max_sum) {
				max_sum = current_sum;
			}
		}
	}
	return max_sum;
}
console.log('Max Subarray');
console.log(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(max_subarray([1]));
console.log(max_subarray([5, -9, 1, 7, 1]));

function max_subarray_2(arr) {
	let current_sum = 0;
	let max_sum = 0;
	for (let i = 0; i < arr.length; i++) {
		current_sum = Math.max(current_sum + arr[i], arr[i]);
		max_sum = Math.max(current_sum, max_sum);
	}
	return max_sum;
}

console.log('Max Subarray 2');
console.log(max_subarray_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(max_subarray_2([1]));
console.log(max_subarray_2([5, -9, 1, 7, 1]));

function move_zeros(arr) {
	let moved_index = 0;
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] !== 0) {
			arr[moved_index] = arr[i];
			moved_index++;
		}
	}
	for (let i = moved_index; i < arr.length; i++) {
		arr[i] = 0;
	}
	return arr;
}

console.log(move_zeros([0, 1, 0, 3, 12]));

function contains_duplicate(arr) {
	//checks
	if (arr.length === 0) {
		return false;
	}

	const unique_keys = new Map();
	for (let i = 0; i < arr.length; i++) {
		if (!unique_keys.has(arr[i])) {
			unique_keys.set(arr[i], i);
		} else {
			return true;
		}
	}
	return false;
}

console.log(contains_duplicate([1, 2, 3, 1]));
console.log(contains_duplicate([1, 2, 3, 4]));

// Some examples
const unique = (str) => {
	const chr_lookup = new Map();
	for (let i = 0; i < str.length; i++) {
		if (chr_lookup.has(str[i])) {
			return false;
		}
		chr_lookup.set(str[i], true);
	}
	if (str.length === chr_lookup.size) {
		return true;
	} else {
		return 'Check your logic';
	}
};

const is_permutation = (str_1, str_2) => {
	if (!str_1 || !str_2) {
		console.log('what');
		return false;
	}

	if (str_1.length !== str_2.length) {
		return false;
	}

	const map_1 = new Map();
	const map_2 = new Map();

	for (let i = 0; i < str_1.length; i++) {
		if (!map_1.has(str_1[i])) {
			map_1.set(str_1[i], 1);
		} else {
			let value = Number(map_1.get(str_1[i]));
			map_1.set(str_1[i], (value += 1));
		}
	}

	for (let i = 0; i < str_2.length; i++) {
		if (!map_2.has(str_1[i])) {
			map_2.set(str_1[i], 1);
		} else {
			let value = Number(map_2.get(str_1[i]));
			map_2.set(str_1[i], (value += 1));
		}
	}

	for (char of map_1) {
		if (map_2[char[0]] !== map_1[char[0]]) {
			return false;
		}
	}
	return true;
};

const replace_white_spaces = (str, length) => {
	str = str.trim();
	let new_str = '';
	if (length == 0) {
		return null;
	}

	for (let i = 0; i < str.length; i++) {
		if (str[i] === ' ') {
			new_str = new_str + '%20';
		} else {
			new_str += str[i];
		}
	}
	return new_str;
};

console.log('\nCheck if its a unique character in the string');
console.log(unique('Alexa'));
console.log(unique('alisona'));
console.log('\nIs Permutation');
console.log(is_permutation('abcd', 'cdba'));
console.log(is_permutation('ccdf', 'fcdd'));

console.log(replace_white_spaces('Mr John Smith    ', 13));

const is_palindrome_permutation = (str) => {
	// checks
	str = str.replace(' ', '');
	const map = new Map();
	let odd_count = 0;
	for (let i = 0; i < str.length; i++) {
		if (!map.has(str[i])) {
			map.set(str[i], 1);
		} else {
			let update_count = map.get(str[i]) + 1;
			map.set(str[i], update_count);
		}
	}
	for (let [letter, count] of map.entries()) {
		if (count % 2 !== 0) {
			odd_count++;
		}
		if (odd_count > 1) {
			return false;
		}
	}
	return true;
};

console.log(is_palindrome_permutation('tacocat'));

let my_str = 'ple';
console.log(my_str.substring(0, 1) + 'a' + my_str.substring(1, my_str.length));
console.log('-------');

const one_away = (str_1, str_2) => {
	let edits = 0;
	for (let i = 0; i < str_1.length; i++) {
		if (str_1[i] !== str_2[i]) {
			edits++;
			str_2 = str_2.substring(i - 1, i) + str_1[i] + str_2.substring(i, str_2.length);
		}
		if (edits > 1) {
			return false;
		}
	}
	return true;
};

console.log(one_away('pale', 'ple'));
console.log(one_away('pales', 'pale'));
console.log(one_away('pale', 'bake'));
