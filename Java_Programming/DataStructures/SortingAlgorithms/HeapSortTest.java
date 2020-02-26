package SortingAlgorithms;

import edu.princeton.cs.algs4.Heap;

import java.util.*;

public class HeapSortTest
{
    public static void main(String[] args)
    {
        Random r = new Random();
        //int arr[] = {12, 11, 13, 5, 6, 7};
        // int[] arr = rand_array(r);
//        System.out.println(Arrays.toString(arr));
//
//        HeapSort h1 = new HeapSort(arr);
//        h1.sort();
//        h1.printArray();

        // 5 random arrays are tested
        for (int i = 1; i <= 5; i++)
        {
            System.out.println("This is random array set " + i + ":");
            int[] arr = rand_array(r);
            System.out.println("Values of array before sort:");
            System.out.println(Arrays.toString(arr));
            HeapSort hp = new HeapSort();
            int[] sorted = hp.sort(arr);
            System.out.println("Values of array after sort:s");
            hp.printArray(sorted);
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
