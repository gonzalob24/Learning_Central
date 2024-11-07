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
// console.log(ar_1.get(0));
// ar_1.pop();
ar_1.push('1');
ar_1.push('2');
console.log('----');
console.log(ar_1);
ar_1.delete();
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

console.log('Merge Sorted arrays');
console.log(merge_sorted_arrays([0, 3, 4, 20, 31, 33], [4, 6, 7, 8]));
let test = [0, 3, 4, 20, 21, 33];
console.log(!test[1]);

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
			console.log('--- ', i, difference);

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

console.log(two_sum([2, 11, 15, 7], 9));
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

// String compression
// aabcccccaaa --> a2b1c5a3
// if the compressed string is not smaller than the original string return the original string
// cas matters

const string_compression = (str) => {
	// checks
	if (str.length === 1) {
		return str;
	}
	let recurrence = 1;
	let compressed_string = '';
	for (let i = 0; i < str.length; i++) {
		if (str[i] === str[i + 1]) {
			recurrence++;
		} else {
			compressed_string += str[i] + recurrence;
			recurrence = 1;
		}
	}
	if (str.length < compressed_string.length) {
		return str;
	} else {
		return compressed_string;
	}
};

console.log(string_compression('aabcccccaaa'));
console.log(string_compression('abca'));

console.log('2D ARRAYS');
console.log('BFS or DFS');
const array_2d = [
	[1, 2, 3, 4, 5],
	[6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20],
];

const directions = [
	[-1, 0], //up
	[0, 1], //right
	[1, 0], //down
	[0, -1], //left
];

const recursive_dfs = (matrix, row, col, seen, values) => {
	if (row < 0 || col < 0 || row >= matrix.length || col >= matrix[0].length || seen[row][col]) {
		return;
	}

	values.push(matrix[row][col]);
	seen[row][col] = true;

	for (let i = 0; i < directions.length; i++) {
		const current_dir = directions[i];
		recursive_dfs(matrix, row + current_dir[0], col + current_dir[1], seen, values);
	}
};
const dfs_traversal_2d_array = (matrix) => {
	const seen = new Array(matrix.length).fill(0).map(() => new Array(matrix[0].length).fill(false));

	const values = [];
	recursive_dfs(matrix, 0, 0, seen, values);
	return values;
};

const traversal_bfs = (matrix) => {
	const seen = new Array(matrix.length).fill(0).map(() => new Array(matrix[0].length).fill(false));
	const values = [];

	const queue = [[0, 0]];

	while (queue.length) {
		const current_pos = queue.shift();
		const row = current_pos[0];
		const col = current_pos[1];

		if (row < 0 || row >= matrix.length || col < 0 || col >= matrix[0].length || seen[row][col]) {
			continue;
		}

		seen[row][col] = true;
		values.push(matrix[row][col]);

		for (let i = 0; i < directions.length; i++) {
			const current_dir = directions[i];
			queue.push([row + current_dir[0], col + current_dir[1]]);
		}
	}
	return values;
};

console.log(dfs_traversal_2d_array(array_2d));
console.log(traversal_bfs(array_2d));

console.log('no of Islands');
const directions_2 = [
	[-1, 0], //up
	[0, 1], //right
	[1, 0], //down
	[0, -1], //left
];

const island_matrix = [
	[1, 1, 1, 0, 0],
	[1, 1, 1, 0, 1],
	[0, 1, 0, 0, 1],
	[0, 0, 0, 1, 1],
];

const traversal_num_islands = (matrix) => {
	let count = 0;
	if (matrix.length === 0) {
		return 0;
	}

	for (let row = 0; row < matrix.length; row++) {
		for (let col = 0; col < matrix[0].length; col++) {
			if (matrix[row][col] === 1) {
				count++;
				matrix[row][col] = 0; // flip 1 to 0 so that I don't count it again
				// BFS to find adjacent islands
				const queue = []; // use array since JS does not have a queue implementation
				queue.push([row, col]); // add current direction

				while (queue.length) {
					const current_pos = queue.shift();
					const current_row = current_pos[0];
					const current_col = current_pos[1];

					for (let i = 0; i < directions.length; i++) {
						const current_dir = directions[i];
						console.log(`dir -- ${i}`, current_dir);

						const next_row = current_row + current_dir[0];
						const next_col = current_col + current_dir[1];

						// make sure coords are not out of bounds
						if (next_row < 0 || next_row >= matrix.length || next_col < 0 || next_col >= matrix[0].length) {
							continue;
						}
						console.log('next row - col', next_row, next_col);

						if (matrix[next_row][next_col] === 1) {
							queue.push([next_row, next_col]);
							matrix[next_row][next_col] = 0; // flip the 1 to avoid double counting
						}
					}
				}
			}
		}
	}
	return count;
};
console.log(traversal_num_islands(island_matrix));

const contains_duplicates = (arr) => {
	// use a hash set: insert and check in O(1) -> constant time
	const values_seen = new Set();
	// T: O(n)
	// S: O(n)
	for (let i = 0; i < arr.length; i++) {
		if (!values_seen.has(arr[i])) {
			values_seen.add(arr[i]);
		} else {
			return true;
		}
	}
	return false;
};

const valid_anagram = (s, t) => {
	// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

	const string_1_hash = new Map();
	const string_2_hash = new Map();

	if (s.length !== t.length) {
		return false;
	}
	for (let i = 0; i < s.length; i++) {
		string_1_hash.set(s[i], (string_1_hash.get(s[i]) || 0) + 1);
		string_2_hash.set(t[i], (string_2_hash.get(t[i]) || 0) + 1);
	}

	for (let [char, count] of string_1_hash) {
		const count_2 = string_2_hash.get(char);

		if (count !== count_2) {
			return false;
		}
	}

	return true;
};

const valid_anagram_2 = (s, t) => {
	// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
	const str_s = s.split('').sort().join('');
	const str_t = t.split('').sort().join('');

	return str_s === str_t;
};

console.log(valid_anagram('aacc', 'ccac'));

const group_anagrams = (strs) => {
	if (strs.length === 0) {
		return [''];
	}
	if (strs.length === 1) {
		return [strs];
	}

	const results = {};
	for (let i = 0; i < strs.length; i++) {
		let str_key = strs[i].split('').sort().join('');

		if (!results[str_key]) {
			results[str_key] = [strs[i]];
		} else {
			let current_array = results[str_key];
			current_array.push(strs[i]);
			results[str_key] = current_array;
		}
	}

	return Object.values(results);
};

const strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'];
console.log('group anagrams');

console.log(group_anagrams(strs));
