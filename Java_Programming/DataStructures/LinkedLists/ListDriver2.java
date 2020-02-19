package LinkedLists;

public class ListDriver2
{

	public static void main(String[] args)
	{
		LinkedList2<Integer> I = new LinkedList2<Integer>();
		// LinkedList<Integer> I2 = new LinkedList<Integer>();
		System.out.println(I.getCurrent());
		//		for (int i = 0; i < 4; i++)
		//		{
		//			I.listInsert((i + 3));
		//		}
		//
		//		System.out.println("After the first loop (3,4,5,6)");
		//		System.out.println("_________________________");
		//		// System.out.println(I.getFirst());
		//		I.reset();
		//
		//		while (!I.isAtEnd())
		//		{
		//			Node2<Integer> temp = I.getCurrent();
		//			Integer n = temp.getValue();
		//
		//			System.out.println(n);
		//			I.advance();
		//		}
		//
		//		I.listHeadInsert(500);
		//		System.out.println("After the head insert(500,3,4,5,6)");
		//		System.out.println("_________________________");
		//		I.reset();
		//
		//		while (!I.isAtEnd())
		//		{
		//			Node2<Integer> temp = I.getCurrent();
		//			Integer n = temp.getValue();
		//
		//			System.out.println(n);
		//			I.advance();
		//		}
		//
		//		I.listRemove(5);
		//		System.out.println("After the remove (500,3,4,6)");
		//		System.out.println("_________________________");
		//		I.reset();
		//
		//		while (!I.isAtEnd())
		//		{
		//			Node2<Integer> temp = I.getCurrent();
		//			Integer n = temp.getValue();
		//
		//			System.out.println(n);
		//			I.advance();
		//		}
		//
		//		for (int i = 1; i < 4; i++)
		//		{
		//			I.listInsert(i * 100);
		//		}
		//
		//		System.out.println("After the inserting (100, 200, 300)");
		//		System.out.println("_________________________");
		//		I.reset();
		//
		//		while (!I.isAtEnd())
		//		{
		//			Node2<Integer> temp = I.getCurrent();
		//			Integer n = temp.getValue();
		//
		//			System.out.println(n);
		//			I.advance();
		//		}
		//		I.reset();
		//
		//		if (I.listSearch(200) != null)
		//		{
		//			System.out.println("Searched and found the 200");
		//			System.out.println("_________________________\n");
		//		}
		//
		//		I.listInsert(150);
		//		System.out.println("After the inserting 150 before 200");
		//		System.out.println("_________________________");
		//		I.reset();
		//
		//		while (!I.isAtEnd())
		//		{
		//			Node2<Integer> temp = I.getCurrent();
		//			Integer n = temp.getValue();
		//
		//			System.out.println(n);
		//			I.advance();
		//		}
		//		/*
		//		 * I2.listInsert(500);
		//		 * I2.listInsert(7);
		//		 * I2.listInsert(9);
		//		 * I2.listInsert(200);
		//		 * I2.listInsert(301);
		//		 * I.addList(I2); add in order non repeating numbers
		//		 *
		//		 * System.out.println("After the inserting list 2 (500, 7, 9, 200, 301");
		//		 * System.out.println("_________________________");
		//		 * I.reset();
		//		 *
		//		 * while(!I.isAtEnd())
		//		 * {
		//		 * Node<Integer> temp = I.getCurrent();
		//		 * Integer n = temp.getValue();
		//		 *
		//		 * System.out.println(n);
		//		 * I.advance();
		//		 * }
		//		 *
		//		 * I2.listRemove(9);
		//		 * I2.listRemove(200);
		//		 *
		//		 * I.subtractList(I2); remove elements that are the same
		//		 *
		//		 * System.out.println("After removing list 2 (500, 7, 301");
		//		 * System.out.println("_________________________");
		//		 * I.reset();
		//		 *
		//		 * while(!I.isAtEnd())
		//		 * {
		//		 * Node<Integer> temp = I.getCurrent();
		//		 * Integer n = temp.getValue();
		//		 *
		//		 * System.out.println(n);
		//		 * I.advance();
		//		 * }
		//		 */
		//
		//		I.reverseList();
		//		System.out.println("After reversing the list");
		//		System.out.println("_________________________");
		//		I.reset();

	}

}
