/*
 * Two-Dimensional Array. Complete the given class by writing a method that:
 * 
 * a. takes in any two-dimensional array of integers,
 * b. returns the sum total of all integers in the array
 * c. prints the array values by row with a sub-total at the end of each row d.
 * 
 * code must generate this Example Output:
 * Values in array1 by row are:
 * 1 2 3 = 6
 * 6 5 = 11
 * 8 = 8
 * 
 * Array-Total = 25
 * 
 */

package QuickCodeClass;

import java.util.*;

public class TwoDArray
{

	public static void main(String[] args)
	{
		// Create and output a 2D Array
		int[][] array1 =
			{
					{ 1, 2, 3 },
					{ 6, 5 },
					{ 8 } };

		System.out.println("Values in the array by row: ");
		int arrayTotal = outputArray(array1);
		System.out.printf("Array-Total: %d", arrayTotal);
	}

	// Output the array method
	public static int outputArray(int[][] array)
	{
		int arrayTotal = 0;

		// loop through the array's row
		for (int row = 0; row < array.length; row++)
		{
			int rowTotal = 0;
			for (int columns = 0; columns < array[row].length; columns++)
			{
				System.out.printf("%d ", array[row][columns]);
				rowTotal += array[row][columns];
			}
			System.out.printf(" = %d ", rowTotal);
			arrayTotal += rowTotal;
			System.out.println();
		}
		return arrayTotal;
	}

}
