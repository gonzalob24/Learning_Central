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
 * PURPOSE: Implement Heapsort and Quicksort. Run your programs on some sample data. Choose arrays with at least 30
 *          elements not all of them distinct.
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
 *
 *
 *
 */

package SortingAlgorithms;


public class QuickSort
{
    public QuickSort()
    {

    }

    public int[] quickSort(int[] array, int start, int end)
    {
        if (start < end)
        {
            int pivot = partition(array, start, end);
            quickSort(array, start, pivot - 1);
            quickSort(array, pivot + 1, end);
        }
        return array;
    }

    private int partition(int[] array, int p, int  q)
    {
        int pivot = q;
        int i = p - 1;
        for (int j = p; j <= q; j++ )
        {
            if (array[j] <= array[pivot])
            {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        return i;
    }
    public void printArray(int[] array)
    {
        System.out.print("[" + array[0]);
        for (int i = 1; i < array.length; i++)
        {
            System.out.print(", " + array[i]);
        }
        System.out.println("]\n\n");
    }
}