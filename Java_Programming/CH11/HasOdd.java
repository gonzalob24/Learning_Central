/*
 * Write a method hasOdd that takes a Set of integers as a parameter and that
 * returns true if the set contains at least one odd integer, and false
 * otherwise. If passed the empty set, your method should return false.
 * 
 */

import java.util.*;

public class HasOdd
{

	public static void main(String[] args)
	{
		Set<Integer> set1 = new HashSet<Integer>();
		set1.add(2);
		set1.add(4);
		set1.add(6);
		set1.add(8);
		set1.add(7);
		set1.add(10);
		System.out.println(hasOdd(set1));

	}

	public static boolean hasOdd(Set<Integer> nums)
	{
		Iterator<Integer> results = nums.iterator();
		boolean flag = true;

		while (flag)
		{
			if (results.hasNext())
			{
				if (results.next() % 2 != 0)
				{
					flag = true;
					break;
				}
			} else
			{
				flag = false;
			}
		}
		return flag;
	}
}
