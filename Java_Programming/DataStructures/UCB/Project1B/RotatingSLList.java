package UCB.Project1B;

import UCB.Project1.SLList;

public class RotatingSLList<Any> extends SLList<Any>
{
	/**
	 * Rotates the list to the right
	 */
	public void rotateRight()
	{
		Any x = removeLast();
		addFirst(x);
	}

	public static void main(String[] args)
	{
		RotatingSLList<Integer> list1 = new RotatingSLList<>();
		list1.addLast(10);
		list1.addLast(11);
		list1.addLast(12);
		list1.addLast(13);
		list1.print();
		list1.rotateRight();
		list1.print();
	}
}
