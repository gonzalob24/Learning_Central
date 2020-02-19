
/*
 * Write a method countUnique that takes a List of integers as a parameter and
 * returns the number of unique integer values in the list. Use a Set as
 * auxiliary storage to help you solve this problem.
 * 
 * For example, if a list contains the values [3, 7, 3, -1, 2, 3, 7, 2, 15, 15],
 * your method should return 5. The empty list contains 0 unique values.
 */
import java.util.*;

public class CountUnique
{

	public static void main(String[] args)
	{
		List<Integer> list1 = new LinkedList<Integer>();
		list1.add(0);
		list1.add(0);
		list1.add(2);
		list1.add(0);
		list1.add(4);
		list1.add(0);
		list1.add(6);
		list1.add(0);
		list1.add(8);
		list1.add(0);
		list1.add(10);
		list1.add(0);
		list1.add(12);
		list1.add(0);
		list1.add(14);
		list1.add(0);
		list1.add(16);
		System.out.println(list1);
		System.out.println(countUnique(list1));

	}

	public static int countUnique(List<Integer> list1)
	{
		Set<Integer> result = new HashSet<Integer>(list1);
		System.out.println(result);
		return result.size();
	}

}
