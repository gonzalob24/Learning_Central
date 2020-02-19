
/*
 * Write a method called alternate that accepts two Lists of integers as its
 * parameters and returns a new List containing alternating elements from the
 * two lists, in the following order:
 * 
 * First element from first list First element from second list Second element
 * from first list Second element from second list Third element from first list
 * Third element from second list
 * 
 * If the lists do not contain the same number of elements, the remaining
 * elements from the longer list should be placed consecutively at the end. For
 * example, for a first list of (1, 2, 3, 4, 5) and a second list of (6, 7, 8,
 * 9, 10, 11, 12), a call of alternate(list1, list2) should return a list
 * containing (1, 6, 2, 7, 3, 8, 4, 9, 5, 10, 11, 12). Do not modify the
 * parameter lists passed in.
 */

import java.util.*;

public class Alternate
{

	public static void main(String[] args)
	{
		List<Integer> list1 = new LinkedList<Integer>();
		List<Integer> list2 = new LinkedList<Integer>();
		list1.add(1);
		list1.add(2);
		list1.add(3);
		list1.add(4);
		list1.add(5);

		list2.add(6);
		list2.add(7);
		list2.add(8);
		list2.add(9);
		list2.add(10);
		list2.add(11);
		list2.add(12);
		// alternate(list1, list2);
		System.out.println(alternate2(list1, list2));
		System.out.println("This is for alternate2");
		System.out.println(alternate2(list1, list2));
	}

	// Method that alternates between both lists to create a new one.
	public static List<Integer> alternate2(List<Integer> list1, List<Integer> list2)
	{
		List<Integer> result = new LinkedList<Integer>();
		Iterator<Integer> first = list1.iterator();
		Iterator<Integer> second = list2.iterator();

		boolean flag = true;

		while (flag)
		{
			if (first.hasNext())
			{
				int num = first.next();
				result.add(num);
			}

			if (second.hasNext())
			{
				int num2 = second.next();
				result.add(num2);
			}
			if (!first.hasNext() && !second.hasNext())
			{
				flag = false;
			}
		}
		return result;
	}
}
