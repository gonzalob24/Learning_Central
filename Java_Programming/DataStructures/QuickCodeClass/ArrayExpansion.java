/*
 * Complete the Java application by writing the code segments that will complete
 * this array expansion. Problem Solving Process is not necessary. You have 15
 * minutes.
 *
 * a. Declare and Inititalize array (MyGradesArray) with the following Grades:
 * 87, 90, 78, 92, 96, 82. (Note: array size is six)
 * b. Make a copy of MyGradesArray (name: CopyMyGrades)
 * c. Make a new MyGradesArray that will hold ten grades
 * d. Copy grades from CopyMyGrades to the new MyGradesArray
 * e. Reclaim memory
 *
 * from CopyMyGrades
 * Output:
 * MyGradesArray
 * 87 90 78 92 96 82
 *
 * CopyMyGrades
 * 87 90 78 92 96 82
 *
 * New MyGradesArray
 * 0000000000 Completed Expansion of MyGradesArray
 * 87 90 78 92 96 82 0 0 0 0
 */

package QuickCodeClass;

import java.util.*;

public class ArrayExpansion
{

	public static void main(String[] args)
	{
		int[] myGradesArray = {87, 90, 78, 92, 96, 82};

		// int[] copyMyGrades = Arrays.copyOf(myGradesArray, myGradesArray.length);
		int[] copyMyGrades = myGradesArray;
		myGradesArray = new int[10];

		for (int i = 0; i < copyMyGrades.length; i++)
		{
			myGradesArray[i] = copyMyGrades[i];
		}

		System.out.println(Arrays.toString(myGradesArray));
		copyMyGrades = null;
		System.out.println(Arrays.toString(copyMyGrades));

	}

}
