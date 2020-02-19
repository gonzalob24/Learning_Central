/*
 * Given the main() method below; please write the recursive method, in Java,
 * that produces the given Example Output for this problem. Note: This is a
 * factorial problem; positive integers only.
 * You have 15 minutes.
 */

package QuickCodeClass;

public class RecursionCode
{

	public static void main(String[] args)
	{
		int myInt = 6;
		int a = calcFact(myInt);
		System.out.printf("The factorial of %d is : %d\n", myInt, a);
	}

	public static int calcFact(int n)
	{
		int result;

		if (n == 1)
		{
			result = 1;
			System.out.printf("returns %d from calcFact(%d)\n", result, n);
			return result;
		} else
		{
			result = calcFact(n - 1) * n;
			System.out.printf("returns %d from calcFact(%d)\n", result, n);
			return result;
		}
	}

}
