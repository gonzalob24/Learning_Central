'use-strict';

class Node {
	constructor(value = null) {
		this.value = value;
		this.next = null;
	}
}

class DoublyNode3 {
	constructor(value) {
		this.value = value;
		this.next = null;
		this.prev = null;
		this.child = null;
	}
}

class LinkedList {
	constructor(value = value) {
		this.length = 1;
	}

	append(value) {}

	prepend(value) {}

	insert(index, value) {}

	remove(index) {}

	traverse() {}

	reverse() {}

	revers_m_n(m, n) {}
}

class DoublyNode {
	constructor(value = null) {
		this.value = value;
		this.next = null;
		this.prev = null;
	}
}

class SinglyLL extends LinkedList {
	constructor(value = null) {
		super(value);
		this.head = new Node(value);
		this.tail = this.head;
	}
}

class DoublyLL extends LinkedList {
	constructor(value = null) {
		super(value);
		this.head = new DoublyNode(value);
		this.tail = this.head;
	}
}

class DoublyLL3 extends LinkedList {
	constructor(value = null) {
		super(value);
		this.head = new DoublyNode3(value);
		this.tail = this.head;
	}
}

class Stack {
	// use an array
	constructor() {
		this.array = [];
		this.top = null;
		this.bottom == null;
		this.length = 0;
	}

	add(value) {}

	peek() {}
}

class Queue extends Stack {
	constructor() {
		super();
	}

	enqueue() {}

	dequeue() {}

	peek() {}
}

module.exports = { Node, DoublyNode, SinglyLL, DoublyLL, DoublyNode3, DoublyLL3, Stack };
