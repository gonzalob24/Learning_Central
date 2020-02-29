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
 *            HeapSort: sort and heapify
 *
 * OUTPUT: Sorted array
 *
 * POSTCONDITIONS: The program will return a sorted array
 *
 * ALGORITHMS:
 *           HeapSort:
 *             Build-heap(A)
 *              ​ for i = n to 1 do
 *                  swap(A[1],A[i])
 *                  ​n=n-1
 *              Heapify(A,1)
 *
 * Sample Output:
 *      This is random array set 1:
 *      Values of array before sort:
 *      [9, 0, 17, 29, 17, 6, 24, 18...
 *      Values of array after sort:
 *      [0, 0, 1, 4, 5, 6, 6, 7, 8...
 */

package SortingAlgorithms;

public class HeapSort
{
    private int[] array;

    public HeapSort()
    {
        //this.array = array;
    }

    public int[] sort(int[] array)
    {
        // Length of the array
        int n = array.length;

        // Building the heap
        for (int i = n / 2 - 1; i >= 0; i--)
        {
            heapify(array, n, i);
        }
        //
        for (int i = n -1; i >= 0; i--)
        {
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;

            heapify(array, i,0);
        }

        return array;
    }
    // Heapify
    public void heapify(int[] array, int n, int i)
    {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && array[left] > array[largest])
        {
            largest = left;
        }
        if (right < n && array[right] > array[largest])
        {
            largest = right;
        }

        if (largest != i)
        {
            int swap = array[i];
            array[i] = array[largest];
            array[largest] = swap;

            heapify(array, n, largest);
        }
    }
    //Print the array
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
