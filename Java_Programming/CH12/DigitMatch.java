/*
 * Write a recursive method digitMatch that accepts two non-negative integers as
 * parameters and that returns the number of digits that match between them. Two
 * digits match if they are equal and have the same position relative to the end
 * of the number (i.e. starting with the ones digit). In other words, the method
 * should compare the last digits of each number, the second-to-last digits of
 * each number, the third-to-last digits of each number, and so forth, counting
 * how many pairs match. For example, for the call of digitMatch(1072503891,
 * 62530841), the method would compare as follows:
 * 
 * 1 0 7 2 5 0 3 8 9 1
 * | | | | | | | |
 * 6 2 5 3 0 8 4 1
 * The method should return 4 in this case because 4 of these pairs match (2-2,
 * 5-5, 8-8, and 1-1). Below are more examples:
 * 
 * Call Value Returned
 * digitMatch(38, 34) 1
 * digitMatch(5, 5552) 0
 * digitMatch(892, 892) 3
 * digitMatch(298892, 7892) 3
 * digitMatch(380, 0) 1
 * digitMatch(123456, 654321) 0
 * digitMatch(1234567, 67) 2
 * Your method should throw an IllegalArgumentException if either of the two
 * parameters is negative. You are not allowed to construct any structured
 * objects other than Strings (no array, List, Scanner, etc.) and you may not
 * use any loops to solve this problem; you must use recursion.
 */
public class DigitMatch
{

	public static void main(String[] args)
	{
		// System.out.println(112 / 10);
		System.out.println(digitMatch(12, 11));

	}

	public static int digitMatch(int n1, int n2)
	{
		if (n1 < 0 || n2 < 0)
		{
			throw new IllegalArgumentException("Values can't be less than 0");
		} else if (n1 == 0 && n2 == 0)
		{
			return 1;
		} else
		{
			int results = 0;
			if (n1 % 10 == n2 % 10)
			{
				results += 1;
				digitMatch(n1 / 10, n2 / 10);

			}
			if (n1 / 10 == 0 || n2 / 10 == 0)
			{
				return results;
			}
			return results + digitMatch(n1 / 10, n2 / 10);
		}
	}
}
