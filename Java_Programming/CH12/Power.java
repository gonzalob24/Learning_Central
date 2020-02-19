
public class Power
{

	public static void main(String[] args)
	{
		System.out.println(power(2, 16));
	}

	public static int power(int x, int y)
	{
		// Base case the power of 0 is 1 and checks if exponents is 0
		if (y < 0)
		{
			throw new IllegalArgumentException("negative exponent: " + y);
		} else if (y == 0)
		{
			return 1;
		} else if (y % 2 == 0)
		{
			return power(x * x, y / 2);
		} else
		{
			return x * power(x, y - 1);
		}
	}
}
