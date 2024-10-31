'use-strict';

class Node {
	constructor(value = null) {
		this.value = value;
		this.next = null;
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

module.exports = { Node, DoublyNode, SinglyLL, DoublyLL };
