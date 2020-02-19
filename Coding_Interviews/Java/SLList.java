public class SLList<T>
{
    private int size;
    private Node<T> header;

    public SLList()
    {
        header = new Node("Start", null);
        size = 0;
    }

    public SLList(T value)
    {
        header = new Node("Start", null);
        header.next = new Node(value, header.next);
        size ++;
    }

    public void addFront(T value)
    {
        header.next = new Node(value, header.next);
        size++;
    }

    public T removeFirst()
    {
        T first_item = header.next.info;
        header.next = header.next.next;
        size--;
        return first_item;
    }

    public void addLast(T value)
    {
        Node p = header;
        Node temp = new Node(value, null);

        while(p.next != null)
        {
            p = p.next;
        }
        p.next = temp;
        size++;
    }

    public void insert(T value, int position)
    {
        Node<T> p = header.next;
        int idx = 1;

        while (p.next != null && idx < position - 1)
        {
            idx++;
            p = p.next;
        }
        Node<T> temp = new Node(value, p.next);
        p.next = temp;
        size++;
    }

    public void display()
    {
        Node p = header.next;
        while(p != null)
        {
            System.out.print(p.info + " ");
            p = p.next;
        }
        System.out.println();
    }
}
