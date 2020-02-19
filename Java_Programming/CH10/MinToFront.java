
/*
 * Write a method minToFront that takes an ArrayList of integers as a parameter
 * and that moves the minimum value in the list to the front, otherwise
 * preserving the order of the elements. For example, if a variable called list
 * stores the following values: {3, 8, 92, 4, 2, 17, 9} and you make this call:
 * minToFront(list); it should store the following values after the call: {2, 3,
 * 8, 92, 4, 17, 9} You may assume that the list stores at least one value.
 */

import java.util.*;

public class MinToFront
{

    public static void main(String[] args)
    {
        ArrayList<Integer> numbs = new ArrayList<Integer>(Arrays.asList(3, 8, 92, 4, 2, 17, 9));

        System.out.println(numbs);
        minToFront(numbs);
        System.out.println(numbs);
    }

    // Method that moves the min integer of an ArrayList to the front
    public static void minToFront(ArrayList<Integer> numbers)
    {
        int min = 9999;
        int index = 0;
        int remove_index = 0;
        for (int num : numbers)
        {
            if (num < min)
            {
                min = num;
                remove_index = index;
            }
            index++;
        }
        numbers.remove(remove_index);
        numbers.add(0, min);
    }

}
