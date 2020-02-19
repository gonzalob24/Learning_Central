
/*
 * Write a method intersect that takes two Maps of strings to integers as
 * parameters and that returns a new map whose contents are the intersection of
 * the two. The intersection of two maps is defined here as the set of keys and
 * values that exist in both maps. So if some key K maps to value V in both the
 * first and second map, include it in your result. If K does not exist as a key
 * in both maps, or if K does not map to the same value V in both maps, exclude
 * that pair from your result. For example, consider the following two maps:
 * 
 * {Janet=87, Logan=62, Whitaker=46, Alyssa=100, Stefanie=80, Jeff=88, Kim=52,
 * Sylvia=95} {Logan=62, Kim=52, Whitaker=52, Jeff=88, Stefanie=80, Brian=60,
 * Lisa=83, Sylvia=87} Calling your method on the preceding maps would return
 * the following new map (the order of the key/value pairs does not matter):
 * 
 * {Logan=62, Stefanie=80, Jeff=88, Kim=52}
 */

import java.util.*;

public class Intersect
{

	public static void main(String[] args)
	{
		Map<String, Integer> map1 = new HashMap<String, Integer>();
		Map<String, Integer> map2 = new HashMap<String, Integer>();
		map1.put("Janet", 87);
		map1.put("Logan", 62);
		map1.put("Whitaker", 46);
		map1.put("Alyssa", 100);
		map1.put("Stephanie", 80);
		map1.put("Jeff", 88);
		map1.put("Kim", 52);
		map1.put("Sylvia", 95);
		map2.put("Logan", 62);
		map2.put("Kim", 52);
		map2.put("Whitaker", 52);
		map2.put("Jeff", 88);
		map2.put("Stephanie", 80);
		map2.put("Brian", 60);
		map2.put("Lisa", 83);
		map2.put("Sylvia", 87);
		System.out.println(intersect(map1, map2));

	}

	public static Map<String, Integer> intersect(Map<String, Integer> map1, Map<String, Integer> map2)
	{
		Collection<Integer> values = map1.values();
		Set<String> names1 = map1.keySet();
		Set<String> names2 = map2.keySet();

		Map<String, Integer> results = new HashMap<String, Integer>();

		for ( int i = 0; i < values.size(); i++ )
		{
			for ( String name1 : names1 )
			{
				for ( String name2 : names2 )
				{
					if ((map1.get(name1) == map2.get(name1)) && (name1 == name2))
					{
						results.put(name1, map1.get(name1));

					}
				}
			}
		}
		return results;
	}
}
