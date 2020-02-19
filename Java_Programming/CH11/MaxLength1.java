
/*
 * Write a method maxLength that takes a Set of strings as a parameter and that
 * returns the length of the longest string in the set. If your method is passed
 * an empty set, it should return 0.
 */

import java.util.*;

public class MaxLength1
{

	public static void main(String[] args)
	{
		Set<String> one = new HashSet<String>();
		one.add("RK");
		one.add("Bye");
		one.add("Longesttttt");
		System.out.println(maxLength(one));
	}

	public static int maxLength(Set<String> strng)
	{
		int large = 0;
		Iterator<String> list1 = strng.iterator();
		while (list1.hasNext())
		{
			String str = list1.next();

			if (str.length() > large)
			{
				large = str.length();
			}
		}
		return large;
	}
}
