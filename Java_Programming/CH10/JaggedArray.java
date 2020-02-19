
public class JaggedArray
{

	public static void main(String[] args)
	{
		int[][] jagged = new int[5][];

		// Creating the size of each part of the array
		for ( int i = 0; i < jagged.length; i++ )
		{
			jagged[i] = new int[i + 1];
		}

		int count = 1;
		for ( int i = 0; i < jagged.length; i++ )
		{
			for ( int c = 0; c < jagged[i].length; c++ )
			{
				jagged[i][c] = count++;
			}
		}

		System.out.print("jagged = [[" + jagged[0][0] + "], ");
		for ( int i = 1; i < jagged.length - 1; i++ )
		{
			System.out.print("[");
			for ( int c = 0; c < jagged[i].length - 1; c++ )
			{
				System.out.print(jagged[i][c] + ", ");
			}
			System.out.print(jagged[i][i] + "], ");
		}
		System.out.print("[");
		for ( int i = 4; i < jagged.length; i++ )
		{
			for ( int c = 0; c < jagged[i].length - 1; c++ )
			{
				System.out.print(jagged[i][c] + ", ");
			}
			System.out.print(jagged[i][i] + "]");
		}
		System.out.println("]");
	}

}
