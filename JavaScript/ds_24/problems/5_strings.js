// Typed out strings
// # --> backspace

const { Stack } = require('../common_classes/LinkedLists');

// are both equal when they are both types out
const typed_out_string = (str1) => {
	const arr_string = []; // S: (n)

	for (let i = 0; i < str1.length; i++) {
		// T: O(n)
		if (str1[i] === '#') {
			// T: O(1)
			arr_string.pop(); // T: O(1)
		} else {
			arr_string.push(str1[i]); // T: O(1)
		}
	}

	return arr_string;
};

const typed_out_strings = (str1, str2) => {
	const s1 = typed_out_string(str1); // T: O(A) --> A and B because the size of both arrays may differ
	const s2 = typed_out_string(str2); // T: O(B)
	if (s1.length !== s2.length) {
		return false;
	} else {
		for (let i = 0; i < s1.length; i++) {
			// T: O(A + B)
			if (s1[i] !== s2[i]) {
				return false;
			}
		}
	}

	return true;
};

const typed_out_optimized = (str1, str2) => {
	let p1 = str1.length - 1;
	let p2 = str2.length - 1;

	while (!(p1 < 0) || !(p2 < 0)) {
		if (str1[p1] == ' #' || str2[p2] === '#') {
			if (str1[p1] == '#') {
				let decrease_count = 2;
				while (decrease_count > 0) {
					p1--;
					decrease_count--;
					if (str1[p1] === '#') {
						decrease_count += 2;
					}
				}
			}

			if (str2[p2] === '#') {
				let decrease_count = 2;
				while (decrease_count > 0) {
					p2--;
					decrease_count--;

					if (str2[p2] === '#') {
						decrease_count += 2;
					}
				}
			}
		} else {
			if (str1[p1] !== str2[p2]) {
				return false;
			} else {
				p1--;
				p2--;
			}
		}
	}
	return true;
};

// T: O(a + b)
// S: O(a + b)
// can I optimize? maybe with space complexity, time is already pretty fast.
console.log(typed_out_strings('bvv#c#a', 'aA#'));
console.log(typed_out_optimized('abc#d', 'abcc##d'));

const longest_substring_no_repeating_characters = (str) => {
	let max_length = 0;
	let seen_characters = new Map(); // S: O(n)

	// T: O(n)
	for (let i = 0; i < str.length; i++) {
		if (!seen_characters.has(str[i])) {
			seen_characters.set(str[i], true);
		} else {
			seen_characters.clear();
			seen_characters.set(str[i], true);
		}

		max_length = Math.max(max_length, seen_characters.size);
	}
	return max_length;
};

// can this be improved?
// Cna I use a two pointer array system or sliding window approach?
const longest_substring_no_repeating_characters_sliding_window = (str) => {
	let max_length = 0;
	const seen_chars = new Map();
	let left_point = 0;
	for (let right_point = 0; right_point < str.length; right_point++) {
		if (seen_chars.has(str[right_point])) {
			seen_chars.delete(str[right_point]);
			left_point++;
			// console.log(seen_chars);
		}
		seen_chars.set(str[right_point], true);
		// console.log(seen_chars);
		max_length = Math.max(max_length, right_point - left_point + 1);
	}
	return max_length;
};

const lengthOfLongestSubstring = function (s) {
	if (s.length <= 1) return s.length;

	const seen = new Map();
	let left = 0;
	let longest = 0;

	for (let right = 0; right < s.length; right++) {
		const currentChar = s[right];
		const previouslySeenChar = seen[currentChar];

		if (previouslySeenChar >= left) {
			left = previouslySeenChar + 1;
		}

		seen[currentChar] = right;
		// console.log('current --> ', seen);

		longest = Math.max(longest, right - left + 1);
	}
	console.log('FINAL --> ', seen);

	return longest;
};

const sub_array_find_sum = (arr, sum) => {
	// edge
	if (arr.length === 0) {
		return 0;
	}
	const sub_array = [];
	let current_sum = 0;
	let left_pointer = 0;
	for (let right_point = 1; right_point < arr.length; right_point++) {
		current_sum = current_sum + arr[left_pointer] + arr[right_point];
		if (current_sum === sum) {
			return sub_array;
		}
		if (current_sum > sum) {
			current_sum = current_sum - arr[right_point];
			left_pointer++;
			current_sum = current_sum - arr[left_pointer];
		}
	}
	return current_sum;
};

const max_sum_subarray_size_2 = (arr) => {
	let left_pointer = 0;
	let max_sum = 0;
	if (arr.length < 2) {
		return 0;
	}

	for (let right_pointer = 1; right_pointer < arr.length; right_pointer++) {
		let current_sum = arr[left_pointer] + arr[right_pointer];
		max_sum = Math.max(current_sum, max_sum);
		left_pointer++;
	}
	return max_sum;
};

const subarrays_add_up_to_given_sum = (arr, sum) => {
	let left_pointer = 0;
	let current_sum = 0;
	let sub_arrays = [];
	let sub_array = [];
	for (let right_pointer = 0; right_pointer < arr.length; right_pointer++) {
		//
		if (current_sum === sum) {
			sub_arrays.push([...sub_array]);
		}

		current_sum = current_sum + arr[right_pointer];
		sub_array.push(arr[right_pointer]);

		if (current_sum > sum) {
			current_sum -= arr[left_pointer];
			sub_array.shift();
			left_pointer++;
		}
	}
	return sub_arrays;
};

const max_length_1_flip_0_k_times = (arr, k_flips) => {
	let flipped = 0;
	let max_length = 0;
	let left = 0;
	for (let right = 0; right < arr.length; right++) {
		if (arr[right] === 0) {
			flipped++;
		}
		while (flipped > k_flips) {
			if (arr[left] === 0) {
				flipped--;
			}
			left++;
		}

		max_length = Math.max(max_length, right - left + 1);
		console.log(left, right, flipped, max_length);
	}
	return max_length;
};

console.log('Length of longest substring: ', longest_substring_no_repeating_characters('abacbdca'));
console.log('Length of longest substring: ', longest_substring_no_repeating_characters('aaabcdaaa'));
console.log('Length of longest substring: ', longest_substring_no_repeating_characters(''));
console.log('Length of longest substring: ', longest_substring_no_repeating_characters('abccabb'));
console.log('Sliding window');
// console.log(longest_substring_no_repeating_characters_sliding_window('abccabb'));
console.log(longest_substring_no_repeating_characters_sliding_window('abcbdaac'));
console.log('---');
console.log(lengthOfLongestSubstring('abcbdaac'));
console.log('Subarray sum');
console.log(sub_array_find_sum([4, 2, 6, 3, 8], 9));
console.log('Max Sum Array size 2 --> ', max_sum_subarray_size_2([-1, 2, 3, 1, -3, 2]));
console.log('Sum of subarray that add up to target sum: ', subarrays_add_up_to_given_sum([1, 7, 4, 3, 1, 2, 1, 5, 1], 7));
console.log("Max continuous 1's -- ", max_length_1_flip_0_k_times([0, 1, 0, 1, 0, 0, 1, 1], 2));
console.log("Max continuous 1's -- ", max_length_1_flip_0_k_times([1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0], 2));

const is_palindrome = (str) => {
	// ignore case
	// only alpha numeric chars
	let left = 0;
	let remove_chars = str.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
	console.log(remove_chars);

	for (let right = remove_chars.length - 1; left < right; ) {
		if (remove_chars[left] !== remove_chars[right]) {
			return false;
		}
		left++;
		right--;
	}
	return true;
};

console.log('Is Palindrome');
console.log(is_palindrome('aabaa')); //T
console.log(is_palindrome('aabbaa')); //T
console.log(is_palindrome('abc')); //F
console.log(is_palindrome('a')); //T
console.log(is_palindrome('')); //T
console.log(is_palindrome('A man, a plan, a canal: Panama')); //T

console.log('Parentheses Checker');

class ParenthesesChecker extends Stack {
	constructor() {
		super();
		this.left_parentheses = new Map([
			['{', '}'],
			['[', ']'],
			['(', ')'],
		]);
		this.right_parentheses = new Map([
			['}', '{'],
			[']', '['],
			[')', '('],
		]);
	}

	add(value) {
		this.array.push(value);
		this.length++;
	}

	pop() {
		let value = this.array.pop();
		this.length--;
		return value;
	}

	peek() {
		return this.array[this.length - 1];
	}
	is_valid_parenthesis(str) {
		for (let i = 0; i < str.length; i++) {
			if (this.left_parentheses.has(str[i])) {
				this.add([str[i]]);
			} else {
				let left = this.pop();
				if (this.left_parentheses.get(left) !== str[i]) {
					return false;
				}
			}
		}
		return this.length === 0;
	}

	remove_brackets(str) {
		let string = str.split('');
		for (let i = 0; i < string.length; i++) {
			if (string[i] === '(') {
				this.add(i);
			} else {
				if (this.length === 0 && str[i] === ')') {
					string[i] = '';
				} else if (str[i] === ')') {
					this.array.pop();
				}
			}
		}
		for (let i = 0; i < this.array.length; i++) {
			string[this.array[i]] = '';
		}
		this.array = [];
		this.length = 0;
		return string.join('');
	}
}

let stack = new ParenthesesChecker();
let string = '{([])}';
let string2 = '';
let string3 = '{(])]}';
console.log(stack.is_valid_parenthesis(string));
console.log(stack.is_valid_parenthesis(string2));
console.log(stack.is_valid_parenthesis(string3));

let stack2 = new ParenthesesChecker();
let str_brackets = 'a)bc(d)';
let str_2 = '(a(bc(a)';
console.log(stack2.remove_brackets(str_brackets));
console.log(stack2.remove_brackets(str_2));
