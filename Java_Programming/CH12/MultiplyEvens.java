/*
 * Write a method multiplyEvens that returns the product of the first n even
 * integers. For example:
 * 
 * Call Output Reason
 * multiplyEvens(1); 2 2 = 2
 * multiplyEvens(2); 8 2 * 4 = 8
 * multiplyEvens(3); 48 2 * 4 * 6 = 48
 * multiplyEvens(4); 384 2 * 4 * 6 * 8 = 384
 * You should throw an IllegalArgumentException if passed a value less than or
 * equal to 0.
 */
public class MultiplyEvens
{

	public static void main(String[] args)
	{
		System.out.println(multiplyEvens(3));
		// multiplyEvens(3);

	}

	public static int multiplyEvens(int n)
	{
		if (n <= 0)
		{
			throw new IllegalArgumentException("Value can't be less than or equal to 0");
		} else if (n == 1)
		{
			return 2;
		} else
		{

			return multiplyEvens(n - 1) * n * 2;
			
		}

	}
}
