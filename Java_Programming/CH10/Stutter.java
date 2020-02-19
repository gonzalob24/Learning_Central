
/*
 * Write a method stutter that takes an ArrayList of Strings and an integer k as
 * parameters and that replaces every string with k copies of that string. For
 * example, if the list stores the values ["how", "are", "you?"] before the
 * method is called and k is 4, it should store the values ["how", "how", "how",
 * "how", "are", "are", "are", "are", "you?", "you?", "you?", "you?"] after the
 * method finishes executing. If k is 0 or negative, the list should be empty
 * after the call.
 */

import java.util.*;

public class Stutter
{

	public static void main(String[] args)
	{
		ArrayList<String> test = new ArrayList<String>(Arrays.asList("how", "are", "you?"));

		System.out.println(test);
		stutter(test, 3);
		System.out.println(test);
	}

	// Method will duplicate each string in the ArrayList k number of times
	public static void stutter(ArrayList<String> list1, int k)
	{
		if (k <= 0)
		{
			list1.clear();
		} else
		{
			// int length_of_array = list1.size();
			for (int i = 0; i < list1.size(); i += k)
			{
				for (int j = 0; j < k - 1; j++)
				{
					list1.add(i, list1.get(i));
				}
			}
		}
	}
}
