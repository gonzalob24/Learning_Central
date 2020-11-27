// import queue from "../StacksQueues/queue";
// const queue = require("../StacksQueues/queue.js");

class Node {
	constructor(value) {
		this.info = value;
		this.lchild = null;
		this.rchild = null;
	}
}

class BinarySearchTree {
	constructor() {
		this.root = null;
	}
	isEmpty() {
		return this.root === null;
	}
	// Add a new node
	insert(data) {
		const newNode = new Node(data);
		var tempNode = this.root;
		var p;
		if (this.isEmpty()) {
			this.root = newNode;
			return this;
		}
		// else {
		// 	while (tempNode !== null) {
		// 		p = tempNode;
		// 		if (data <= tempNode.info) {
		// 			tempNode = tempNode.lchild;
		// 		} else {
		// 			tempNode = tempNode.rchild;
		// 		}
		// 	}
		// 	// insert new node
		// 	if (data <= p.info) {
		// 		p.lchild = newNode;
		// 	} else {
		// 		p.rchild = newNode;
		// 	}
		// }

		while (true) {
			if (data === tempNode.info) {
				return undefined;
			}
			if (data < tempNode.info) {
				if (tempNode.lchild === null) {
					tempNode.lchild = newNode;
					return this;
				}
				tempNode = tempNode.lchild;
			} else {
				if (tempNode.rchild === null) {
					tempNode.rchild = newNode;
					return this;
				}
				tempNode = tempNode.rchild;
			}
		}
	}

	insert_recursion(data) {
		this.root = this._insert_recursion(data, this.root);
	}

	_insert_recursion(data, p) {
		// Base case --> root is null
		if (p === null) {
			p = new Node(data);
		} else if (data < p.info) {
			p.lchild = this._insert_recursion(data, p.lchild);
		} else if (data > p.info) {
			p.rchild = this._insert_recursion(data, p.rchild);
		} else {
			console.log(`Node already exists`);
		}

		return p;
	}
	// find node in BST
	find(data) {
		// if (this.isEmpty()) {
		// 	return undefined;
		// } else {
		// 	var prevNode;
		// 	var currentNode = this.root;
		// 	while (currentNode !== null) {
		// 		prevNode = currentNode;
		// 		if (data === currentNode.info) {
		// 			return `Data was found`;
		// 		} else if (data < currentNode.info) {
		// 			currentNode = currentNode.lchild;
		// 		} else if (data > currentNode.info) {
		// 			currentNode = currentNode.rchild;
		// 		}
		// 	}
		// 	if (currentNode === null) {
		// 		return "Data not found";
		// 	}
		// }
		if (this.isEmpty()) {
			return undefined;
		} else {
			var found = false;
			var currentNode = this.root;
			while (currentNode && !found) {
				if (data === currentNode.info) {
					return true;
				} else if (data < currentNode.info) {
					currentNode = currentNode.lchild;
				} else if (data > currentNode.info) {
					currentNode = currentNode.rchild;
				}
			}
			return false;
		}
	}

	find_recursion(data) {
		return this._find_recursion(data, this.root) !== null;
	}

	_find_recursion(data, node) {
		if (node === null) {
			return node;
		} else if (data < node.info) {
			node = this._find_recursion(data, node.lchild);
		} else if (data > node.info) {
			node = this._find_recursion(data.node.rchild);
		}

		return node;
	}

	// Level order --> BFS
	// Use a queue to help out
	level_order() {
		// visis root
		const q = [];
		const results = [];
		var removedItem;
		q.push(this.root);

		// checks to see if q is empty
		while (q.length) {
			removedItem = q.shift();
			results.push(removedItem.info);
			if (removedItem.lchild !== null) {
				q.push(removedItem.lchild);
			}
			if (removedItem.rchild !== null) {
				q.push(removedItem.rchild);
			}
		}
		return results;
	}

	// Inorder Traversal
	inorder() {
		this._inorder(this.root);
	}

	_inorder(root) {
		if (root === null) {
			return;
		} else {
			this._inorder(root.lchild);
			console.log(root.info);
			this._inorder(root.rchild);
		}
	}

	preorder() {
		this._preoder(this.root);
	}

	_preoder(root) {
		if (root === null) {
			return;
		} else {
			console.log(root.info);
			this._preoder(root.lchild);
			this._preoder(root.rchild);
		}
	}
}

const tree = new BinarySearchTree();
tree.insert(100);
tree.insert(200);
tree.insert(90);
tree.insert(80);
tree.insert(95);

const tree_rec = new BinarySearchTree();
tree_rec.insert_recursion(200);
tree_rec.insert_recursion(300);
tree_rec.insert_recursion(600);
tree_rec.insert_recursion(100);
tree_rec.insert_recursion(90);
tree_rec.insert_recursion(85);
tree_rec.insert_recursion(55);
console.log(tree.find(80));
console.log(tree.find(800));
console.log(tree_rec.find_recursion(100));
tree_rec.insert_recursion(600);
const arr = tree_rec.level_order();
tree_rec.inorder();
console.log(`--------Preorder---------`);
tree_rec.preorder();
