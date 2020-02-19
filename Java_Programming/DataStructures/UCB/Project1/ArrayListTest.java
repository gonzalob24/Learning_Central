package UCB.Project1;

public class ArrayListTest
{
	public static void main(String[] args)
	{
		ArrayList<Integer> list1 = new ArrayList<>();

		list1.addLast(1);
		list1.addLast(4);
		list1.addLast(1);
		list1.print();
		System.out.println("First item removed: " + list1.removeFirst());
		list1.print();
		list1.addLast(55);
		//list1.addLast(10);
		list1.print();
		list1.removeFirst();
		list1.print();

	}
}
