
public class GCD
{

	public static void main(String[] args)
	{
		System.out.println(greatestCD(-132, 20));

	}

	public static int greatestCD(int x, int y)
	{
		if (x < 0 || y < 0)
		{
			// return the absolute value of recursion
			return greatestCD(Math.abs(x), Math.abs(y));
		} else if (y == 0)
		{
			return x;
		} else
		{
			return greatestCD(y, x % y);
		}
	}
}
