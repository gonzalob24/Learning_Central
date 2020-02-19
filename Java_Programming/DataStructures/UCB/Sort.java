package UCB;

import org.junit.Test;

public class Sort
{
	/**
	 * sorts strings destructively
	 */
	public static void sort(String[] x)
	{
		// Find the smallest item
		// move it to the front
		// selection sort the rest, use recursion

		sort(x, 0);

	}

	/**
	 * sort x starting at position x
	 */
	private static void sort(String[] x, int start)
	{
		if (start == x.length)
		{
			return;
		}
		int smallestIndex = findSmallest(x, start);
		swap(x, start, smallestIndex);
		sort(x, start + 1);
	}

	/**
	 * swap item a with b
	 */
	public static void swap(String[] x, int a, int b)
	{
		String temp = x[a];
		x[a] = x[b];
		x[b] = temp;
	}

	/**
	 * returns the index of the smallest string in x
	 */
	public static int findSmallest(String[] x, int start)
	{
		int smallestIndex = start;
		for (int i = start; i < x.length; i++)
		{
			int compare = x[i].compareTo(x[smallestIndex]);
			if (compare < 0)
			{
				smallestIndex = i;
			}
		}
		return smallestIndex;
	}
}
