
/*
 * Write the output that is printed when the given method below is passed each
 * of the following maps as its parameter. Assume that each parameter map stores
 * its key/value pairs in exactly the order shown, and that is the order in
 * which a for-each loop would examine them. Recall that maps print in a
 * {key1=value1, key2=value2, ..., keyN=valueN} format. Your answer should
 * display the right values in the right order.
 */
import java.util.*;

public class MapMystery2
{

	public static void main(String[] args)
	{
		Map<String, String> second = new TreeMap<String, String>();

		second.put("sheep", "wool");
		second.put("house", "brick");
		second.put("cast", "plaster");
		second.put("wool", "wool");
		System.out.println(second);
		mapMystery2(second);
	}

	public static void mapMystery2(Map<String, String> list)
	{
		Set<String> str = new TreeSet<String>();
		for ( String key : list.keySet() )
		{
			if (!list.get(key).equals(key))
			{
				str.add(list.get(key));
			} else
			{
				str.remove(list.get(key));
			}
		}
		System.out.println(str);
	}
}
