
/*
 * Write a method isUnique that accepts a Map from strings to strings as a
 * parameter and returns true if no two keys map to the same value (and false if
 * any two or more keys do map to the same value). For example, calling your
 * method on the following map would return true:
 * 
 * {Marty=Stepp, Stuart=Reges, Jessica=Miller, Amanda=Camp, Hal=Perkins} Calling
 * it on the following map would return false, because of two mappings for
 * Perkins and Reges:
 * 
 * {Kendrick=Perkins, Stuart=Reges, Jessica=Miller, Bruce=Reges, Hal=Perkins}
 * The empty map is considered to be unique, so your method should return true
 * if passed an empty map.
 */

import java.util.*;

public class IsUnique
{

	public static void main(String[] args)
	{
		Map<String, String> map1 = new HashMap<>();
		map1.put("Mart", "Stepp");
		map1.put("Kendrick", "Perkins");
		map1.put("Stuart", "map1.put(\"Mart\", \"Stepp\");Reges");
		map1.put("Jessica", "Miller");
		map1.put("Bruce", "Stepp");
		System.out.println(map1);
		System.out.println(isUnique(map1));

	}

	public static boolean isUnique(Map<String, String> map1)
	{
		Collection<String> value = map1.values();
		Map<String, Integer> results = new HashMap<>();

		for ( String word : value )
		{
			if (results.containsKey(word))
			{
				results.put(word, results.get(word) + 1);
			} else
			{
				results.put(word, 1);
			}
		}
		System.out.println(results);
		boolean flag = true;
		if (!value.isEmpty())
		{
			return !results.containsValue(2);
		} else
		{
			return flag;
		}

	}
}
