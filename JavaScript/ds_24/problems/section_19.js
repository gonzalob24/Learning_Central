// Helper Singly Linked List
class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class SinglyLL {
	// creating the first node
	constructor(value) {
		this.head = { value: value, next: null };
		this.tail = this.head;
		this.length = 1;
	}

	append(value) {
		// create new node
		const new_node = new Node(value);
		// insert new node
		this.tail.next = new_node;
		// tail is now the node
		this.tail = new_node;
		this.length++;
	}

	prepend(value) {
		const new_node = new Node(value);
		new_node.next = this.head;
		this.head = new_node;
		this.length++;
		return this;
	}

	insert(index, value) {
		// check params
		if (index >= this.length) {
			return this.append(value);
		}

		const new_node = new Node(value);
		let current_node = this.head;
		let counter = 0;
		// get the node right before the actual index
		while (counter !== index - 1) {
			current_node = current_node.next;
			counter++;
		}
		const temp_node = current_node.next;
		current_node.next = new_node;
		new_node.next = temp_node;
		this.length++;
		console.log(this.print_list());
	}

	remove(index) {
		// check params
		let current_node = this.head;
		let counter = 0;
		while (counter !== index - 1) {
			current_node = current_node.next;
			counter++;
		}
		const delete_node = current_node.next;
		current_node.next = delete_node.next;
		this.length--;
		console.log(this.print_list());
	}

	reverse() {
		// if (this.length === 1) {
		//   return this.print_list()
		// }
		if (!this.head.next) {
			return this.head;
		}
		let first_node = this.head;
		let second_node = first_node.next;
		this.tail = this.head;
		while (second_node) {
			const temp = second_node.next;
			second_node.next = first_node;
			first_node = second_node;
			second_node = temp;
		}
		this.head.next = null;
		this.head = first_node;
		return this.print_list();
	}

	print_list() {
		const array = [];
		let current_node = this.head;
		while (current_node !== null) {
			array.push(current_node.value);
			current_node = current_node.next;
		}
		return array;
	}
}

/**
 *
 * @param {*} arr
 * @param {*} target_sum
 * @returns
 */

const two_sum_array = (arr, target_sum) => {
	// pick two numbers that add up to the target sum
	const numbers_seen = new Map();
	for (let i = 0; i < arr.length; i++) {
		//
		const difference = target_sum - arr[i];
		if (!numbers_seen.has(difference)) {
			numbers_seen.set(arr[i], i);
		} else {
			return [i, numbers_seen.get(difference)];
		}
	}
	return numbers_seen;
};

const two_sum_array_brute_force = (arr, target_sum) => {
	let number_to_find = null;
	for (let p1 = 0; p1 < arr.length; p1++) {
		number_to_find = target_sum - arr[p1];
		for (let p2 = p1 + 1; p2 < arr.length; p2++) {
			if (number_to_find === arr[p2]) {
				return [p1, p2];
			}
		}
	}
	// if it reaches the end I have not found a solution
	return null;
};

console.log(two_sum_array([2, 7, 11, 15], 9));
console.log(two_sum_array([3, 2, 4], 6));
console.log(two_sum_array_brute_force([1, 3, 7, 9, 2], 11));

list_1 = new SinglyLL(2);
list_1.append(4);
list_1.append(3);

list_2 = new SinglyLL(5);
list_2.append(6);
list_2.append(4);

const add_two_numbers = (l1, l2) => {
	let str_num_1 = '';
	let str_num_2 = '';
	let current_node = l1.head;
	while (current_node !== null) {
		str_num_1 = current_node.value + str_num_1;
		current_node = current_node.next;
	}

	let current_node_2 = l2.head;
	while (current_node_2 !== null) {
		str_num_2 = current_node_2.value + str_num_2;
		current_node_2 = current_node_2.next;
	}
	let sum = Number(str_num_1) + Number(str_num_2);

	const sum_string = String(sum);
	let new_list;
	for (let i = 0; i < sum_string.length; i++) {
		if (i === 0) {
			new_list = new SinglyLL(sum_string[i]);
		} else {
			new_list.append(sum_string[i]);
		}
	}
	console.log(new_list);
};

add_two_numbers(list_1, list_2);
l1 = new SinglyLL(0);
l2 = new SinglyLL(0);

add_two_numbers(l1, l2);

const longest_substring_no_repeating_characters = (str) => {
	// find the longest substring
	// no repeating characters

	let count = 0;
	let longest = 0;
	const hash = new Map();
	for (let i = 0; i < str.length; i++) {
		if (!hash.has(str[i])) {
			hash.set(str[i], 1);
			count++;
		} else {
			hash.clear();
			count = 0;
		}
		if (longest < count) {
			longest = count;
		}
	}
	return longest;
};

const longest_substring_no_repeating_characters_LR_pointer = (str) => {
	// find the longest substring
	// no repeating characters
	let max = 0;
	const hash = new Set();
	let l = 0;
	for (let r = 0; r < str.length; r++) {
		while (hash.has(str[r])) {
			hash.delete(str[l]);
			l += 1;
		}
		hash.add(str[r]);

		max = Math.max(max, r - l + 1);
	}
	return max;
};

// console.log(longest_substring_no_repeating_characters('abcabcbb'));
// console.log(longest_substring_no_repeating_characters('bbbbb'));
console.log(longest_substring_no_repeating_characters('pwwkew'));
console.log(longest_substring_no_repeating_characters_LR_pointer('pwwkew'));

// Brute force solution
const container_with_most_water = (arr) => {
	// a = h X w
	let max_area = 0;
	for (let p1 = 0; p1 < arr.length; p1++) {
		for (let p2 = p1 + 1; p2 < arr.length; p2++) {
			let min_height = Math.min(arr[p1], arr[p2]);
			let area = min_height * (p2 - p1);
			max_area = Math.max(max_area, area);
		}
	}
	return max_area;
};

const container_with_most_water_optimized = (arr) => {
	let max_area = 0;
	let p2 = arr.length - 1;
	// I can also use a while loop
	// while (p1 < p2) --> this removes the if (p2 - p1 < 0)
	for (let p1 = 0; p1 < arr.length; ) {
		if (p2 - p1 < 0) {
			break;
		}
		let min_height = Math.min(arr[p1], arr[p2]);
		let area = min_height * (p2 - p1);
		max_area = Math.max(max_area, area);

		if (arr[p1] < arr[p2]) {
			p1++;
		} else {
			p2--;
		}
	}
	return max_area;
};

console.log('Max container with water BRUTE FORCE');

console.log(container_with_most_water([1, 7, 2, 0, 1, 3]));
console.log(container_with_most_water([]));
console.log(container_with_most_water([1]));
console.log(container_with_most_water([6, 9, 3, 4, 5, 8]));

console.log('Max container with water Optimized');
console.log(container_with_most_water_optimized([1, 7, 2, 0, 1, 3]));
console.log(container_with_most_water_optimized([]));
console.log(container_with_most_water_optimized([1]));
console.log(container_with_most_water_optimized([6, 9, 3, 4, 5, 8]));
console.log(container_with_most_water_optimized([7, 1, 2, 3, 9]));
