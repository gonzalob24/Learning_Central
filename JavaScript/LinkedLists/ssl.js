class Node {
	constructor(value) {
		this.info = value;
		this.next = null;
	}
}

class SinglyLinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
		this.length = 0;
	}
	// check of SLL is empty
	isEmpty() {
		return this.length === 0;
	}

	push(data) {
		var tempNode = new Node(data);
		if (this.isEmpty()) {
			this.head = tempNode;
			this.tail = this.head;
		} else {
			this.tail.next = tempNode;
			this.tail = tempNode;
		}

		this.length++;
		//return this;
	}

	pop() {
		if (this.isEmpty()) {
			return "List is empty";
		} else if (this.length === 1) {
			var p = this.head;
			var poppedItem = p.info;
			this.head = null;
			this.tail = null;
		} else {
			var p = this.head;
			while (p.next.next !== null) {
				p = p.next;
			}
			var poppedItem = p.next.info;
			this.tail = p;
			p.next = null;
		}
		this.length--;
		return poppedItem;
	}

	displayList() {
		if (this.isEmpty()) {
			return `List is empty`;
		} else {
			let p = this.head;
			while (p !== null) {
				console.log(p.info);
				p = p.next;
			}
		}
	}

	// add at the beginning
	unshift(data) {
		var tempNode = new Node(data);
		if (this.isEmpty()) {
			this.head = tempNode;
			this.tail = tempNode;
		} else {
			tempNode.next = this.head;
			this.head = tempNode;
		}
		this.length++;
	}

	// remove from the front
	shift() {
		if (this.isEmpty()) {
			return `List is empty`;
		} else {
			var removedItem = this.head.info;
			this.head = this.head.next;
		}
		this.length--;
		return removedItem;
	}

	itemAt(index) {
		if (index < 0 || index > this.length) {
			return null;
		} else {
			var p = this.head;
			for (let i = 0; i < index; i++) {
				p = p.next;
			}
			return p;
		}
	}

	set(data, index) {
		var foundNode = this.itemAt(index);
		if (!foundNode) {
			return false;
		} else {
			foundNode.info = data;
			return true;
		}
	}

	insert(data, index) {
		if (index < 0 || index > this.length) {
			return false;
		} else if (index === this.length) {
			this.push(data);
			return true;
		} else if (index == 0) {
			this.unshift(data);
			return true;
		} else {
			var tempNode = new Node(data);
			var prevNode = this.itemAt(index - 1);
			tempNode.next = prevNode.next;
			prevNode.next = tempNode;

			return true;
		}
	}

	get listSize() {
		return this.length;
	}

	get lastItem() {
		return this.tail.info;
	}
}

const sll = new SinglyLinkedList();
console.log(sll.isEmpty());
sll.push(10);
sll.push(9);
sll.push(8);
sll.push(3);
console.log(sll.listSize);
sll.displayList();
console.log(`Popped item: ${sll.pop()}`);
sll.unshift(7);
sll.unshift(11);
console.log(`Removed item: ${sll.shift()}`);
sll.displayList();
console.log(`Item at 2 ${sll.itemAt(2)}`);
sll.set(55, 2);
sll.displayList();
sll.insert(17, 0);
console.log("New item added");
sll.displayList();
// console.log(`Last item is ${sll.lastItem}`);
// console.log(`Popped item: ${sll.pop()}`);
// console.log(`Popped item: ${sll.pop()}`);
// console.log(`Popped item: ${sll.pop()}`);
// console.log(`Popped item: ${sll.pop()}`);
