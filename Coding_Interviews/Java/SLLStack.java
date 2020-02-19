public class SLLStack<T> implements StackInterface<T>
{
    private Node<T> header;
    private int size;

    public SLLStack()
    {
        header = new Node("Start", null);
        size = 0;
    }

    public void push(T value)
    {
        header.next = new Node(value, header.next);
    }

    public T pop()
    {
        T popped_item = header.next.info;
        header.next = header.next.next;
        return popped_item;
    }

    public void display()
    {
        Node<T> p = header.next;
        while (p != null)
        {
            System.out.print(p.info + " ");
            p = p.next;
        }
        System.out.println();
    }
}
