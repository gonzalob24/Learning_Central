'use-strict';
class HashTable {
	constructor(size) {
		this.size = size;
		this.data = new Array(size);
	}

	_hash(key) {
		let hash = 0;
		for (let i = 0; i < key.length; i++) {
			hash = (hash + key.charCodeAt(i) * i) % this.data.length;
		}
		return hash;
	}

	set(key, value) {
		// O(1)
		let address = this._hash(key);
		if (!this.data[address]) {
			this.data[address] = [];
		}
		// O(1)
		this.data[address].push([key, value]);
	}

	get(key) {
		// if no collisions -- O(1)
		// with collisions -- O(n)
		let address = this._hash(key);
		let location = this.data[address];
		if (location) {
			for (let i = 0; i < location.length; i++) {
				if (location[i][0] === key) {
					return location[i][1];
				}
			}
		}
		return undefined;
	}

	keys() {
		const keys = [];
		for (let i = 0; i < this.data.length; i++) {
			if (this.data[i]) {
				for (let j = 0; j < this.data[i].length; j++) {
					keys.push(this.data[i][j][0]);
				}
			}
		}
		return keys;
	}
}

const table_1 = new HashTable(60);
table_1.set('Grapes', 1100);
table_1.set('Oranges', 2);
table_1.set('Apples', 44);
console.log(table_1.get('Grapes'));
console.log(table_1.keys());

// given an array find the first recurring item
const find_first_recurring_element = (arr) => {
	//checks
	if (arr.length <= 1) {
		return undefined;
	}
	// space complexity O(n)
	const elements_map = new Map();
	// O(n)
	for (let i = 0; i < arr.length; i++) {
		if (!elements_map.has(arr[i])) {
			elements_map.set(arr[i], true);
		} else {
			return arr[i];
		}
	}
	return undefined;
};

console.log(find_first_recurring_element([2, 5, 1, 2, 3, 5, 1, 2, 4]));
console.log(find_first_recurring_element([2, 1, 1, 2, 3, 5, 1, 2, 4]));
console.log(find_first_recurring_element([2, 3, 4, 5]));
