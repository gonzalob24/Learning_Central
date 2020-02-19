/*
 * Write a method starString that accepts an integer parameter n and returns a
 * string of stars (asterisks) 2n long (i.e., 2 to the nth power).
 */

public class StarString
{

	public static void main(String[] args)
	{
		System.out.println(stars(4));
	}

	public static String stars(int n)
	{
		if (n < 0)
		{
			throw new IllegalArgumentException("Number can't be less than 0");
		}
		if (n == 0)
		{
			return "*";
		} else
		{

			return stars(n - 1) + stars(n - 1);
		}
	}
}
