package SortingAlgorithms;

// Driver class for 2-3-4
public class Tree234
{
	// set root node to private for
	private Tree234Node root = new Tree234Node();

	// method to do an inorder traversal
	public void inorderTraversal()
	{
		inorderTraversal(root);
	}

	// private method to help with the traversal
	private void inorderTraversal(Tree234Node r)
	{
		// check of its a leaf
		if (r.checkIfLeaf())
		{
			for (int i = 0; i < r.getTotalItems(); i++)
			{
				r.getData(i).printData();
			}
		}
		else
		{
			for (int i = 0; i < r.getTotalItems() + 1; i++)
			{
				inorderTraversal(r.getChild(i));
				if (i < r.getTotalItems())
				{
					r.getData(i).printData();
				}
			}
		}
	}

	// Method that will sort the array

	public void sort1(int[] arr1)
	{
		int x = 0;
        // start with root
		sort1(root, arr1, x);
	}

	// private method that will help sort the array
	// using recursion
	private int sort1(Tree234Node node, int[] arr1, int x)
	{
		// check if its a leaf
		if (node.checkIfLeaf())
		{
			for (int i = 0; i < node.getTotalItems(); i++)
			{
				arr1[x] = node.getData(i).data;
				x++;
			}
			return x;
		}
		else
		{
			for (int i = 0; i < node.getTotalItems() + 1; i++)
			{
				x = sort1(node.getChild(i), arr1, x);

				if (i < node.getTotalItems())
				{
					arr1[x] = node.getData(i).data;
					x++;
				}
			}
			return x;
		}
	}

	// Method that will insert values to the tree
	public void add(int x)
	{
		// Create a new node
		Tree234Node current = root;

		// New data item for the node
		TreeData add_data = new TreeData(x);

		while(true)
		{
			if (current.checkIfFull())
			{
				splitNode(current);
				// go back and get the parent
				current = current.getParent();
				current = getNXTChild(current, x);
			}
			// check if its a leaf to exit
			else if (current.checkIfLeaf())
			{
				break;
			}
			else
			{
				current = getNXTChild(current, x);
			}
		}
		// insert the new data value
		current.addItem(add_data);
	}

	// method that will split the node when full
	public void splitNode(Tree234Node n)
	{
		TreeData rightMost;
		TreeData nextItem;
		Tree234Node parent;
		Tree234Node ch2;
		Tree234Node ch3;

		int idx;

		// remove right most data
		nextItem = n.removeData();
		// remove the next data
		rightMost = n.removeData();

		// remove the children
		ch2 = n.removeChild(2);
		ch3 = n.removeChild(3);

		Tree234Node rightNode = new Tree234Node();

		if (n == root)
		{
			// set root as new data
			root = new Tree234Node();
			parent = root;
			// add child to root
			root.addChild(0, n);
		}
		else
		{
			// set new parent
			parent = n.getParent();
		}
		// this one is the previous middle item
		idx = parent.addItem(rightMost);
		int n_items = parent.getTotalItems();

		for (int i = n_items - 1; i > idx; i--)
		{
			Tree234Node temp = parent.removeChild(i);
			// add a child the right
			parent.addChild(i + 1, temp);
		}
		// add the rightNode to the parent
		parent.addChild(idx + 1, rightNode);

		rightNode.addItem(nextItem);
		rightNode.addChild(0, ch2);
		rightNode.addChild(1, ch3);
	}

	// method that will get the next child from the node
	public Tree234Node getNXTChild(Tree234Node n, int data)
	{
		// get the total items in the node
		int num = n.getTotalItems();
		int i;
		for (i = 0; i < num; i++)
		{
			if (data < n.getData(i).data)
			{
				return n.getChild(i);
			}
		}
		return n.getChild(i);
	}

	// method that will print the values of the tree
	public void printTree()
	{
		printTree(root, 0, 0);
	}

	// private method that helps print the values of the tree
	// using recursion
	private void printTree(Tree234Node node, int l, int numb)
	{
		//System.out.print()
		node.printNode();

		int total_items_in_node = node.getTotalItems();
		for (int i = 0; i < total_items_in_node + 1; i++)
		{
			Tree234Node the_next_node = node.getChild(i);

			if(the_next_node != null)
			{
				printTree(the_next_node, l+1, i);
			}
			else
			{
				return;
			}
		}
	}

}
