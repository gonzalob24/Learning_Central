package SortingAlgorithms;

import java.util.*;

public class QuickSortTest
{
    public static void main(String[] args)
    {
        // int[] array = {10, 3, 2, 7, 7, 5, 8, 4, 1, 2, 9, 7, 8, 11};

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