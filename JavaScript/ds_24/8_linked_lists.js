let obj_1 = { name: 'Alexa' };
let obj_2 = obj_1;
obj_1.skill = 5;
// i can delete object 1 and object 2 will still have the value that was added because the pointer knows
// that there is an object pointing to that memory location
// js garbage collection is automatic -
delete obj_1;
obj_2.fav = 'Soccer';
// console.log(obj_1);
console.log(obj_2);

// we can delete items in memory
let ll = {
	head: {
		value: 10,
		next: {
			value: 5,
			next: {
				value: 16,
				next: null,
			},
		},
	},
};

console.log(ll);

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

const my_list = new SinglyLL(10);
console.log(my_list);
my_list.append(5);
my_list.append(16);
my_list.prepend(1);
// console.log(my_list.print_list());
my_list.insert(2, 99);
// console.log(my_list.print_list());
my_list.insert(3, 11);
my_list.remove(2);
