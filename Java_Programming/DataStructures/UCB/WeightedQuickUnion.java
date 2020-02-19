package UCB;

import java.util.*;

public class WeightedQuickUnion
{
	public static void main(String[] args)
	{
		int[][] arr = {{1, 2, 3}, {1, 2, 3}, {1, 2, 3}};
		int[][] results = new int[3][3];
		System.out.println(Arrays.deepToString(arr));
		for (int row = 0; row < arr.length; row++)
		{
			for (int col = 0; col < arr[row].length; col++)
			{
				results[row][col] = arr[col][row];
			}
		}
		System.out.println(Arrays.deepToString(results));
	}
}

