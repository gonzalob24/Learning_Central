/*
 * PROGRAMMER: Gonzalo Betancourt
 * 
 * COURSE: CSCI 2315-02 Data Structures
 * 
 * DATE: October 2, 2019
 * 
 * ASSIGNMENT: Homework #3
 * 
 * ENVIRONMENT: Mac OS, Windows or Linux
 * 
 * FILES INCLUDED: Program Solving document, screen shot of working code and
 * BinarySearch source file
 * 
 * PURPOSE: write the code for binary search and create 4 different test cases
 * 
 * PRECONDITIONS: store the integers in an integer array or ArrayList
 * 
 * OUTPUT: Output will be -1 if number we are looking for is not found
 * or the index where the number was found
 * 
 * POSTCONDITIONS: the program will return a result
 * 
 * ALGORITHM: Binary recursive search
 * find the middle point of the array
 * compare the middle point value with the value that we are searching
 * update the left and right boundaries
 * 
 * 
 * ERRORS: What happens in case of unexpected input (optional)
 * 
 * EXAMPLE: A sample execution in terms of input and corresponding output (if
 * appropriate)
 * 
 * 
 * HISTORY: Useful if a sequence of assignments is based on the same project
 * (optional)
 * 
 */

package SortingAlgorithms;

import java.util.*;

public class BinarySearch
{

	private static final int NOT_FOUND = -1;

	public static void main(String[] args)
	{
		Random r = new Random();
		int searchNum4 = r.nextInt(100000) + 1;
		int searchNum3 = r.nextInt(100) + 1;

		// Test Case 1
		ArrayList<Integer> list1 = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));
		Collections.sort(list1);

		// Test Case 2
		ArrayList<Integer> list2 = new ArrayList<Integer>(Arrays.asList(2, 5, 10, 19, 8, 7, 4, 3, 22, 14, 27));
		Collections.sort(list2);

		// Test Case 3 random numbers from 1 - 100
		// The number I will search for is also random
		ArrayList<Integer> list3 = new ArrayList<Integer>();
		for (int i = 0; i < 10; i++)
		{
			int n = r.nextInt(100) + 1;
			list3.add(n);
		}
		Collections.sort(list3);
		// Test Case 4 random numbers from 1 - 100,000
		// The number I will search for is also random
		ArrayList<Integer> list4 = new ArrayList<Integer>();
		for (int i = 0; i < 100000; i++)
		{
			int n = r.nextInt(100000) + 1;
			list4.add(n);
		}
		Collections.sort(list4);

		System.out.println("Program will run 4 times and search for a number in an ArrayList.");
		System.out.println("If the number is not found the program will return -1");
		System.out.printf("Test Case 1: \nsearch for 8: found in index: %d\n\n", binarySearch(list1, 8));
		System.out.printf("Test Case 2: \nsearch for 100: found in: %d\n\n", binarySearch(list2, 100));
		System.out.printf("Test Case 3: \nsearch for %d: found in: %d \n\n", searchNum3, binarySearch(list1, searchNum3));
		System.out.printf("Test Case 4: \nsearch for %d: found in : %d \n\n", searchNum4,
				binarySearch(list1, searchNum4));
	}

	// Method that perform s a binary search on a data type
	public static int binarySearch(ArrayList<Integer> a, int x)
	{
		return binarySearch(a, x, 0, a.size() - 1);
	}

	// private recursive method that performs a binary search
	private static int binarySearch(ArrayList<Integer> a, int x, int low, int high)
	{
		if (low > high)
		{
			return NOT_FOUND;
		}

		int mid = (low + high) / 2;

		if (a.get(mid).compareTo(x) < 0)
		{
			return binarySearch(a, x, mid + 1, high);
		} else if (a.get(mid).compareTo(x) > 0)
		{
			return binarySearch(a, x, low, mid - 1);
		} else
		{
			return mid;
		}
	}

}
