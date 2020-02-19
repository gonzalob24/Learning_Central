/*
 *Write a method maxOccurrences that accepts a List of integers as a parameter and returns the number
 *of times the most frequently occurring integer (the "mode") occurs in the list. Solve this problem
 *using a Map as auxiliary storage. If the list is empty, return 0.
 */

import java.util.*;
public class MaxOccurrences
{
    public static void main(String[] args)
    {
        ArrayList<Integer> list1 = new ArrayList<>(
                Arrays.asList(0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16));
        System.out.println(maxOccurrences(list1));
    }

    public static int maxOccurrences(List<Integer> list1)
    {
        Map<Integer, Integer> results = new HashMap<>();
        Iterator<Integer> nums = list1.iterator();

        while(nums.hasNext())
        {
            int num  = nums.next();
            if (results.containsKey(num))
            {
                results.put(num, results.get(num) + 1);
            } else
            {
                results.put(num, 1);
            }
        }
        Collection<Integer> value = results.values();
        int max = 0;
        for(int n : value)
        {
            if (n > max)
            {
                max = n;
            }
        }
        return max;
    }
}
