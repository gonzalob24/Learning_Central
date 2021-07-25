package UCB;

//import edu.princeton.cs.algs4.In;

import java.util.Iterator;
import java.util.*;

public class ArraySetTest
{
	public static void main(String[] args)
	{
		ArraySet<Integer> as1 = new ArraySet<>();
		ArraySet<Integer> as2 = new ArraySet<>();
		Set<Integer> set1 = new HashSet<>();
		Set<Integer> setE1 = new HashSet<>();
		Set<Integer> setE2 = new HashSet<>();

		ArraySet<String> testSet = ArraySet.of("hi", "this is my ", "first .of");
		System.out.println(testSet);
		setE1.add(4);
		setE1.add(3);
		setE1.add(2);

		setE2.add(4);
		setE2.add(3);
		setE2.add(2);

		//setE1 = setE2;
		System.out.print("Are setE1==setE2 the same: ");
		System.out.println(setE1 == setE2);
		System.out.print("Using the str1.equals(str2): ");
		System.out.println(setE1.equals(setE2));


		System.out.println("Built in print method" + set1);
		Iterator<Integer> first = set1.iterator();
		while (first.hasNext())
		{
			int x = first.next();
			System.out.print(x + " ");
		}
		System.out.println();

		as1.add(1);
		as1.add(2);
		as1.add(3);
		as1.add(4);

		as2.add(1);
		as2.add(2);
		as2.add(3);
		as2.add(4);
		System.out.println("ArraySet equals");
		System.out.print("Are as1==as2 the same: ");
		System.out.println(as1 == as2);
		System.out.print("Using the str1.equals(str2): ");
		System.out.println(as1.equals(as2));
		System.out.println("Built in method" + as1);

		Iterator<Integer> seer = as1.iterator();
		while (seer.hasNext())
		{
			int i = seer.next();
			System.out.println(i);
		}
	}
}
