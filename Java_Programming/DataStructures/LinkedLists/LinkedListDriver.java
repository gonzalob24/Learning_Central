package LinkedLists;

// import java.util.*;

public class LinkedListDriver
{

	public static void main(String[] args)
	{
		// Scanner input = new Scanner(System.in);

		LinkedList<Integer> I = new LinkedList<Integer>();
		LinkedList<Integer> I2 = new LinkedList<Integer>();
		I.insertAtEnd(33);
		I.insertAtBeginning(45);
		I.insertAtEnd(17);
		I.countNodes();
		I.display();

		I.insertAtEnd(1);
		I.insertAtEnd(10);
		I.display();

		for (int i = 0; i < 4; i++)
		{
			I.insertAtEnd(i + 3);
		}

		System.out.println("After the first loop (3,4,5,6)");
		System.out.println("--------------------------");
		I.display();

		I.insertAtBeginning(500);
		System.out.println("After inserting 500 at the front (500,3,4,5,6)");
		System.out.println("--------------------------");
		I.display();

		I.deleteNode(5);
		System.out.println("After removing element 5 (500,3,4,6)");
		System.out.println("--------------------------");
		I.display();

		for (int i = 1; i < 4; i++)
		{
			I.insertAtEnd((i * 100));
		}

		System.out.println("After inserting (100, 200, 300) at the end");
		System.out.println("--------------------------");
		I.display();

		I.listSearch(200);

		I.insertBefore(150, 200); // insert 150 before 200
		System.out.println("After the inserting 150 before 200");
		System.out.println("--------------------------");
		I.display();

		I2.insertAtEnd(88);
		I2.insertAtEnd(500);
		I2.insertAtEnd(7);
		I2.insertAtEnd(9);
		I2.insertAtEnd(200);
		I2.insertAtEnd(301);
		I2.insertAtEnd(77);
		I2.insertAtEnd(3);

		I.addList(I2);

		System.out.println("After the inserting list 2 (500, 7, 9, 200, 301)");
		System.out.println("--------------------------");
		I.display();

		I2.deleteNode(9);
		I2.deleteNode(200);
		System.out.println("After removing 9 and 200 (500, 7, 301)");
		System.out.println("--------------------------");
		I2.display();

		I.subtractList(I2); // remove elements that are the same

		System.out.println("After removing list 2");
		System.out.println("--------------------------");
		I.display();

		I.reverseList();
		System.out.println("After reversing the list");
		System.out.println("--------------------------");
		I.display();

	}

	// Static method that Displays the menu to the user
	// Still working on it. It is currently not part of my solution.
	public static void menu()
	{
		System.out.println("Select an option from the list below.");
		System.out.println("Enter number or (q) to exit the menu.\n");

		System.out.println("1.  Display list");
		System.out.println("2.  Display size of list");
		System.out.println("3.  Insert a node at the Beginning");
		System.out.println("4.  Insert a node at the End");
		System.out.println("5.  Insert a node at a certain position");
		System.out.println("6.  Insert a node AFTER a certain element");
		System.out.println("7.  Insert a node BEFORE a certain element");
		System.out.println("8.  Search for an element");
		System.out.println("9.  Reverse the list");
		System.out.println("10. Delete the first node");
		System.out.println("11. Delete the last node");
		System.out.println("12. Delete a certain element");
	}
}