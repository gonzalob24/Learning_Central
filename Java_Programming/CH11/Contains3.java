import java.util.*;

/*
 * Write a method contains3 that accepts a List of strings as a parameter and
 * returns true if any single string occurs at least 3 times in the list, and
 * false otherwise. Use a map as auxiliary storage.
 */
public class Contains3
{

	public static void main(String[] args)
	{
		List<String> list12 = new LinkedList<>();
		list12.add("foo");
		list12.add("foo");
		list12.add("bar");
		list12.add("fork");
		list12.add("bort");
		list12.add("spoon");
		list12.add("foo");
		list12.add("dude");
		System.out.println(list12);
		System.out.println(contains3(list12));

	}

	public static boolean contains3(List<String> list1)
	{
		Map<String, Integer> results = new HashMap<>();
		for ( String word : list1 )
		{
			if (results.containsKey(word))
			{
				results.put(word, results.get(word) + 1);
			} else
			{
				results.put(word, 1);
			}
		}
		return results.containsValue(3);
	}
}
