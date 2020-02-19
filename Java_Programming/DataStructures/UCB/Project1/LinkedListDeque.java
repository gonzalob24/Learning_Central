package UCB.Project1;

import UCB.Project1B.ASLList;

import java.util.Dictionary;
import java.util.EmptyStackException;

public class LinkedListDeque<Any> implements ASLList<Any>
{
	//private DIntNode front;
	//private DIntNode rear;
	private DIntNode<Any> header;
	private int size;

	//empty LinkedListDeque with header node
	public LinkedListDeque()
	{
		header = new DIntNode(63, null, null);
		header.prev = header;
		header.next = header;
		//front = null;
		//rear = null;
		size = 0;
	}

	// method that created a deep copy of other. If you change other the new LinkedListDeque should not change
	// They will be two different objects.
	public LinkedListDeque(LinkedListDeque other)
	{
		//DIntNode header = new DIntNode(63);
		//header.prev = header;
		//header.next = header;
		//size = 0;
		//for (int i = 0; i< other.size(), i++)
		//  addLast(other.get(i))
	}

	//method that checks if deque is empty
	@Override
	public boolean isEmpty()
	{
		return size == 0;
	}

	//Mehtod that will add a node to the beginning of the deque
	@Override
	public void addFirst(Any x)
	{
		// newd DIntNode temp = new DIntNode(x); // I also need to change the DIntNode class for the other implementation
		//		if (this.isEmpty())
		//		{
		//			this.front = this.rear = temp;
		//		} else
		//		{
		//			temp.next = front;
		//			front.prev = temp;
		//			front = temp;
		//		}
		DIntNode<Any> temp = new DIntNode(x, header, header.next);
		header.next.prev = temp;
		header.next = temp;
		size++;
	}

	//method that will add a node to the end
	@Override
	public void addLast(Any x)
	{
		//
		//		if (this.isEmpty())
		//		{
		//			this.front = this.rear = temp;
		//		} else
		//		{
		//			rear.next = temp;
		//			temp.prev = rear;
		//			rear = temp;
		//		}

		DIntNode<Any> temp = new DIntNode(x, header.prev, header);
		header.prev.next = temp;
		header.prev = temp;
		size++;
	}

	//method that will return the size of the dequeue
	@Override
	public int size()
	{
		return size;
	}

	//method that will remove a node from the front
	@Override
	public Any removeFirst()
	{
		//this.front = front.next;
		//this.front.prev = null;
		if (size == 0)
		{
			throw new EmptyStackException();
		} else
		{
			Any first_item = header.next.item;
			header.next = header.next.next;
			header.next.prev = header;

			size--;
			return first_item;
		}
	}

	/**
	 * ]
	 * Returns the first item from the list
	 * does not modify the list
	 */
	@Override
	public Any getFirst()
	{
		//this.front = front.next;
		//this.front.prev = null;
		if (size == 0)
		{
			throw new EmptyStackException();
		} else
		{
			Any first_item = header.next.item;
			return first_item;
		}
	}

	//method that will delete an item/node from the rear
	@Override
	public Any removeLast()
	{
		//this.rear = rear.prev;
		//this.rear.next = null;
		Any last_item = header.prev.item;
		header.prev = header.prev.prev;
		header.prev.next = header;
		size--;
		return last_item;
	}

	/**
	 * returns the last item from the list
	 * does not modigy the list
	 */
	@Override
	public Any getLast()
	{
		//this.rear = rear.prev;
		//this.rear.next = null;
		if (size == 0)
		{
			throw new EmptyStackException();
		} else
		{
			Any last_item = header.prev.item;
			return last_item;
		}
	}

	//method that will get the item at the given index. starting with 0
	@Override
	public Any get(int index_i)
	{
		//DIntNode p = front; //have a reference to the front of the deque
		//		DIntNode p = front;
		//		int position = 0;
		//		while (p != null && position != index_i)
		//		{
		//			position++;
		//			p = p.next;
		//		}
		//		return p.item;
		if (index_i >= size || index_i < 0)
		{
			throw new EmptyStackException();
		} else
		{
			DIntNode<Any> p = header.next;
			int position = 0;
			while (position != index_i)
			{
				position++;
				p = p.next;
			}
			return p.item;
		}
	}

	/**
	 * this time the getsValue will be implemented using recursion
	 */
	public Any getValueWithRecursion(int index_i)
	{
		if (index_i > size || index_i == 0)
		{
			throw new EmptyStackException();
		} else
		{
			return getValueRecursionHelper(header.next, index_i);
		}
	}

	/**
	 * Private recursive help method
	 */
	private Any getValueRecursionHelper(DIntNode<Any> pointer, int index)
	{
		//base case if index == 0
		if (index == 1)
		{
			return pointer.item;
		} else
		{
			return getValueRecursionHelper(pointer.next, index - 1);
		}
	}

	/**
	 * Inserts an type into the given position
	 */
	@Override
	public void insert(Any x, int index)
	{
		int position = 1;
		DIntNode<Any> p = header;
		while (p.next != header && position <= index - 1)
		{
			p = p.next;
			position++;
		}

		DIntNode<Any> temp = new DIntNode(x, p, p.next);
		p.next = temp;
		p.next.prev = temp;
		size++;
	}

	//method that will display the deque
	public void display()
	{
		//DIntNode p = front;
		DIntNode<Any> p = header.next;
		while (p != header)
		{
			System.out.print(p.item + " ");
			p = p.next;
		}
		System.out.println("\n");
	}

}
