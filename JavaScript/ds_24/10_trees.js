class Node {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

class BST {
	constructor() {
		this.root = null;
	}

	insert(value) {
		const new_node = new Node(value);
		// is tree empty
		if (this.root == null) {
			this.root = new_node;
			return this.root;
		}

		let current_node = this.root;
		while (current_node !== null) {
			if (new_node.value > current_node.value) {
				if (current_node.right !== null) {
					current_node = current_node.right;
				} else {
					current_node.right = new_node;
					return this;
				}
			} else if (new_node.value < current_node.value) {
				if (current_node.left !== null) {
					current_node = current_node.left;
				} else {
					current_node.left = new_node;
					return this;
				}
			}
		}
	}

	lookup(value) {
		let current_node = this.root;
		if (current_node === null) {
			return null;
		}

		while (current_node !== null) {
			if (current_node.value === value) {
				return current_node;
			} else if (value < current_node.value) {
				current_node = current_node.left;
			} else {
				current_node = current_node.right;
			}
		}
		return null;
	}
	remove(value) {
		if (!this.root) {
			return false;
		}
		let parent = null;
		let current_node = this.root;
		let right_left = null;
		while (current_node) {
			if (value < current_node.value) {
				parent = current_node;
				current_node = current_node.left;
				// right_left = 'left';
			} else if (value > current_node.value) {
				parent = current_node;
				current_node = current_node.right;
				// right_left = 'right';
			} else if (value === current_node.value) {
				// no right child
				// if (current_node.right === null && current_node.left == null) {
				// 	if (right_left === 'right') {
				// 		parent.right = null;
				// 		return this;
				// 	} else {
				// 		parent.left == null;
				// 		return this;
				// 	}
				// } else if (current_node.right === null && current_node.left !== null) {
				// 	if (right_left === 'right') {
				// 		parent.right = current_node;
				// 		return this;
				// 	} else {
				// 		parent.left == current_node;
				// 		return this;
				// 	}
				// }
				// or no left child
				// or no children
				if (current_node.right === null) {
					if (parent === null) {
						this.root = current_node.left;
					} else {
						if (current_node.value < parent.value) {
							parent.left = current_node.left;
						} else if (current_node.value > parent.value) {
							parent.right = current_node.left;
						}
					}
				} else if (current_node.right.left === null) {
					current_node.right.left = current_node.left;
					if (parent === null) {
						this.root = current_node.left;
					} else {
						if (current_node.value < parent.value) {
							parent.left = current_node.right;
						} else if (current_node.value > parent.value) {
							parent.right = current_node.right;
						}
					}
				} else {
					// find right childs left most child
					let left_most = current_node.right.left;
					let left_most_parent = current_node.right;
					while (left_most.left !== null) {
						left_most_parent = left_most;
						left_most = left_most.left;
					}
					left_most_parent.left = left_most.right;
					left_most.left = current_node.left;
					left_most.right = current_node.right;

					if (parent === null) {
						this.root = left_most;
					} else {
						if (current_node.value < parent.value) {
							parent.left = left_most;
						} else if (current_node.value > parent.value) {
							parent.right = left_most;
						}
					}
				}
				return true;
			}
		}
	}
}

const bst1 = new BST();
bst1.insert(9);
bst1.insert(4);
bst1.insert(20);
bst1.insert(1);
bst1.insert(6);
bst1.insert(15);
bst1.insert(170);

console.log(JSON.stringify(bst1.root));

function traverse(node) {
	const tree = { value: node.value };
	tree.left = node.left === null ? null : traverse(node.left);
	tree.right = node.right === null ? null : traverse(node.right);
	return tree;
}

console.log('\n Found node: ', bst1.lookup(1));
console.log('\n Found node: ', bst1.lookup(170));
console.log('\n Found node: ', bst1.lookup(10));

bst1.remove(6);
console.log(JSON.stringify(bst1.root));
