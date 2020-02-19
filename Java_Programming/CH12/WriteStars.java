
public class WriteStars
{

	public static void main(String[] args)
	{

	}

	public static void stars(int n)
	{
		if (n == 0)
		{
			System.out.println();
		} else
		{
			System.out.print("*");
			stars(n - 1);
		}
	}
}
