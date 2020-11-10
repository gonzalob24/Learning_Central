"use strict";

class Node {
	constructor(value) {
		this.info = value;
		this.next = null;
		this.prev = null;
	}
}

class DoubleLinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
		this.length = 0;
	}

	isEmpty() {
		return this.length === 0;
	}
	// add a node at the end of the list
	push(value) {
		let tempNode = new Node(value);
		if (this.isEmpty()) {
			this.head = tempNode;
			this.tail = tempNode;
		} else {
			tempNode.prev = this.tail;
			this.tail.next = tempNode;
			this.tail = tempNode;
		}

		this.length++;
	}

	// remove the last item
	pop() {
		var removedItem = this.tail;
		if (this.isEmpty()) {
			return `List is empty`;
		} else if (this.length === 1) {
			this.tail = null;
			this.head = null;
		} else {
			this.tail = removedItem.prev;
			this.tail.next = null;
			removedItem.prev = null;
		}
		this.length--;

		return removedItem;
	}
	display() {
		var p = this.head;
		while (p !== null) {
			console.log(p.info);
			p = p.next;
		}
	}
}

const dll = new DoubleLinkedList();
dll.push(1);
dll.push(2);
dll.push(3);
dll.push(4);
dll.display();
dll.pop();
console.log(`-----Popped Item--------`);
dll.display();
