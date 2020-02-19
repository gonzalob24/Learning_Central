
/*
 * Write a method markLength4 that takes an ArrayList of Strings as a parameter
 * and that places a string of four asterisks "****" in front of every string of
 * length 4. For example, suppose that a variable called list contains the
 * following values: {"this", "is", "lots", "of", "fun", "for", "every", "Java",
 * "programmer"} And you make the following call: markLength4(list); then list
 * should store the following values after the call: {"****", "this", "is",
 * "****", "lots", "of", "fun", "for", "every", "****", "Java", "programmer"}
 * Notice that you leave the original strings in the list, "this", "lots",
 * "Java", but include the four-asterisk string in front of each to mark it.
 */

import java.util.*;

public class MarkLength4
{

	public static void main(String[] args)
	{
		ArrayList<String> test1 = new ArrayList<String>(
				Arrays.asList("this", "is", "lots", "of", "fun", "for", "every", "Java", "programmer"));

		System.out.println(test1);
		markLength4(test1);
		System.out.println(test1);

	}

	// Method that takes an ArrayList of Strings and places a string of four
	// asterisks **** in front of every string of length 4.

	public static void markLength4(ArrayList<String> list_four)
	{
		for ( int i = 0; i < list_four.size(); i++ )
		{
			if (list_four.get(i).length() == 4)
			{
				list_four.add(i, "****");
				i++;
			}
		}
	}

}
