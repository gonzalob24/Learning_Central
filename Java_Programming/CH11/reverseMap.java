import java.util.*;

public class reverseMap
{
	public static void main(String[] args)
	{
		Map<Integer, String> map1 = new HashMap<>();
		map1.put(42, "Marty");
		map1.put(81, "Sue");
		map1.put(17, "Ed");
		map1.put(31, "Dave");
		map1.put(56, "Ed");
		map1.put(3, "Marty");
		map1.put(29, "Ed");

		//System.out.println(map1);
		System.out.println(reverseMaps(map1));
	}
	public static Map<String, Integer> reverseMaps(Map<Integer, String> map1)
	{
		Collection<String> values = map1.values();
		Set<Integer> keys = map1.keySet();
		Iterator<Integer> itr = keys.iterator();
		//System.out.println(values);
		//Set<String> setvalues = new HashSet<>(map1.values());
		//System.out.println(setvalues);

		Map<String, Integer> results = new HashMap<>();

		while (itr.hasNext())
		{
			int key = itr.next();
			results.put(map1.get(key), key);
		}
		return results;
	}
}
