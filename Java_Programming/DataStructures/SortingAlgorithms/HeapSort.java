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
        int n = array.length;

        //Building the heap
        for (int i = n / 2 - 1; i >= 0; i--)
        {
            heapify(array, n, i);
        }

        for (int i = n -1; i >= 0; i--)
        {
            int temp = array[0];
            array[0] = array[i];
            array[i] = temp;

            heapify(array, i,0);
        }

        return array;
    }

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
