package UCB.Project1;

import java.util.Arrays;
import java.util.Collections;

public class SLListTest
{
	public static void main(String[] args)
	{
		SLList<Integer> list = new SLList<>();


		//list.addEnd(1);
		list.addFirst(23);
		list.addFirst(44);
		list.addFirst(89);
		list.addFirst(45);
		list.addFirst(56);
		list.addFirst(15);
		list.addFirst(155);
		System.out.print(list.removeFirst());
		System.out.println("\nThe size of the list is " + list.size());
		list.print();
		list.addFirst(33);
		list.addLast(59);
		list.addLast(100);
		list.addLast(201);
		list.addFirst(20202);
		list.addFirst(1111);
		list.addLast(101010);

		System.out.println("First is " + list.getFirst());
		System.out.println("Last is " + list.getLast());
		System.out.println("The size of the list is " + list.size_using_iteration());
		System.out.println("The size of the list is " + list.size());
		System.out.println("The size of the list is " + list.fastSize());
		list.print();
		list.removeLast();
		list.print();
		System.out.println("The size of the list after deletion " + list.fastSize());
		System.out.println("First is " + list.get(1));




	}
}
