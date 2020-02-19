/*
 * Write a recursive method indexOf that accepts two Strings as parameters and
 * that returns the starting index of the first occurrence of the second String
 * inside the first String (or -1 if not found). The table below lists several
 * calls to your method and their expected return values. Notice that case
 * matters, as in the last example that returns -1.
 * 
 * Call Value Returned
 * indexOf("Barack Obama", "Bar") 0
 * indexOf("Barack Obama", "ck") 4
 * indexOf("Barack Obama", "a") 1
 * indexOf("Barack Obama", "McCain") -1
 * indexOf("Barack Obama", "BAR") -1
 * Strings have an indexOf method, but you are not allowed to call it. You are
 * limited to these methods:
 * 
 * Method Description
 * equals(String other) returns true if the two Strings contain the same
 * characters
 * length() returns the int number of characters in the String
 * substring(int fromIndex, int toIndex)
 * substring(int fromIndex) returns a new String containing the characters from
 * this String from fromIndex (inclusive) to toIndex (exclusive), or to the end
 * of the String if toIndex is omitted
 * You are not allowed to construct any structured objects other than Strings
 * (no array, List, Scanner, etc.) and you may not use any loops to solve this
 * problem; you must use recursion.
 */
public class IndexOf
{

	public static void main(String[] args)
	{
		// System.out.println(indexOf("Barack Obama", "ck"));
		System.out.println(indexOf("abc", "d"));
		// System.out.println(indexOf("abc", "b"));

	}

	public static int indexOf(String s1, String s2)
	{
		if (s1.equals(s2))
		{
			return 0;
		} else if (s1.length() >= s2.length())
		{
			int length = s2.length();
			int index = 0;

			String s1_substring = s1.substring(0, length);

			if (s1_substring.equals(s2))
			{
				return index;
			} else
			{
				index += 1 + indexOf(s1.substring(1), s2);
				if (index != 0)
				{
					return index;
				}
			}
		}
		return -1;
	}
}
