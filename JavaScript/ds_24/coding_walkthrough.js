const nemo = ['nemo', 'sdf', 'marlin', 'two', 'three', '4', '5', '6', '7'];

const large = new Array(100).fill('nemo');

function findNemo(array) {
	let time = performance.now();
	for (let i = 0; i < array.length; i++) {
		if (array[i] === 'nemo') console.log('Found NEMO');
	}
	let end_time = performance.now();
	console.log('Call to find nemo took: ' + (end_time - time) + ' milliseconds');
}

// findNemo(large);

let array = [1, 2, 3, 6];
let array2 = [1, 2, 3, 4];
let array3 = [1, 2, 3, 9];
let sum = 8;
let first = 0;
let last = array.length - 1;
const has_pair_with_sum = (array) => {
	for (let i = 0; i < array.length; i++) {
		if (first >= last) {
			return 'No Pairs found';
		} else if (array[first] + array[last] == sum) {
			return 'The pair is ' + array[first] + ' ' + array[last];
		} else if (array[first] + array[last] < sum) {
			first = first + 1;
		} else if (array[first] + array[last] > sum) {
			last = last - 1;
		}
	}
};

console.log(has_pair_with_sum(array));

const a1 = ['a', 'b', 'c', 'x'];
const a2 = ['z', 'y', 'x'];
const contains_common_element = (a1, a2) => {
	for (let i = 0; i < a1.length; i++) {
		for (let j = 0; j < a2.length; j++) {
			if (a1[i] === a2[j]) {
				return true;
			}
		}
	}
	return false;
};

// console.log(contains_common_element(a1, a2));

const contains_common_element_better = (a1, a2) => {
	// O(n)
	const value_seen = new Set();

	if (a1.length > a2.length) {
		for (let i = 0; i < a1.length; i++) {
			// O(n)
			value_seen.add(a1[i]); // O(1)
		}
		for (let j = 0; j < a2.length; j++) {
			//O(n)
			if (value_seen.has(a2[j])) {
				//O(1)
				return true;
			}
		}
		return false;
	} else {
		for (let i = 0; i < a2.length; i++) {
			value_seen.add(a2[i]);
		}
		for (let j = 0; j < a1.length; j++) {
			if (value_seen.has(a1[j])) {
				return true;
			}
		}
		return false;
	}
};

console.log(contains_common_element_better(a1, a2));
