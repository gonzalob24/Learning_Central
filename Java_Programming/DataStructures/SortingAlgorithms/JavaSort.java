/*
 * PROGRAMMER: Gonzalo Betancourt
 *
 * COURSE: CSCI 2315-02 Data Structures
 *
 * DATE: October 2, 2019
 * ASSIGNMENT: Homework #4
 *
 * ENVIRONMENT: Mac OS, Windows or Linux
 *
 * FILES INCLUDED: JavaSort.java and JavaSortTest.java source file, Problem
 * solving document, Screen shot of working code
 *
 * PRECONDITIONS: include integers in Arrays
 *
 *
 * ALGORITHM:
 * BubbleSort, insertion Sort, Merge Sort, Quick Sort will be used to sort an
 * Array
 *
 *
 * EXAMPLE:
 * Array before sorting:
 * [61, 46, 80, 90, 95, 83, 71, 99, 96, 91, 99, 4, 7]
 *
 *
 *
 * Please enter a number to select the sorting algorithm:
 * 1. Bubble Sort
 * 2. Insertion Sort
 * 3. Shell Sort
 * 4. Merge Sort
 * 5. Quick Sort
 * Your choice: 3
 *
 *
 * Each completed pass of the array:
 * ShellSort:
 * a[61, 46, 80, 90, 95, 83, 71, 99, 96, 91, 99, 4, 7]
 * a[61, 46, 80, 90, 95, 83, 71, 99, 96, 91, 99, 4, 7]
 *
 */

package SortingAlgorithms;

import java.util.*;

public class JavaSort
{
	private int[] array = new int[13];

	// Bubble sort algorithm
	// The algorithm I worked out on my own.
	// I added a swaps variable to check of the algorithm is sorted on the first
	// pass
	public void bubbleSort(int[] a)
	{
		for (int x = a.length - 2; x >= 0; x--) // Traversing the array
		{
			int swaps = 0; // the swaps checks to see if the array is already sorted
			for (int j = 0; j < x; j++)
			{
				if (a[j] > a[j + 1])
				{
					int temp = a[j];
					a[j] = a[j + 1];
					a[j + 1] = temp;
					swaps++;
				}
			}
			print(a);
			if (swaps == 0) // if array is sorted there will be no more traversals
			{
				break;
			}
		}
	}

	// Code from Udemy class DS in java
	public void selectionSort(int[] a)
	{
		int min_index, temp, i, j;
		for (i = 0; i < a.length - 1; i++)
		{
			min_index = i;
			// j is one more than i since we want to compare the next value
			for (j = i + 1; j < a.length; j++)
			{
				if (a[j] < a[min_index])
				{
					min_index = j;
				}
			}
			if (i != min_index)
			{
				temp = a[i];
				a[i] = a[min_index];
				a[min_index] = temp;
			}
			print(a);
		}
	}

	// Program that does the insertion sort algorithm
	// I read about this algorithm on Udemy
	public void insertionSort(int[] a)
	{
		int j;
		for (int x = 1; x < a.length; x++)
		{
			int temp = a[x]; // temporary variable that will hold the xth element
			j = x - 1;  // initially j = 0
			while (j >= 0 && a[j] > temp)
			{
				a[j + 1] = a[j];
				j--;  // decrement j
			}
			a[j + 1] = temp; // placing the temp value into the index a after j.
			print(a);
		}
	}

	// Program that will run the shell sort
	// I read about this algorithm on Udemy
	public void shellSort(int[] a)
	{
		int h = 3;
		int j = 0;
		while (h >= 1)
		{
			int temp;
			for (int x = h; x < a.length; x++)
			{
				temp = a[x];
				j = x - h;
				while (j >= 0 && a[j] > temp)
				{
					a[j + h] = a[j];
					j -= h;
				}
				a[j + h] = temp;
				print(a);
			}
			h -= 2;
		}
	}

	// New version of the mergeSort using recursion
	// Big O (NlogN)
	public static void mergeSort(int[] a)
	{
		// base case is if array length is 0 or 1
		if (a.length > 1)
		{
			// Split array into two halves left and right
			int[] left = Arrays.copyOfRange(a, 0, a.length / 2);
			int[] right = Arrays.copyOfRange(a, a.length / 2, a.length);

			// Using recursion sort the left and right side
			mergeSort(left);
			mergeSort(right);

			// Now after mergeSort merge the two arrays with the merge method
			merge(a, left, right);
		}
	}

	// Program that will use the merge sort to sort the array
	// I read about this algorithm on Udemy
	/*
	 * public void mergeSort(int[] a, int low, int high)
	 * {
	 * int range = high - low;
	 * if (range <= 1)
	 * {
	 * return;
	 * }
	 * int mid = (low + range / 2);
	 * // recursive sort
	 * mergeSort(a, low, mid);
	 * mergeSort(a, mid, high);
	 *
	 * // merge two sorted arrays
	 * int[] temp = new int[range];
	 * int i = low;
	 * int j = mid;
	 *
	 * for (int k = 0; k < range; k++)
	 * {
	 * if (i == mid)
	 * {
	 * temp[k] = a[j++];
	 * } else if (j == high)
	 * {
	 * temp[k] = a[i++];
	 * } else if (a[j] < a[i])
	 * {
	 * temp[k] = a[j++];
	 * } else
	 * {
	 * temp[k] = a[i++];
	 * }
	 * }
	 * for (int k = 0; k < range; k++)
	 * {
	 * a[low + k] = temp[k];
	 * }
	 * print(a);
	 * }
	 */
	// Merging two arrays that will help with the merge sort.
	public static void merge(int[] a, int[] left, int[] right)
	{
		int index_1 = 0;
		int index_2 = 0;

		for (int i = 0; i < a.length; i++)
		{
			if (index_2 >= a.length || index_1 < a.length && left[index_1] <= right[index_2])
			{
				a[i] = left[index_1];
				index_1++;
			} else
			{
				a[i] = right[index_2];
				index_2++;
			}
		}
	}

	// Program that will implement the quick sort algorithm
	// I read about this algorithm on Udemy
	public void quickSort(int[] a, int low, int high)
	{
		int i = low;
		int j = high;
		int temp;
		int pivot = a[(low + high) / 2];

		// I will partition the array
		while (i <= j)
		{
			while (a[i] < pivot)
			{
				i++;
			}
			while (a[j] > pivot)
			{
				j--;
			}
			if (i <= j)
			{
				// Perform some swaps
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
				i++;
				j--;
			}
		}
		// sorting the lower half recursively
		if (low < j)
		{
			quickSort(a, low, j);
		}
		if (i < high)
		{
			quickSort(a, i, high);
		}
		print(a);
	}

	// printing the array
	public void print(int[] a)
	{
		System.out.print("a[" + a[0]);
		for (int z = 1; z < a.length; z++)
		{
			System.out.print(", " + a[z]);
		}
		System.out.println("]");
	}
}
