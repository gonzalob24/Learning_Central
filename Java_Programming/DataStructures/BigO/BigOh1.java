package BigO;

public class BigOh1
{

	public static void main(String[] args)
	{
		int[] array1 =
			{ 2, 4, 8, 16, 20, 32, 64, 100 };

		int y = 1, x, z;
		// int n = 0;
		int count = 0;

		for (int n: array1)
		{
			// System.out.print(n + " ");
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= n; j++)
				{
					x = 2 * y;
					z = x--;
					count++;
				}
			}
			System.out.printf("When n is %-3d the inner loop executes %-5d times.", n, count);
			System.out.println();
			count = 0;
		}

	}

}
