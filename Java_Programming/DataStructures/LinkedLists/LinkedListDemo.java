package LinkedLists;

import java.util.*;

public class LinkedListDemo
{

	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		SingleLinkedList<Integer> list1 = new SingleLinkedList<Integer>();
		list1.displayList(); // currently list is empty
		list1.createList();

		list1.displayList();
		list1.insertAtEnd(500);
		list1.displayList();
		list1.deleteData(5);
		list1.search(4);
		list1.displayList();
		list1.deleteLastNode();
		list1.displayList();
		list1.reverseList();
		list1.displayList();
	}

}
