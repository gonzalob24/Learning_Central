public class SearchTree<T extends Comparable<T>>
{
	private SearchTreeNode<T> overallroot;

	public SearchTree()
	{
		overallroot = null;
	}

	/**
	 * adds a T value to the emtpty tree
	 *
	 * @param value
	 */
	public void add(T value)
	{
		overallroot = add(overallroot, value);
	}

	/**
	 * adds a T value to the overallroot of the tree
	 */
	private SearchTreeNode<T> add(SearchTreeNode<T> root, T value)
	{
		if (root == null)
		{
			root = new SearchTreeNode<T>(value);
		} else if (value.compareTo(root.info) <= 0)
		{
			root.left = add(root.left, value);
		} else
		{
			root.right = add(root.right, value);
		}

		return root;
	}

	/**
	 * returns boolean if T value is in the search tree
	 *
	 * @param value
	 * @return
	 */
	public boolean contains(T value)
	{
		return contains(overallroot, value);
	}

	private boolean contains(SearchTreeNode<T> root, T value)
	{
		if (root == null)
		{
			return false;
		} else
		{
			int compare = value.compareTo(root.info);
			if (compare == 0)
			{
				return true;
			} else if (compare < 0)
			{
				return contains(root.left, value);
			} else
			{
				return contains(root.right, value);
			}
		}
	}

	/**
	 * Prints the Search tree using inorder traversal
	 */
	public void printInorder()
	{
		System.out.println("Inorder Traversal:");
		printInorder(overallroot);
		System.out.println();
	}

	/**
	 * uses root node to print tree using inorder traversal
	 *
	 * @param root
	 */
	private void printInorder(SearchTreeNode<T> root)
	{
		if (root != null)
		{
			printInorder(root.left);
			System.out.print(root.info + " ");
			printInorder(root.right);
		}
	}

	/**
	 * prints tree in preorder starting with overallroot
	 */
	public void printPreorder()
	{
		System.out.println("Preorder Traversal:");
		printPreorder(overallroot);
		System.out.println();
	}

	/**
	 * prints tree in preorder starting with overallroot
	 */
	private void printPreorder(SearchTreeNode root)
	{
		if (root != null)
		{
			System.out.print(root.info + " ");
			printPreorder(root.left);
			printPreorder(root.right);
		}
	}

	/**
	 * Prints the tree using postorder traversal starting from root fo the tree
	 */
	public void printPostorder()
	{
		System.out.println("Postorder Traversal:");
		printPostorder(overallroot);
		System.out.println();
	}

	/**
	 * prints the tree using postorder starting with a node
	 *
	 * @param root
	 */
	private void printPostorder(SearchTreeNode root)
	{
		if (root != null)
		{
			printPostorder(root.left);
			printPostorder(root.right);
			System.out.print(root.info + " ");

		}
	}

	/**
	 * prints the tree sideways starting with root node of the tree
	 */
	public void printSideways()
	{
		System.out.println("Sideways view of the tree:");
		printSideways(overallroot, 0);
		System.out.println();

	}

	/**
	 * prints tree sideways using a node and increasing the level of the node
	 * to prints correct number of spaces
	 *
	 * @param root
	 * @param level
	 */
	private void printSideways(SearchTreeNode<T> root, int level)
	{
		if (root != null)
		{
			printSideways(root.right, level + 1);
			for (int i = 0; i < level; i++)
			{
				System.out.print("  ");
			}
			System.out.println(root.info);
			printSideways(root.left, level + 1);
		}
	}
}
