package UCB.Project1;

public class ArrayQueueTest
{
	public static void main(String[] args)
	{
		ArrayQueue<Integer> queue1 = new ArrayQueue<>();

		System.out.println("The ArrayQueue is empty: " + queue1.isEmpty());
		queue1.display(); //when there are no elements in the arrayqueue they will be filled with null because its an object
		queue1.enqueue(2);
		queue1.enqueue(4);
		queue1.enqueue(11);
		queue1.display();
		queue1.dequeue();
		queue1.display();
		queue1.enqueue(34);
		queue1.enqueue(22);
		queue1.display();
		queue1.dequeue();
		queue1.display();
		queue1.enqueue(76);
		queue1.display();
	}
}
