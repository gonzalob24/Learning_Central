/*
 * PROGRAMMER: Gonzalo Betancourt
 *
 * COURSE: CSCI 3352-02 Adv. Data Structures
 *
 * DATE: February 26, 2020
 *
 * ASSIGNMENT: Programing Assignment: Heapsort and Quicksort
 *
 * ENVIRONMENT: Mac OS, Windows or Linux
 *
 * FILES INCLUDED: java source file
 *
 * PURPOSE: Implement Heapsort and Quicksort. Run your programs on some sample data.
 *          Choose arrays with at least 30
 *          elements not all of them distinct.
 *
 *          I used a random generator to create 5 different arrays and sorted
 *          each of them.
 *
 * PRECONDITIONS:
 *            Store the integers in an integer array
 *            Quicksort:
 *              i = j - 1
 *              j = typically the first element
 *              p = pivot, typically the last element
 *
 * OUTPUT: Sorted array
 *
 * POSTCONDITIONS: The program will return a sorted array
 *
 * ALGORITHMS:
 *           Quicksrot:
 *              At each step:
 *                  if j <= p
 *                      i++
 *                      swap(i, j)
 *                  j++
 *
 * Sample Output:
 *      This is random array set 1:
 *      Values of array before sort:
 *      [9, 0, 17, 29, 17, 6, 24, 18...
 *      Values of array after sort:
 *      [0, 0, 1, 4, 5, 6, 6, 7, 8...
 */


package SortingAlgorithms;

import java.util.*;

public class QuickSortTest
{
    public static void main(String[] args)
    {

        Random r = new Random();

        for (int i = 1; i <= 5; i++)
        {
            System.out.println("This is random array set " + i + ":");
            int[] arr = rand_array(r);
            System.out.println("Values of array before sort:");
            System.out.println(Arrays.toString(arr));
            QuickSort qs = new QuickSort();
            int[] sorted = qs.quickSort(arr, 0, arr.length - 1);
            System.out.println("Values of array after sort:s");
            qs.printArray(sorted);
        }
    }

    // Generates a random array length 30
    public static int[] rand_array(Random r)
    {
        int[] array = new int[30];

        for (int i = 0; i < 30; i++)
        {
            int n = r.nextInt(31);
            array[i] = n;
        }

        return array;
    }
}