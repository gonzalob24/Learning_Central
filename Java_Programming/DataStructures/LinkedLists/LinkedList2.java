package LinkedLists;

public class LinkedList2<T> // <T> means it is a generic class
{
	private Node2<T> head;  // front of the list is called the head
	private Node2<T> cursor; // cursor is the one that moves along the list

	// Constructor
	public LinkedList2()
	{
		// an empty list the head of the list not used its always empty
		head = new Node2<T>(null, null); // since T v is an object in Node class it will be null
		cursor = head; // cursor starts in the same place as the head of the list
	}

	// if cursor == null we are at the end of the list
	public boolean isAtEnd()
	{
		return (cursor.getNext() == null);
	}

	// move the cursor to the beginning of the list
	public void reset()
	{
		cursor = head; // recall head does not move it stays at the beginning of the list
	}

	// advance the cursor one spot to the right
	public void advance()
	{
		cursor = cursor.getNext();

		// in my other class its equivalent to p = p.link b/c i have info and link
		// public in node class
	}

	// return the node to the right of the cursor
	public Node2<T> getCurrent()
	{
		return cursor.getNext();
	}

	// return the first node in the list
	public Node2<T> getFirst()
	{
		return head.getNext();
	}

	// insert an element at the beginning of the list
	// insertion is done to the right of head/start
	public void listHeadInsert(T value)
	{
		// Node<T> temp = new Node<T>(value, head.getNext());
		head.setNext(new Node2<T>(value, head.getNext())); // link of the new Node is null if new node is at the end
	}

	// Wherever the cursor is, insert a node to the right
	// then move the cursor to point to the newly inserted node
	// you may remove the line that advanced the cursor, but you need to make sure
	// that you advance the cursor when inserting elements at the end of the list
	public void listInsert(T value)
	{
		// insert to the right of the cursor

		cursor.setNext(new Node2<T>(value, cursor.getNext()));

		cursor = cursor.getNext(); // advances the cursor to the newly inserted node
	}

	// move the cursor across the list and stop if you find the value
	// or you reach the end of the list.
	// return the node that contains the value
	// return null if the value is not found

	public Node2<T> listSearch(T value)
	{
		// when we search for a value we start at the beginning
		cursor = head; // start the cursor at the beginning
		while (cursor.getNext() != null && !cursor.getNext().getValue().equals(value))
		{
			cursor = cursor.getNext();
		}
		return cursor.getNext(); // returns the node
	}

	// removing a value from the list
	public void listRemove(T value)
	{
		// Again start at the beginning
		cursor = head; // start cursor at the beginning

		while (cursor.getNext() != null && !cursor.getNext().getValue().equals(value))
		{
			cursor = cursor.getNext();
		}

		if (cursor.getNext() != null)
		{
			cursor.setNext(cursor.getNext().getNext());
		}
	}

	// Method that reverses the link
	public void reverseList()
	{
		cursor = head;
		cursor.getValue();
	}

}
