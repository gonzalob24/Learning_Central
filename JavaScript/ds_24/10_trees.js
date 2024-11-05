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
		while (true) {
			if (current_node.value > value) {
				if (!current_node.left) {
					current_node.left = new_node;
					return this;
				} else {
					current_node = current_node.left;
				}
			} else {
				if (!current_node.right) {
					current_node.right = new_node;
					return this;
				} else {
					current_node = current_node.right;
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

	bfs() {
		let current_node = this.root;
		let list = [];
		// add root node to queue
		let queue = []; // keep track of children
		queue.push(current_node);
		while (queue.length > 0) {
			current_node = queue.shift(); // get first item from the queue
			// console.log(current_node.value);
			list.push(current_node.value); // add value to the list
			if (current_node.left) {
				queue.push(current_node.left); // add left children to queue
			}
			if (current_node.right) {
				queue.push(current_node.right); // add right children
			}
		}
		return list;
	}

	bfs_recursive(queue, list) {
		// base case
		if (queue.length === 0) {
			return list;
		}
		let current_node = queue.shift();
		list.push(current_node.value);
		if (current_node.left) {
			queue.push(current_node.left); // add left children to queue
		}
		if (current_node.right) {
			queue.push(current_node.right); // add right children
		}
		return this.bfs_recursive(queue, list);
	}

	bfs_recursive_2() {
		let list = this.bfs_recursive_helper([this.root], []);
		return list;
	}

	bfs_recursive_helper(queue, list) {
		if (queue.length === 0) {
			return list;
		}
		let current_node = queue.shift(); // get first item from queue
		list.push(current_node.value);
		if (current_node.left) {
			queue.push(current_node.left);
		}
		if (current_node.right) {
			queue.push(current_node.right);
		}
		return this.bfs_recursive_helper(queue, list);
	}

	bfs_level_order() {
		return this.bfs_level_order_helper([this.root], 1, [], []);
	}

	bfs_level_order_helper(queue, temp_list, list) {
		if (queue.length === 0) {
			return list;
		}

		let current_node = queue.shift();
		if (current_node.left) {
			queue.push(current_node.left);
			temp_list.push(current_node.value);
		}
		if (current_node.right) {
			queue.push(current_node.right);
			temp_list.push(current_node.value);
		}

		list.push(temp_list);
		return this.bfs_level_order_helper(queue, temp_list, list);
	}

	bfs_iterative() {
		return this.bfs_iterative_helper(this.root);
	}

	bfs_iterative_helper(root) {
		let results = [];
		let queue = [root];

		while (queue.length) {
			let current_node = queue.shift();
			results.push(current_node.value);

			if (current_node.left) {
				queue.push(current_node.left);
			}
			if (current_node.right) {
				queue.push(current_node.right);
			}
		}
		return results;
	}

	bfs_level_order_iterative() {
		return this.bfs_level_order_iterative_helper(this.root);
	}

	bfs_level_order_iterative_helper(root) {
		let results = [];
		let temp_arr = [];
		let queue = [root];
		let level_length = queue.length;
		let counter = 0;

		while (queue.length) {
			let current_node = queue.shift();
			counter++;
			temp_arr.push(current_node.value);

			if (current_node.left) {
				queue.push(current_node.left);
			}

			if (current_node.right) {
				queue.push(current_node.right);
			}

			if (counter === level_length) {
				results.push(temp_arr);
				temp_arr = [];
				counter = 0;
				level_length = queue.length;
			}
		}
		return results;
	}

	// use recursion
	dfs_in_order() {
		return this.traverse_in_order(this.root, []);
	}

	dfs_post_order() {
		return this.traverse_post_order(this.root, []);
	}

	dfs_pre_order() {
		return this.traverse_pre_order(this.root, []);
	}

	traverse_in_order(node, list) {
		// console.log(node.value);

		if (node.left) {
			this.traverse_in_order(node.left, list);
		}
		list.push(node.value);
		if (node.right) {
			this.traverse_in_order(node.right, list);
		}
		return list;
	}

	traverse_post_order(node, list) {
		// console.log(node.value);

		if (node.left) {
			this.traverse_post_order(node.left, list);
		}
		if (node.right) {
			this.traverse_post_order(node.right, list);
		}
		list.push(node.value);
		return list;
	}

	traverse_pre_order(node, list) {
		// console.log(node.value);
		list.push(node.value);
		if (node.left) {
			this.traverse_pre_order(node.left, list);
		}
		if (node.right) {
			this.traverse_pre_order(node.right, list);
		}

		return list;
	}

	true_bst() {
		return this.is_true_bst(this.root, this.root.value);
	}

	is_true_bst(node, root_value) {
		if (node.left) {
			if (!(node.left.value < root_value)) {
				return false;
			}
			return this.is_true_bst(node.left, root_value);
		}
		if (node.right) {
			if (!(node.right.value > root_value)) {
				return false;
			}
			return this.is_true_bst(node.right);
		}
		return true;
	}

	max_depth() {
		return this.max_depth_traversal(this.root, 0);
	}

	max_depth_traversal(node, depth) {
		if (!node) {
			return depth;
		}
		depth++;
		let left = this.max_depth_traversal(node.left, depth);
		let right = this.max_depth_traversal(node.right, depth);
		return Math.max(left, right);
	}
}

const bst1 = new BST();
bst1.insert(9);
bst1.insert(4);
bst1.insert(20);
bst1.insert(1);
bst1.insert(6);
bst1.insert(8);
bst1.insert(10);
bst1.insert(15);
bst1.insert(170);
console.log('BFS');
console.log(bst1.bfs());
console.log('recursive');
console.log(bst1.bfs_recursive([bst1.root], []));
console.log(bst1.bfs_recursive_2());
console.log('Level order');
console.log(bst1.bfs_level_order_iterative());

console.log('DFS');
console.log(bst1.dfs_in_order());
console.log(bst1.dfs_post_order());
console.log(bst1.dfs_pre_order());
console.log('TRUE BST');
console.log(bst1.true_bst());

console.log(JSON.stringify(bst1.root));

function traverse(node) {
	const tree = { value: node.value };
	tree.left = node.left === null ? null : traverse(node.left);
	tree.right = node.right === null ? null : traverse(node.right);
	return tree;
}

console.log('\n Found node: ', bst1.lookup(1));
console.log('\n Found node: ', bst1.lookup(170));
console.log('\n Found node: ', bst1.lookup(4));
console.log('Max depth');
console.log(bst1.max_depth());

// bst1.remove(6);
// console.log(JSON.stringify(bst1.root));

// function traverse(node) {
// 	const tree = { value: node.value };
// 	tree.left = node.left === null ? null : traverse(node.left);
// 	tree.right = node.right === null ? null : traverse(node.right);
// 	return tree;
// }
