package LinkedLists;

import java.util.*;

public class LinkedList<T>
{
	private Node<T> head;  // refers to the head of the list, the very front
	private Node<T> cursor; // cursor is the one that moves along the list

	public LinkedList()
	{
		head = null;	// The head or dummy node is always null
	}

	// if cursor == null we are at the end of the list
	public boolean isAtEnd()
	{
		return (cursor.next == null);
	}

	// Method that checks to see if the list is empty
	public boolean isEmpty()
	{
		return (head == null);
	}

	// move the cursor to the beginning of the list
	public void reset()
	{
		cursor = head; // recall head does not move it stays at the beginning of the list
	}

	// counts the number of nodes in the list
	// prints the size of the linked list
	public void countNodes()
	{
		int n = 0;
		cursor = head;
		while (cursor != null)
		{
			n++;
			advance();
		}
		System.out.println("The number of nodes in the list = " + n);
	}

	// advance the cursor one spot to the right
	public void advance()
	{
		cursor = cursor.next;

		// in my other class its equivalent to p = p.link b/c i have info and link
		// public in node class
	}

	// returns the node to the right of the cursor
	public Node<T> getCurrent()
	{
		return cursor.next;
	}

	// return the first node in the list
	public Node<T> getFirst()
	{
		return head.next;
	}

	// insert an element at the beginning of the list
	// insertion is done to the right of head/start
	public void insertAtBeginning(T data)
	{
		Node<T> temp = new Node<T>(data); // creates the node that we want to insert

		temp.next = head; // temp.next points to where head is pointing
		head = temp;
	}

	// Inserts a node at the end of the list
	public void insertAtEnd(T data)
	{

		// insert temp node to the right of the cursor
		Node<T> temp = new Node<T>(data); // creates the node that we want to insert

		// check to see if the start of the list is null then its empty
		// add node as first element
		if (head == null)
		{
			head = temp;
			return;
		}
		cursor = head;
		while (cursor.next != null)
		{
			cursor = cursor.next;
		}
		cursor.next = temp;
	}

	// insert a node before a certain data
	public void insertBefore(T data, T x)
	{
		cursor = head;
		Node<T> temp = new Node<T>(data);
		// if beginning is null list is empty
		if (head == null)
		{
			System.out.println("The list is empty");
			return;
		}
		// x is in the first node
		if (cursor.info == x)
		{
			temp.next = head;
			head = temp;
			return;
		}
		// Find a reference to the predecessor of the node containing x
		while (cursor.next != null)
		{
			if (cursor.next.info.equals(x))
			{
				break;
			}
			cursor = cursor.next;
		}
		if (cursor.next == null)

		{
			System.out.println(x + " is not in the list");
		} else
		{
			temp.next = cursor.next;
			cursor.next = temp;
		}
	}

	// Method that will insert a node after a particular node
	public void insertAfter(T data, T x)
	{
		cursor = head;
		Node<T> temp = new Node<T>(data);

		while (cursor != null)
		{
			if (cursor.info.equals(x))
			{
				break;
			}
			cursor = cursor.next;
		}

		if (cursor == null)
		{
			System.out.println(x + " is not present in the list");
		} else
		{
			temp.next = cursor.next;
			cursor.next = temp;
		}
	}

	// Method that inserts a node after a certain position in the list
	public void insertAtPosition(T data, int position)
	{
		cursor = head;
		Node<T> temp = new Node<T>(data);
		int index = 1;
		if (position == 1)
		{
			temp.next = cursor;
			head = temp;
			return;
		}

		while (index < position - 1 && cursor.next != null)
		{
			index++;
			cursor = cursor.next;
		}
		if (cursor == null)
		{
			System.out.println("You can only insert up to " + index + "th position");
		} else
		{
			temp.next = cursor.next;
			cursor.next = temp;
		}
	}

	// move the cursor across the list and stop if you find the data
	// or you reach the end of the list.
	// return the node that contains the data
	// return null if the data is not found

	public void listSearch(T data)
	{
		// when we search for a data we start at the beginning
		cursor = head; // start the cursor at the beginning
		int position = 1; // keeps track of the position in the list
		while (cursor != null)
		{
			if (cursor.info.equals(data))
			{
				break;
			}
			position++;
			cursor = cursor.next;
		}
		if (cursor == null)
		{
			System.out.println(data + " is not in the list.\n");
			// return null; // returns the node
		} else
		{
			System.out.println("Searched and found the data " + data + "." + " It's at position " + position + "\n");
			// return cursor.next;
		}
	}

	public Node<T> search(T data)
	{
		// when we search for a data we start at the beginning
		cursor = head; // start the cursor at the beginning
		while (cursor != null)
		{
			if (cursor.info.equals(data))
			{
				break;
			}
			cursor = cursor.next;
		}
		return cursor;
	}

	// removing a data from the list
	public void deleteNode(T data)
	{
		// Again start at the beginning
		cursor = head; // start cursor at the beginning

		// first check if data is at the first node
		if (head == null)
		{
			System.out.println("The list is empty");
			return;
		}
		// Deleting the first node of the list
		if (head.info.equals(data))
		{
			head = head.next;
			return;
		}

		// deleting in between or at the end
		while (cursor.next != null)
		{
			if (cursor.next.info.equals(data))
			{
				break;
			}

			cursor = cursor.next;
		}

		if (cursor.next == null)
		{
			System.out.println("The element " + data + " is not in the list");
		} else
		{
			cursor.next = cursor.next.next;
		}
	}

	// Deletes the first node of the list
	public void deleteFirstNode()
	{
		// check to see if the list is emptu
		if (head == null)
		{
			System.out.println("The list is empty");
		}
		head = head.next;
	}

	// method that deletes the last node of the list
	public void deleteLastNode()
	{
		// Check if list is empty
		if (head == null)
		{
			System.out.println("The list is empty");
			return;
		}
		// delete the first node in the list
		if (head.next == null)
		{
			head = null;
			return;
		}
		cursor = head;
		while (cursor.next.next != null)
		{
			cursor = cursor.next;
		}
		cursor.next = null;
	}

	// reversing a single linked list
	public void reverseList()
	{
		cursor = head;
		Node<T> prev = null; // initially this will be null
		Node<T> next_cursor;

		while (cursor != null)
		{
			next_cursor = cursor.next;
			cursor.next = prev;
			prev = cursor;
			cursor = next_cursor;
		}
		head = prev;
	}

	// Method that will add two lists together and not include repeating
	// nodes.
	public void addList(LinkedList<T> list2)
	{
		Node<T> secondTemp = list2.head;
		Node<T> searchDuplicates;

		while (secondTemp != null)
		{
			searchDuplicates = search(secondTemp.info);
			if (searchDuplicates == null)
			{
				this.insertAtEnd(secondTemp.info);
			} else
			{
				secondTemp = secondTemp.next;
			}
		}
	}

	// Method that will subtract two lists and will remove elements
	public void subtractList(LinkedList<T> list2)
	{
		Node<T> secondTemp = list2.head;
		Node<T> searchDuplicates;

		while (secondTemp != null)
		{
			searchDuplicates = search(secondTemp.info);
			if (searchDuplicates != null)
			{
				this.deleteNode(secondTemp.info);
			} else
			{
				secondTemp = secondTemp.next;
			}
		}
	}

	// Method that will create a linked list
	// user decides on how many elements it will have
	// user will manually input the elements on the list
	public void createList()
	{
		Scanner input = new Scanner(System.in);

		System.out.print("Please enter the number of elements you want to add: ");
		int number_of_nodes = input.nextInt();

		if (number_of_nodes == 0)
		{
			return;
		}
		for (int i = 1; i <= number_of_nodes; i++)
		{
			System.out.print("Enter the element to be inserted: ");
			String data2 = input.next();
			T data = (T) data2;
			insertAtEnd(data);
		}
	}

	// Method that will find a cycle in a linked list

	// Displays the nodes of a list
	public void display()
	{
		cursor = head;
		if (head == null)
		{
			System.out.println("List is empty");
			return;
		}
		// System.out.print("The list is: ");

		while (cursor != null)
		{
			System.out.println(cursor.info);
			advance();
		}
		System.out.println("\n");
	}// end of display list
}
