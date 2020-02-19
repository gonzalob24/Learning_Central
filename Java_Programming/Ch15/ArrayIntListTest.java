public class ArrayIntListTest
{

	public static void main(String[] args)
	{
		ArrayIntList list1 = new ArrayIntList(2);
		ArrayIntList list2 = new ArrayIntList(50);

		list1.add(1);
		list1.add(2);
		list1.add(3);
		list1.add(4);
		list1.add(5);


		list2.add(7);
		list2.add(-8);

		System.out.println(list1);
		System.out.println(list2);
		//System.out.println("\nThe sum of the sublist in list1 is: " + list1.sublistSum(3, 3));

		System.out.println(list1.size());
		System.out.println(list2.size());
		//list1.collapse();
		System.out.println(list1);
	}

}
