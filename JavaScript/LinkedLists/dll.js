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

	// Remove from the front
	shift() {
		var removedItem = this.head;
		if (this.isEmpty()) {
			return `List is empty`;
		} else if (this.length === 1) {
			this.head = null;
			this.tail = null;
		} else {
			this.head = removedItem.next;
			removedItem.next = null;
			this.head.prev = null;
		}

		this.length--;
		return removedItem;
	}
	// add at the front
	unshift(value) {
		var tempNode = new Node(value);
		if (this.isEmpty()) {
			this.head = tempNode;
			this.tail = tempNode;
		} else {
			tempNode.next = this.head;
			this.head.prev = tempNode;
			this.head = tempNode;
		}
		this.length++;
	}

	// get node at an index
	get(index) {
		var p;
		var count = 0;
		if (index < 0) {
			return `Index has to be >= 0`;
		} else if (this.isEmpty()) {
			return `List is empty`;
		} else {
			var middle = Math.trunc(this.length / 2);
			// start at front
			if (index < middle) {
				p = this.head;
				while (count < index) {
					p = p.next;
					count++;
				}
			} else {
				// start at end
				count = this.length - 1;
				p = this.tail;
				while (count > index) {
					p = p.prev;
					count--;
				}
			}
		}
		return p;
	}

	/// update node with a different value
	set(index, value) {
		var foundNode = this.get(index);
		if (foundNode !== null) {
			foundNode.info = value;
			return true;
		}

		return false;
	}

	// insert at an index
	insert(index, value) {
		var tempNode = new Node(value);
		if (index < 0 || index > this.length) {
			return false;
		} else if (index === this.length) {
			// add at the end
			this.push(tempNode);
		} else {
			var prevNode = this.get(index - 1);
			tempNode.next = prevNode.next;
			prevNode.next = tempNode;
			tempNode.next.prev = tempNode;
			tempNode.prev = prevNode;
		}
		this.length++;
	}

	// remove can be done with index or value
	remove() {}
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
dll.push(5);
dll.push(6);
dll.push(7);
dll.push(8);
dll.push(9);
dll.display();
dll.pop();
console.log(`-----Popped Item--------`);
dll.display();
console.log(`------Removed from front------`);
dll.shift();
dll.display();
dll.unshift(88);
console.log(`----Add at the front`);
dll.display();
console.log(dll.get(6));
dll.set(3, 44);
dll.insert(3, 11);
dll.display();
//console.log(`Item at 5: ${dll.get(4)}`);
