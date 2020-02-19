package LinkedLists;

public class Node2<T>  // A class Node for generic types
{
	private T        value;  // data that goes into node
	private Node2<T> next;	// stores the link to next node

	public Node2(T v, Node2<T> n) // default constructor
	{
		value = v;
		next = n;
	}

	// getters and setters for the node's value and next pointer
	public T getValue()
	{
		return value;
	}

	public Node2<T> getNext()
	{
		return next;
	}

	public void setValue(T v)
	{
		value = v;
	}

	public void setNext(Node2<T> n)
	{
		next = n;
	}
}
