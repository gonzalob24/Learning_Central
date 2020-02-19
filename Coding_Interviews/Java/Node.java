public class Node<T>
{
    public T info;
    public Node<T> next;

    public Node(T info, Node next)
    {
        this.info = info;
        this.next = next;
    }
}
