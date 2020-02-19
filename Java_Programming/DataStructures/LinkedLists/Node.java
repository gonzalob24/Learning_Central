package LinkedLists;

// Node class to create nodes when needed
public class Node<T>
{
	public T       info;			// actual data that needs to be in the node
	public Node<T> next;			// link is type node and refers to the next node

	public Node(T value)
	{
		this(value, null);
	}

	public Node(T info, Node next)
	{
		this.info = info;
		this.next = next;
	}
}
