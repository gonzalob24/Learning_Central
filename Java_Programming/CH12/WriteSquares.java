/*
 * Write a method writeSquares that accepts an integer parameter n and prints
 * the first n squares separated by commas, with the odd squares in descending
 * order followed by the even squares in ascending order. The following table
 * shows several calls to the method and their expected output:
 * 
 * Call Valued Returned
 * writeSquares(5); 25, 9, 1, 4, 16
 * writeSquares(1); 1
 * writeSquares(8); 49, 25, 9, 1, 4, 16, 36, 64
 * Your method should throw an IllegalArgumentException if passed a value less
 * than 1. Note that the output does not advance onto the next line.
 */

public class WriteSquares
{

	public static void main(String[] args)
	{
		writeSquares(4);

	}

	public static void writeSquares(int n)
	{
		if (n < 1)
		{
			throw new IllegalArgumentException("Value cant be less than 1");
		} else if (n == 1)
		{

			System.out.print(n);
		} else if (n % 2 != 0)
		{
			System.out.print(n * n + ", ");
			writeSquares(n - 2);
			System.out.print(", " + (n - 1) * (n - 1));
		} else
		{
			System.out.print((n - 1) * (n - 1));
			if (n != 2)
			{
				System.out.print(", ");
				writeSquares(n - 2);
			}
			System.out.print(", " + n * n);
		}
	}
}
