
/*
 * Write a method removeEvenLength that takes a Set of strings as a parameter
 * and that removes all of the strings of even length from the set. For example,
 * if your method is passed a set containing the following elements:
 * 
 * ["foo", "buzz", "bar", "fork", "bort", "spoon", "!", "dude"] Your method
 * should modify the set to store the following elements (the order of the
 * elements does not matter):
 * 
 * ["foo", "bar", "spoon", "!"]
 * 
 */
import java.util.*;

public class RemoveEvenLength1
{

	public static void main(String[] args)
	{
		Set<String> list12 = new HashSet<String>();
		list12.add("foo");
		list12.add("buzz");
		list12.add("bar");
		list12.add("fork");
		list12.add("bort");
		list12.add("spoon");
		list12.add("!");
		list12.add("dude");
		System.out.println(list12);
		removeEvenLength(list12);
	}

	public static void removeEvenLength(Set<String> list1)
	{
		Iterator<String> results = list1.iterator();
		Set<String> finalList = new HashSet<String>();
		while (results.hasNext())
		{
			String word = results.next();
			if (word.length() % 2 != 0)
			{
				finalList.add(word);
			}
		}
		System.out.println(finalList);
	}
}
