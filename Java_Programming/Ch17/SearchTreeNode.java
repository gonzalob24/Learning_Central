public class SearchTreeNode<T extends Comparable<T>>
{
    public T info;
    public SearchTreeNode<T> left;
    public SearchTreeNode<T> right;

    public SearchTreeNode(T info)
    {
        this(info, null, null);
    }

    public SearchTreeNode(T info, SearchTreeNode<T> left, SearchTreeNode<T> right)
    {
        this.info = info;
        this.left = left;
        this.right = right;
    }

}
