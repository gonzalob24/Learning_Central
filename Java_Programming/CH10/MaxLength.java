import java.util.*;

// Write a method maxLength that takes an ArrayList of Strings as a parameter and that returns the 
// length of the longest string in the list. If your method is passed an empty list, it should return 0.

public class MaxLength
{
    public static void main(String[] args)
    {
        ArrayList<String> list1 = new ArrayList<>(
                Arrays.asList("all", "bus", "go", "on", "swish", "through", "wipers"));

        //System.out.println(list1);
        System.out.println(maxLength(list1));
    }

    //return the max length of the longest string in the array list
    public static String maxLength(ArrayList<String> list1)
    {
        int max_length = 0;
        String str = "";
        for (String s : list1)
        {
            if (s.length() > max_length)
            {
                max_length = s.length();
                str = s;
            }
        }
        return "The longhtes string is \"" + str + "\" its " + max_length + " characters long";
    }
}
