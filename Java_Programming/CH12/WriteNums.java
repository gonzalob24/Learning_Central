/*
 * Write a method writeNums that accepts an integer parameter n and prints the
 * first n integers starting with 1 in sequential order, separated by commas.
 * For example, the following calls produce the following output: writeNums(5);
 * 1, 2, 3, 4, 5 writeNums(12); 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
 */

public class WriteNums
{

	public static void main(String[] args)
	{
		writeNums(12);

	}

	public static void writeNums(int n)
	{
		if (n < 1)
		{
			throw new IllegalArgumentException("Number can't be less than 1");
		}
		if (n == 1)
		{
			System.out.print(n);
		} else
		{
			System.out.print(n + ", ");
			writeNums(n - 1);
			//System.out.print(", " + n);
		}
	}
}
