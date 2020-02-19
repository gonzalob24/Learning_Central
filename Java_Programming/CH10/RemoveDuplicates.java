
/*
 * Write a method removeDuplicates that takes as a parameter a sorted ArrayList
 * of Strings and that eliminates any duplicates from the list. For example,
 * suppose that a variable called list contains the following values: {"be",
 * "be", "is", "not", "or", "question", "that", "the", "to", "to"} After calling
 * removeDuplicates(list); the list should store the following values: {"be",
 * "is", "not", "or", "question", "that", "the", "to"}
 */

import java.util.*;

public class RemoveDuplicates
{

    public static void main(String[] args)
    {
        // Array is already sorted for this example
        ArrayList<String> list1 = new ArrayList<>(
                Arrays.asList("be", "be", "is", "not", "or", "question", "that", "the", "to", "to"));

        System.out.println(list1);
        //removeDuplicates(list1);
        removeDuplicates2(list1);
    }

    // Method that will remove duplicate strings from a sorted array
    public static void removeDuplicates(ArrayList<String> list2)
    {
        ArrayList<String> result = new ArrayList<>();
        String temp = "";

        for (String word : list2)
        {
            if (!(word.equalsIgnoreCase(temp)))
            {
                temp = word;
                result.add(temp);
            }
        }
        System.out.println(result);
    }

    public static void removeDuplicates2(ArrayList<String> list1)
    {
        ArrayList<String> result = new ArrayList<>();

        for (int i = 0; i < list1.size() - 1; i += 2)
        {
            if (!(list1.get(i).equalsIgnoreCase(list1.get(i + 1))))
            {
                result.add(list1.get(i));
                result.add(list1.get(i + 1));

            } else
            {
                result.add(list1.get(i));

            }
        }
        System.out.println(result);
    }
}
