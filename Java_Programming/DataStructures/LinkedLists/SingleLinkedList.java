package LinkedLists;

import java.util.*;

public class SingleLinkedList<T>
{
	private Node1<T> start; // refers to the first node of the list

	// Initialize SLL to null
	public SingleLinkedList()
	{
		start = null;
	}

	// display linked list
	public void displayList()
	{
		Node1<T> p;
		if (start == null)
		{
			System.out.println("List is empty");
			return;
		}
		System.out.print("The list is: ");
		p = start;

		while (p != null)
		{
			System.out.print(p.info + " ");
			p = p.link;
		}
		System.out.println();
	}// end of display list

	// count the nodes in the list
	public void countNodes()
	{
		int n = 0;
		Node1<T> p = start;

		while (p != null)
		{
			n++;
			p = p.link;
		}
		System.out.println("The number of nodes in the list = " + n);
	}

	// Searched for a value in the node
	public boolean search(T x)
	{
		Node1<T> p = start;
		int position = 1;  // keep track of position on the list
		while (p != null)
		{
			if (p.info.equals(x))
			{
				break;
			}
			position++;
			p = p.link;
		}
		if (p == null)
		{
			System.out.println(x + " is not in the list");
			return false;
		} else

		{
			System.out.println(x + " is at position " + position);
			return true;
		}
	}

	// will add a node at the end of the list
	public void insertAtEnd(T data)
	{
		Node1<T> p;
		Node1<T> temp = new Node1<T>(data);

		if (start == null)
		{
			start = temp;
			return;
		}
		p = start;
		while (p.link != null)
		{
			p = p.link;
		}
		p.link = temp;
	}

	// Insert node at the beginning of the linked list
	public void insertAtBeginning(T data)
	{
		Node1<T> temp = new Node1<T>(data); // Temp Node

		if (start == null)
		{
			start = temp;
			return;
		}
		temp.link = start;
		start = temp;
	}

	// Insert node after a particular info
	public void insertAfter(T data, T x)
	{
		Node1<T> p = start;
		Node1<T> temp = new Node1<T>(data);
		while (p != null)
		{
			if (p.info == x)
			{
				break;
			}
			p = p.link;
		}
		if (p == null)
		{
			System.out.println(x + " is not present in the list");
		} else
		{
			temp.link = p.link;
			p.link = temp;
		}

	}

	// Insert before particular info
	public void insertBefore(T data, T x)
	{
		Node1<T> p = start;
		Node1<T> temp = new Node1<T>(data);
		if (start == null)
		{
			System.out.println("The list is empty");
			return;
		}
		// x is in the first node
		if (x == start.info)
		{
			temp.link = start;
			start = temp;
			return;
		}
		while (p.link != null)
		{
			if (p.link.info == x)
			{
				break;
			}
			p = p.link;
		}
		if (p.link == null)
		{
			System.out.println(x + " is not in the list");
		} else
		{
			temp.link = p.link;
			p.link = temp;
		}
	}

	// insert at a particular position in the list
	public void insertAtPosition(T data, int pos)
	{
		Node1<T> p = start;
		Node1<T> temp = new Node1<T>(data);
		int idx;
		if (pos == 1)
		{
			temp.link = start;
			start = temp;
			return;
		}

		for (idx = 1; idx < pos - 1 && p.link != null; idx++)
		{
			p = p.link;
		}

		if (p.link == null)
		{
			System.out.println("You can only insert up to " + idx + "th position");
		} else
		{
			temp.link = p.link;
			p.link = temp;
		}
	}

	// Delete the first node
	public void deleteFirstNode()
	{
		// Node1<T> p = start;
		if (start == null)
		{
			System.out.println("The list is empty");
			return;
		}
		start = start.link;
	}

	// Delete the last node
	public void deleteLastNode()
	{
		Node1<T> p = start;
		if (start == null)
		{
			System.out.println("The list is empty");
			return;
		}

		if (start.link == null)
		{
			start = null;
			return;
		}
		while (p.link.link != null)
		{
			p = p.link;
		}
		p.link = null;
	}

	// Delete node with particular info
	public void deleteData(T x)
	{
		Node1<T> p = start;
		if (start.info == x)
		{
			start.link = null;
			return;
		}
		while (p.link != null)
		{
			if (p.link.info == x)
			{
				break;
			}
			p = p.link;
		}
		if (p.link == null)
		{
			System.out.println("The element " + x + " is not in the list");
		} else
		{
			p.link = p.link.link;
		}
	}

	// reversing a single linked list
	public void reverseList()
	{
		Node1<T> p = start;
		Node1<T> prev = null;
		Node1<T> next;

		while (p != null)
		{
			next = p.link;
			p.link = prev;
			prev = p;
			p = next;
		}
		start = prev;
	}

	// create a Linked list
	public void createList()
	{
		Scanner input = new Scanner(System.in);

		System.out.print("Enter the number of elements you want to add: ");
		int number_nodes = input.nextInt();

		if (number_nodes == 0)
		{
			return;
		}
		for (int i = 1; i <= number_nodes; i++)
		{
			System.out.print("Enter the element to be inserted: ");
			T data = (T) input.next();
			insertAtEnd(data);
		}
	}// end of creating linked list
}
