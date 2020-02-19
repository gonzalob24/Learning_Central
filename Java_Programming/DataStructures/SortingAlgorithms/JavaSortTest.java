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

public class JavaSortTest
{

	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int[] array = new int[13];

		// Random number generation
		Random r = new Random();

		// add elements to array
		for (int i = 0; i < array.length; i++)
		{
			array[i] = r.nextInt(99) + 1;
		}
		System.out.println("Array before sorting:");
		System.out.println(Arrays.toString(array));
		System.out.println("\n\n");
		choice(input, array);
		System.out.println("\n\n");
		System.out.println("Final sort using toStrings from Array class to compare.");
		System.out.println(Arrays.toString(array));
	}

	public static void choice(Scanner input, int[] a)
	{
		JavaSort list1 = new JavaSort();

		System.out.println("Please enter a number to select the sorting algorithm: ");
		System.out.println("1. Bubble Sort");
		System.out.println("2. Insertion Sort");
		System.out.println("3. Shell Sort");
		System.out.println("4. Merge Sort");
		System.out.println("5. Quick Sort");
		System.out.println("6. Selection Sort");

		System.out.print("Your choice: ");
		int choice = input.nextInt();
		System.out.println("\n\nEach completed pass of the array:");
		if (choice == 1)
		{
			System.out.println("BubbleSort:");
			list1.bubbleSort(a);
		} else if (choice == 2)
		{
			System.out.println("InsertionSort:");
			list1.insertionSort(a);
		} else if (choice == 3)
		{
			System.out.println("ShellSort:");
			list1.shellSort(a);
		} else if (choice == 4)
		{
			System.out.println("MergeSort:");
			list1.mergeSort(a);
		} else if (choice == 6)
		{
			System.out.println("SelectionSort:");
			list1.selectionSort(a);
		} else
		{
			System.out.println("QuickSort:");
			list1.quickSort(a, 0, 12);
		}
	}
}
