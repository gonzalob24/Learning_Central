import java.io.*;
import java.util.*;

public class Vocab
{
    public static void main(String[] args)
            throws FileNotFoundException
    {
        Scanner in1 = new Scanner(new File("test1.txt"));
        Scanner in2 = new Scanner(new File("test2.txt"));

        ArrayList<String> list1 = getWords(in1);
        ArrayList<String> list2 = getWords(in2);
        ArrayList<String> common = getOverLap(list1, list2);

        System.out.println("list1 = " + list1);
        System.out.println("list2 = " + list2);
        System.out.println("Overlap = " + common);

    }

    // Static method that reads words and sorts only unique words no duplicates
    public static ArrayList<String> getWords(Scanner input)
    {
        // read all of the words and sort them
        ArrayList<String> words = new ArrayList<>();
        while (input.hasNext())
        {
            String next = input.next().toLowerCase();
            words.add(next);
        }
        Collections.sort(words);

        // Add unique words to new list and return the ArrayList
        ArrayList<String> result = new ArrayList<>();
        if (words.size() > 0)
        {
            result.add(words.get(0));
            for (int i = 1; i < words.size(); i++)
            {
                if (!words.get(i).equals(words.get(i - 1)))
                {
                    result.add(words.get(i));
                }
            }
        }
        return result;
    }

    //Method that gets the overlap from both lists
    public static ArrayList<String> getOverLap(ArrayList<String> list1, ArrayList<String> list2)
    {
        ArrayList<String> result = new ArrayList<>();
        int i1 = 0;
        int i2 = 0;
        while (i1 < list1.size() && i2 < list2.size())
        {
            int num = list1.get(i1).compareTo(list2.get(i2));
            if (num == 0)
            {
                result.add(list1.get(i1));
                i1++;
                i2++;
            } else if (num < 0)
            {
                i1++;
            } else
            {
                i2++;
            }
        }
        return result;
    }
}
