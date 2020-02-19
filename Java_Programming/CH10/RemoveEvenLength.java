
/*
 * Write a method removeEvenLength that takes an ArrayList of Strings as a
 * parameter and that removes all of the strings of even length from the list.
 */

import java.util.*;

public class RemoveEvenLength
{

    public static void main(String[] args)
    {
        ArrayList<String> list = new ArrayList<String>(Arrays.asList("This", "is", "a", "test"));

        System.out.println(list);
        removeEvenLength(list);
        System.out.print(list);

    }

    // Method that removes string of even length from the ArrayList of String
    public static void removeEvenLength(ArrayList<String> lst1)
    {
        ArrayList<String> temp = new ArrayList<String>();

        for (String word : lst1)
        {
            if (word.length() % 2 != 0)
            {
                temp.add(word);
            }
        }
        System.out.println(temp);
    }
}
