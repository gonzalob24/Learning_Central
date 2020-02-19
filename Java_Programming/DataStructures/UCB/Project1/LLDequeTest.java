package UCB.Project1;

public class LLDequeTest
{
	public static void main(String[] args)
	{
		LinkedListDeque d1 = new LinkedListDeque();
		d1.addLast(33);
		d1.addLast(11);
		d1.addFirst(4);
		d1.addFirst(34);
		d1.addFirst(12);
		d1.addLast(77);
		System.out.println("The current size is: " + d1.size());
		d1.display();
		System.out.println("First item is: " + d1.removeFirst());
		d1.display();
		System.out.println("First item is: " + d1.removeFirst());
		System.out.println("The last item is : " + d1.removeLast());
		d1.display();
		d1.addFirst(34);
		d1.addFirst(12);
		d1.addLast(77);
		d1.display();
		d1.insert(22, 3);
		d1.display();
		d1.insert(21, 1);
		d1.display();
		d1.insert(84, 8);
		d1.display();
		System.out.println("Item at position 0 is: " + d1.get(0));
		System.out.println("Item at position 1 is: " + d1.get(1));
		System.out.println("Item at position 2 is: " + d1.get(2));
		System.out.println("Item at position 3 is: " + d1.get(3));
		System.out.println("The current size is: " + d1.size());
		System.out.println("Item at position 2 w/recurssion is: " + d1.getValueWithRecursion(9));
	}

}
