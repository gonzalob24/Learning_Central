
/*
 * Write a method removeShorterStrings that takes an ArrayList of Strings as a
 * parameter and that removes from each successive pair of values the shorter
 * string in the pair. For example, suppose that an ArrayList called list
 * contains the following values: {"four", "score", "and", "seven", "years",
 * "ago"} In the first pair, "four" and "score", the shorter string is "four".
 * In the second pair, "and" and "seven", the shorter string is "and". In the
 * third pair, "years" and "ago", the shorter string is "ago". Therefore, the
 * call: removeShorterStrings(list); should remove these shorter strings,
 * leaving the list as follows: "score", "seven", "years". If there is a tie
 * (both strings have the same length), your method should remove the first
 * string in the pair. If there is an odd number of strings in the list, the
 * final value should be kept in the list.
 */

import java.util.*;

public class ShorterStrings
{

	public static void main(String[] args)
	{
		ArrayList<String> test = new ArrayList<String>(Arrays.asList("Don't", "remove", "the", "last", "string (me)"));
		System.out.println(test);
		removeShorterStrings(test);
		System.out.println(test);
		System.out.println("string (me)".length());

	}

	// Method that removes from each successive pair of values the shorter
	// string in the pair
	public static void removeShorterStrings(ArrayList<String> list1)
	{
		for ( int i = 0; i < list1.size() - 1; i++ )
		{
			if (list1.get(i + 1).length() >= list1.get(i).length())
			{
				list1.remove(i);
			} else
			{
				list1.remove(i + 1);
			}
		}
	}
}
