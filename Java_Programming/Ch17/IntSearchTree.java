public class IntSearchTree
{
    private IntTreeNode overallroot;

    /**
     * Constructs an empty tree
     */
    public IntSearchTree()
    {
        overallroot = null;
    }

    /**
     * add values to the int tree
     */
    public void add(int value)
    {
        overallroot = add(overallroot, value);
    }

    /**
     * private method that helps add the values
     * returns the root value added
     */
    private IntTreeNode add(IntTreeNode root, int value)
    {
        if (root == null)
        {
            root = new IntTreeNode(value);
        } else if (value <= root.info)
        {
            root.left = add(root.left, value);
        } else
        {
            root.right = add(root.right, value);
        }
        return root;
    }

    /**
     * Method that checks if the tree contains stated value
     */
    public boolean contains(int value)
    {
        return contains(overallroot, value);
    }

    /**
     * Private method that will help in finding if tree has such value
     */
    private boolean contains(IntTreeNode root, int value)
    {
        if (root == null)
        {
            return false;
        } else if (value == root.info)
        {
            return true;
        } else if (value < root.info)
        {
            return contains(root.left, value);

        } else
        {
            return contains(root.right, value);
        }
    }

    /**
     * Prints contents in inorder traversal
     */
    public void printInorder()
    {
        System.out.print("Inorder: ");
        printInorder(overallroot);
        System.out.println();
    }

    /**
     * private helper method that prints contents of the tree given root in inorder traversal
     */
    private void printInorder(IntTreeNode root)
    {
        if (root != null)
        {
            printInorder(root.left);
            System.out.print(root.info + " ");
            printInorder(root.right);
        }
    }

    /**
     * prints the contents of the tree sideways one per line
     * Using indentation to indicate node depth
     */
    public void printSideways()
    {
        System.out.println("Sideways view of Tree:");
        printSideways(overallroot, 0);
    }

    /**
     * private method that prints a sideways view of the tree
     * using indentation and root node
     */
    private void printSideways(IntTreeNode root, int level)
    {
        if (root != null)
        {
            printSideways(root.right, level + 1);
            for (int i = 0; i < level; i++)
            {
                System.out.print("\t");
            }
            System.out.println(root.info);
            printSideways(root.left, level + 1);
        }
    }

}
