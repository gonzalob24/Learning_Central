
/*
 * Write a method countCommon that takes two Lists of integers as parameters and
 * returns the number of unique integers that occur in both lists. Use one or
 * more Sets as storage to help you solve this problem.
 * 
 * For example, if one list contains the values [3, 7, 3, -1, 2, 3, 7, 2, 15,
 * 15] and the other list contains the values [-5, 15, 2, -1, 7, 15, 36], your
 * method should return 4 (because the elements -1, 2, 7, and 15 occur in both
 * lists).
 */
import java.util.*;

public class CountCommon
{

	public static void main(String[] args)
	{
		List<Integer> list1 = new LinkedList<Integer>();
		List<Integer> list2 = new LinkedList<Integer>();
		list1.add(3);
		list1.add(7);
		list1.add(3);
		list1.add(-1);
		list1.add(2);
		list1.add(3);
		list1.add(7);
		list1.add(2);
		list1.add(15);
		list1.add(15);

		list2.add(-5);
		list2.add(15);
		list2.add(2);
		list2.add(-1);
		list2.add(7);
		list2.add(15);
		list2.add(36);
		System.out.println(countCommon(list1, list2));

	}

	public static int countCommon(List<Integer> list1, List<Integer> list2)
	{
		Set<Integer> nums = new HashSet<Integer>(list1);
		nums.retainAll(list2);
		System.out.println(nums);
		return nums.size();
	}

}
