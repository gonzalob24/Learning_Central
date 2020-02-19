public class IntTree
{
    private IntTreeNode overallRoot;

    /**
     * pre: max >= 0 throws IllegalArgumentException if not
     * post: constructs a sequential tree with given max
     *
     * @param max
     */
    public IntTree(int max)
    {
        if (max < 0)
        {
            throw new IllegalArgumentException("Max: " + max);
        }
        overallRoot = buildTree(1, max);
    }

    /**
     * Private method that will help construct a binary tree
     * n is the root unless n is greater than max in which case the tree is empty
     */
    private IntTreeNode buildTree(int n, int max)
    {
        if (n > max)
        {
            return null;
        } else
        {
            // IntTreeNode left = buildTree(2 * n, max);
            // IntTreeNode right = buildTree(2 * n + 1, max);
            // return new IntNode (n, left, right); or on one line
            return new IntTreeNode(n, buildTree(2 * n, max), buildTree(2 * n + 1, max));
        }
    }

    /**
     * prints the preorder traversal of the binary tree
     */
    public void printPreorder()
    {
        System.out.print("Preorder: ");
        printPreorder(overallRoot);
        System.out.println();

    }

    /**
     * helper method for the printPreorder()
     */
    private void printPreorder(IntTreeNode root)
    {
        //base case
        if (root != null)
        {
            System.out.print(root.info + " ");
            printPreorder(root.left);
            printPreorder(root.right);
        }
    }

    /**
     * prints the inorder traversal of the binary tree
     */
    public void printInorder()
    {
        System.out.print("Inorder: ");
        printInorder(overallRoot);
        System.out.println();

    }

    /**
     * helper method to print binary tree inorder
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
     * prints postOrder treversal
     */
    public void printPostorder()
    {
        System.out.print("Postorder: ");
        printPostorder(overallRoot);
        System.out.println();
    }

    /**
     * Private method that will help with printing postOrder
     */
    private void printPostorder(IntTreeNode root)
    {
        if (root != null)
        {
            printPostorder(root.left);
            printPostorder(root.right);
            System.out.print(root.info + " ");
        }
    }

    /**
     * Method that prints the tree sideways
     */
    public void printSideways()
    {
        printSideways(overallRoot, 0);
    }

    /**
     * Private method that will help with printing the tree sideways
     */
    private void printSideways(IntTreeNode root, int level)
    {
        // base case
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

    /**
     * calculates the sum of the values of a tree
     */
    public int sumOfTree()
    {
        return sumOfTree(overallRoot);
    }

    /**
     * private method that will help calculating the sum
     */
    private int sumOfTree(IntTreeNode root)
    {
        //base case when root -- null
        if (root == null)
        {
            return 0;
        } else
        {
            return root.info + sumOfTree(root.left) + sumOfTree(root.right);
        }
    }

    /**
     * returns the levels in a tree
     */
    public int countLevels()
    {
        return countLevels(overallRoot);
    }

    /**
     * private method that will help countLevels
     */
    private int countLevels(IntTreeNode root)
    {
        // base case
        if (root == null)
        {
            return 0;
        } else
        {
            return 1 + Math.max(countLevels(root.left), countLevels(root.right));
        }
    }

    /**
     * counting the number of leaves in a tree
     */
    public int countLeaves()
    {
        return countLeaves(overallRoot);
    }

    /**
     * private method that will help countLeaves
     */
    private int countLeaves(IntTreeNode root)
    {
        if (root == null)
        {
            return 0;
        } else if (root.left == null && root.right == null)
        {
            return 1;
        } else
        {
            return countLeaves(root.left) + countLeaves(root.right);
        }
    }

}
