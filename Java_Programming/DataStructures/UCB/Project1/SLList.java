package UCB.Project1;


import UCB.Project1B.ASLList;

public class SLList<Any> implements ASLList<Any>
{
	//private SLListNode first;
	// The first item if it exists is located at header.next
	private SLListNode<Any> header; //header node for special cases like adding to end on an empty list
	private int size;

	// Creates an empty SLList
	public SLList()
	{
		header = new SLListNode(63, null);
		size = 0;
	}

	public SLList(Any x)
	{
		header = new SLListNode(63, null);
		header.next = new SLListNode(x, null);
		size = size + 1;  //this is called caching; putting aside data to speed up retrieval
	}

	//add a node to the beginning of the list
	@Override
	public void addFirst(Any x)
	{
		//SLListNode temp = new SLListNode(x, null);
		//temp.next = header;
		//header.next = temp;
		header.next = new SLListNode(x, header.next);
		size++;
		//first = new SLListNode(x, first);
	}

	//Method that deletes the first node of the SLList
	@Override
	public Any removeFirst()
	{
		Any first_item = header.next.item;
		header.next = header.next.next;
		size--;
		return first_item;
	}

	// returns the first item in the list
	@Override
	public Any getFirst()
	{

		return header.next.item;
	}

	//add to the end of the list
	@Override
	public void addLast(Any x)
	{

		SLListNode temp = new SLListNode(x, null);
		SLListNode p = header;
		while (p.next != null)
		{
			p = p.next;
		}

		p.next = temp;
		size++;

	}

	//get the last item
	@Override
	public Any getLast()
	{
		SLListNode<Any> p = header;

		while (p.next != null)
		{
			p = p.next;
		}
		return p.item;
	}

	/**
	 * Removes the last item from the list
	 */
	@Override
	public Any removeLast()
	{
		SLListNode<Any> p = header;

		while (p.next.next != null)
		{
			p = p.next;
		}
		Any last_item = p.next.item;
		p.next = null;
		return last_item;
	}

	/**
	 * returns the elements at the given position
	 */
	@Override
	public Any get(int x)
	{
		SLListNode<Any> p = header.next;
		int index = 1;
		while (index != x)
		{
			p = p.next;
			index++;

		}
		return p.item;

	}

	/**
	 * Inserts item into the given position
	 */
	@Override
	public void insert(Any x, int position)
	{
		SLListNode<Any> p = header;


		int index = 1;
		while (p.next != null && index <= position - 1)
		{
			p = p.next;
			index++;
		}
		SLListNode<Any> temp = new SLListNode(x, p.next);
		//temp.next = p.next;
		p.next = temp;
	}

	//returns the size of SLList
	public int size_using_iteration()
	{
		SLListNode p = header.next;
		int count = 0;
		while (p != null)
		{
			count++;
			p = p.next;
		}
		return count;
	}

	//Helper function
	//Recursive method that will return the size of the list
	private static int size(SLListNode p)
	{
		//recall private static method means that the private method will not
		//attempt to access information in SLList
		if (p.next == null)
		{
			return 1;
		} else
		{
			return 1 + size(p.next);
		}
	}

	/**
	 * returns the current size of the SLList using the helper recursive method above
	 */
	@Override
	public int size()
	{
		if (header.next == null)
			return 0;
		return size(header.next);
	}

	// A size method that is much faster than the previous one
	public int fastSize()
	{
		return size;
	}

	/**
	 * Reverses the items in the SLList
	 */
	public void reverse()
	{
		if (isEmpty())
		{
			System.out.println("The list is empty");
		}

		SLListNode p = header.next;
		SLListNode next_node;
		SLListNode prev = null;

		while (p != null)
		{
			next_node = p.next;
			p.next = prev;
			prev = p;
			p = next_node;
		}
		header.next = prev;

	}

	/**
	 * checks if the SLList is empty
	 */
	@Override
	public boolean isEmpty()
	{
		return size == 0;
	}

	/**
	 * display method
	 */
	@Override
	public void print()
	{
		//		SLListNode p = header.next;
		//		while (p != null)
		//		{
		//			System.out.print(p.item + " ");
		//			p = p.next;
		//		}
		//		System.out.println();
		System.out.println("The override");
		for (SLListNode p = header.next; p != null; p = p.next)
		{
			System.out.print(p.item + " ");
		}
		System.out.println();
	}
}
