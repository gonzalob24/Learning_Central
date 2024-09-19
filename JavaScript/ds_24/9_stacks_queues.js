// stacks
// build it with Array or LL?
// why an array vs LL and vice versa?

// Queues
// build it with Array or LL?
// why an array vs LL and vice versa?

class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class Stack {
	constructor() {
		this.top = null;
		this.bottom = null;
		this.length = 0;
	}
	peek() {
		return this.top.value;
	}

	push(value) {
		// create new node
		const new_node = new Node(value);
		// check if stack is empty
		if (this.length === 0) {
			this.bottom = new_node;
			this.top = this.bottom;
		} else {
			const temp_top = this.top;
			this.top = new_node;
			this.top.next = temp_top;
		}

		this.length++;
	}

	pop() {
		if (!this.top) {
			return null;
		}
		if (this.top === this.bottom) {
			this.bottom = null;
		}
		let temp_top = this.top;
		this.top = this.top.next;
		this.length--;
		return temp_top.value;
	}
}

const stack_1 = new Stack();
stack_1.push(1);
stack_1.push(2);
stack_1.push(3);
// stack_1.push(4);
// console.log(stack_1);
// console.log(stack_1.peek());
console.log(stack_1.pop());
console.log(stack_1.pop());
console.log(stack_1);

class StackArray {
	constructor() {
		this.array = [];
	}

	peek() {
		return this.array[this.array.length - 1];
	}

	pop() {
		this.array.pop();
	}

	push(value) {
		this.array.push(value);
	}
}

const stack_array = new StackArray();
stack_array.push(1);
stack_array.push(2);
stack_array.push(3);
console.log(stack_array);
console.log(stack_array.peek());
stack_array.pop();
console.log(stack_array);

class QueLL {
	constructor() {
		this.first = null;
		this.last = null;
		this.length = 0;
	}

	peek() {
		return this.first;
	}

	enqueue(value) {
		const new_node = new Node(value);
		if (this.length === 0) {
			this.first = new_node;
			this.last = this.first;
		} else {
			this.last.next = new_node;
			this.last = new_node;
		}
		this.length++;
	}

	dequeue() {
		if (this.length === 0) {
			return null;
		}
		if (this.first === this.last) {
			this.last = null;
		}
		this.first = this.first.next;
		this.length--;
	}
}

const queue_ll = new QueLL();
queue_ll.enqueue(1);
queue_ll.enqueue(2);
queue_ll.enqueue(3);
console.log(queue_ll);
queue_ll.dequeue();
console.log(queue_ll);
queue_ll.dequeue();
console.log(queue_ll);
queue_ll.dequeue();
console.log(queue_ll);

// 232 Q. Implement a queue using stacks
