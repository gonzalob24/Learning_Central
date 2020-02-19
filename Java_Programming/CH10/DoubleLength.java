
/*
 * Write a method doubleList that takes an ArrayList of Strings as a parameter
 * and that replaces every string with two of that string. For example, if the
 * list stores the values {"how", "are", "you?"} before the method is called, it
 * should store the values {"how", "how", "are", "are", "you?", "you?"} after
 * the method finishes executing.
 */
import java.util.*;

public class DoubleLength
{
	public static void main(String[] args)
	{
		ArrayList<String> list = new ArrayList<String>(Arrays.asList("how", "are", "you?"));

		System.out.println(list);
		doubleList(list);
		System.out.println(list);

	}

	// Method that will double each element in the list
	public static void doubleList(ArrayList<String> list)
	{
		int length = 2 * list.size() - 1;

		for ( int i = 0; i < length; i += 2 )
		{
			list.add(i, list.get(i));

		}
	}
}
