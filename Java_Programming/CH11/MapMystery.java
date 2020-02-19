
/*
 * Write the output that is printed when the given method below is passed each
 * of the following maps as its parameter. Assume that each parameter map stores
 * its key/value pairs in exactly the order shown, and that is the order in
 * which a for-each loop would examine them. Recall that maps print in a
 * {key1=value1, key2=value2, ..., keyN=valueN} format. Your answer should
 * display the right keys and values in the right order.
 */

import java.util.*;

public class MapMystery
{

	public static void main(String[] args)
	{
		Map<String, String> first = new TreeMap<>();
		first.put("siskel", "ebert");
		first.put("girl", "boy");
		first.put("heads", "tails");
		first.put("ready", "begin");
		first.put("first", "last");
		first.put("begin", "end");
		System.out.println(first);
		System.out.println(first.keySet());
		mapMystery1(first);
	}

	public static void mapMystery1(Map<String, String> map)
	{
		Map<String, String> result = new TreeMap<>();

		for ( String key : map.keySet() )
		{
			if (key.compareTo(map.get(key)) < 0)
			{
				result.put(key, map.get(key));
			} else
			{
				result.put(map.get(key), key);
			}
		}
		System.out.println(result);
	}
}
