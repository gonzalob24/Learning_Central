import java.util.*;

public class ArrayListExample
{

	public static void main(String[] args)
	{
		ArrayList<String> first = new ArrayList<String>();

		first.add("one");
		first.add("two");
		first.add("third");
		first.add("Fives");
		first.add("Joess");

		System.out.println(first + " is size " + first.size());

		// first.clear();
		// System.out.println(first + " The sie is " + first.size());
		// first.add(3, "Hi"); can't add because the ArrayList currently has
		// size 0
		System.out.println("The number of plural words is " + countPlural(first));

	}

	// ArrayList passed as a parameter
	public static int countPlural(ArrayList<String> list1)
	{
		int count = 0;
		for ( int i = 0; i < list1.size(); i++ )
		{
			if (list1.get(i).endsWith("s"))
			{
				count++;
			}
		}
		return count;
	}

}
