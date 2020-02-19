/*
 * Write a method sumTo that accepts an integer parameter n and returns the sum
 * of the first n reciprocals. In other words:
 * 
 * sumTo(n) returns: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
 * 
 * For example, the call of sumTo(2) should return 1.5. The method should return
 * 0.0 if passed the value 0 and should throw an IllegalArgumentException if
 * passed a value less than 0.
 */

public class SumTo
{
	public static void main(String[] args)
	{
		System.out.println(sumTo(4));
	}

	public static double sumTo(int n)
	{
		if (n < 0)
		{
			throw new IllegalArgumentException("The value cant be less than 0");
		} else if (n == 0)
		{
			return 0.0;
		} else
		{
			return (double) 1 / n + sumTo(n - 1);
		}
	}
}
