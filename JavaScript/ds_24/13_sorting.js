const numbers = [2, 65, 34, 2, 1, 7, 8];
console.log(numbers.sort());

// to sort numbers in JS
const sorted = numbers.sort(function (a, b) {
	return a - b;
});

console.log(sorted);

// bubble sort: move largest element to the right using multiple pass through's
// compare current element to one on the right and only swap if current element is larger
const bubble_sort = (arr) => {
	for (let i = 0; i < arr.length; i++) {
		for (let j = 0; j < arr.length; j++) {
			if (arr[j] > arr[j + 1]) {
				let temp_number = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp_number;
				console.log(arr);
			}
		}
		// console.log(arr);
	}
	return arr;
};

bubble_sort([5, 6, 8, 1, 2]);
// bubble_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]);
// place the smallest elements at the front. Always scans for smallest item and
// places it towards the front
const selection_sort = (arr) => {
	for (let i = 0; i < arr.length; i++) {
		let smallest_loc = i;
		let temp_number = arr[i];
		for (let j = i + 1; j < arr.length; j++) {
			if (arr[smallest_loc] > arr[j]) {
				smallest_loc = j;
			}
		}
		console.log(arr);

		arr[i] = arr[smallest_loc];
		arr[smallest_loc] = temp_number;
	}
	return arr;
};

console.log(selection_sort([5, 6, 8, 1, 2]));

console.log('\n\ninsertion sort');

// fast when list is almost sorted or a very small data set
// compare the next element to the growing sorted items and place it
// in the correct location
const insertion_sort = (arr) => {
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] < arr[0]) {
			//move number to first position
			console.log(i);
			// move item from one position to i'th position
			arr.unshift(arr.splice(i, 1)[0]);
			console.log(arr);
		} else {
			// locate the correct position for the number
			for (let j = 1; j < i; j++) {
				if (arr[i] > arr[j - 1] && arr[i] < arr[j]) {
					console.log(i, j);
					console.log(arr);
					// delete and move i'th item to correct place in sorted portion of list, to j'th position
					arr.splice(j, 0, arr.splice(i, 1)[0]);
					console.log(arr);
				}
			}
		}
	}
	return arr;
};
const temp_arr = [23, 1, 10, 5, 6];
temp_arr.unshift(temp_arr.splice(1, 1)[0]); // 1,23,10,5,2
temp_arr.splice(1, 0, temp_arr.splice(2, 1)[0]);
console.log('----', temp_arr);

// console.log(temp_arr);
// console.log(temp_arr.splice(1, 0, temp_arr.splice(3, 1)[0]));
// console.log(temp_arr);

// console.log(temp_arr.splice(0, 1));
// console.log(temp_arr);
// temp_arr.unshift(temp_arr.splice(0, 1)[0]);
// console.log(temp_arr);
// console.log(insertion_sort([5, 6, 8, 1, 2]));

const merge_sort = (arr) => {
	if (arr.length === 1) {
		return arr;
	}
	//split array into right and left
	const middle = Math.floor(arr.length / 2);
	const left = arr.slice(0, middle);
	const right = arr.slice(middle);
	console.log('left', left);
	console.log('right', right);

	return merge(merge_sort(left), merge_sort(right));
};

function merge(left, right) {
	// merges the right and left items
	const result = [];
	let left_index = 0;
	let right_index = 0;
	while (left_index < right_index && right_index < right.length) {
		if (left[left_index] < right[right_index]) {
			result.push(left[left_index]);
			left_index++;
		} else {
			result.push(right[right_index]);
			right_index++;
		}
	}
	console.log(left, right);

	return result.concat(left.slice(left_index)).concat(right.slice(right_index));
}

console.log('\n\nQuick Sort');

function quickSort(array, left, right) {
	const len = array.length;
	let pivot;
	let partitionIndex;

	if (left < right) {
		pivot = right;
		// move partition index to middle
		partitionIndex = partition(array, pivot, left, right);

		//sort left and right with divide and conqueror
		quickSort(array, left, partitionIndex - 1);
		quickSort(array, partitionIndex + 1, right);
	}
	return array;
}

function partition(array, pivot, left, right) {
	let pivotValue = array[pivot];
	let partitionIndex = left;

	for (let i = left; i < right; i++) {
		if (array[i] < pivotValue) {
			swap(array, i, partitionIndex);
			partitionIndex++;
		}
	}
	swap(array, right, partitionIndex);
	return partitionIndex;
}

function swap(array, firstIndex, secondIndex) {
	var temp = array[firstIndex];
	array[firstIndex] = array[secondIndex];
	array[secondIndex] = temp;
}

//Select first and last index as 2nd and 3rd parameters
const nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
quickSort(nums, 0, nums.length - 1);
console.log(nums);
