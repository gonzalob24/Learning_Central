// Queues

class Node {
	constructor(value) {
		this.info = value;
		this.next = null;
	}
}

class Queue {
	constructor() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}
	isEmpty() {
		return this.size === 0;
	}

	// at to the end
	enqueue(value) {
		var newNode = new Node(value);
		if (this.isEmpty()) {
			this.head = newNode;
			this.tail = newNode;
		} else {
			this.tail.next = newNode;
			this.tail = newNode;
		}
		this.size++;
	}

	// removing from the start of the queue
	dequeue() {
		var removedItem;
		if (this.isEmpty()) {
			return `Queue is empty`;
		} else if (this.size === 1) {
			removedItem = this.head.info;
			this.head = null;
			this.tail = null;
		} else {
			removedItem = this.head.info;
			this.head = this.head.next;
		}

		this.size--;
		return removedItem;
	}
}

q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
q.dequeue();
