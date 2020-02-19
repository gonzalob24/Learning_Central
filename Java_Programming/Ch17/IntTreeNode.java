/**
 * Class to store a single node of a binary tree
 */
public class IntTreeNode
{
	public int info;
	public IntTreeNode left;
	public IntTreeNode right;

	public IntTreeNode(int data)
	{
		this(data, null, null);
	}

	public IntTreeNode(int info, IntTreeNode left, IntTreeNode right)
	{
		this.info = info;
		this.left = left;
		this.right = right;
	}
}
