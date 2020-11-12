// push / pop methods
class Node {
	constructor(value) {
		this.info = value;
		this.next = null;
	}
}

class Stack {
	constructor() {
		this.first = null;
		this.last = null;
		this.size = 0;
	}

	isEmpty() {
		return this.size == 0;
	}
	// add to the end
	push(value) {
		var tempNode = new Node(value);
		if (this.isEmpty()) {
			this.first = tempNode;
			this.last = tempNode;
		} else {
			//this.last.next = tempNode; // head -->1 --> 2 -->null tail
			//this.last = tempNode;
			// var temp = this.first;
			//this.first = tempNode;
			//this.first.next = temp;
			tempNode.next = this.first;
			this.first = tempNode;
		}

		this.size++;
	}

	// remove from top of stack
	pop() {
		var poppedItem;
		if (this.isEmpty()) {
			return ` Stack is empty`;
		} else if (this.size === 1) {
			poppedItem = this.first.info;
			this.first = null;
			this.last = null;
		} else {
			poppedItem = this.first.info;
			this.first = this.first.next;
		}

		this.size--;
		return poppedItem;
	}

	peek() {
		if (this.isEmpty()) {
			return `Stack is empty`;
		} else {
			return this.first.info;
		}
	}

	delete() {
		if (this.isEmpty()) {
			return `Stack is empty`;
		} else {
			this.first = null;
			this.last = null;
			this.size = 0;
		}
	}
}

s = new Stack();
s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);
s.pop();
console.log(s.peek());
s.delete();
