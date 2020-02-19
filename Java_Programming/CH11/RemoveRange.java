import java.util.LinkedList;
import java.util.List;

/*
 * Write a method called removeInRange that accepts four parameters: a List of
 * integers, an element value, a starting index, and an ending index. The
 * method's behavior is to remove all occurrences of the given element that
 * appear in the list between the starting index (inclusive) and the ending
 * index (exclusive). Other values and occurrences of the given value that
 * appear outside the given index range are not affected.
 * 
 * For example, for the list (0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0,
 * 16), a call of removeInRange(list, 0, 5, 13) should produce the list (0, 0,
 * 2, 0, 4, 6, 8, 10, 12, 0, 14, 0, 16). Notice that the zeros located at
 * indices between 5 inclusive and 13 exclusive in the original list (before any
 * modifications were made) have been removed.
 */
public class RemoveRange
{

	public static void main(String[] args)
	{
		List<Integer> list1 = new LinkedList<Integer>();
		list1.add(0);
		list1.add(0);
		list1.add(2);
		list1.add(0);
		list1.add(4);
		list1.add(0);
		list1.add(6);
		list1.add(0);
		list1.add(8);
		list1.add(0);
		list1.add(10);
		list1.add(0);
		list1.add(12);
		list1.add(0);
		list1.add(14);
		list1.add(0);
		list1.add(16);
		System.out.println(list1);
		removeInRange(list1, 0, 5, 13);
		System.out.println(list1);

	}

	// Method that removes the even all occurrences of the given element between
	// start (inclusive) and ending (exclusive) index
	public static List<Integer> removeInRange(List<Integer> list1, int elmnt, int start_idx, int end_idx)
	{

		for ( int i = end_idx - 1; i >= start_idx; i-- )
		{
			if (list1.get(i) == elmnt)
			{
				list1.remove(i);
			}
		}
		return list1;
	}

}
