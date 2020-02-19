package LinkedLists;

public class Node1<T>
{
	public T        info;  // actual data that needs to be in the node
	public Node1<T> link;  // link is type node and refers to the next node

	// Constructor
	public Node1(T i)
	{
		info = i;
		link = null;
	}
}
