package UCB.Project1;

public class ArrayDequeTest
{
	public static void main(String[] args)
	{
		ArrayDeque a1 = new ArrayDeque();
		a1.addFront(1);
		a1.addFront(3);
		a1.addFront(5);
		a1.addBack(6);
		a1.addBack(16);
		a1.addBack(56);
		a1.addBack(12);
		a1.addBack(7);
		a1.addBack(66);
		a1.addBack(133);
		a1.addFront(331);
		a1.display();
		System.out.println("\nThe current size of the ArrayDeque is: " + a1.size());
		System.out.println("The item at the front of the ArrayDeque is: " + a1.removeFront());
		System.out.println("The item at the front of the ArrayDeque is: " + a1.removeFront());
		System.out.println("The item at the front of the ArrayDeque is: " + a1.removeFront());
		System.out.println("The item at the front of the ArrayDeque is: " + a1.removeFront());
		a1.display();
		System.out.println("\nThe current size of the ArrayDeque is: " + a1.size());

	}
}
