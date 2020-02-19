import java.util.*;

public class StackQueuePattern
{
	public static void main(String[] args)
	{
		Stack<Integer> s1 = new Stack<>();
		Stack<Integer> s2 = new Stack<>();

		s1.push(1);
		s1.push(2);
		s1.push(3);
		s1.push(4);
		s1.push(5);
		s1.push(7);
		s1.push(9);
		s1.push(11);

		s2.push(13);
		s2.push(4);
		s2.push(17);
		s2.push(8);
		s2.push(1);
		s2.push(91);
		s2.push(81);
		s2.push(71);

		System.out.println(parityPattern(s1, s2));

	}

	/**
	 * Compare two stacks for similarity in terms of even and odd
	 * pattern.
	 *
	 * @return
	 */
	public static boolean parityPattern(Stack<Integer> s1, Stack<Integer> s2)
	{
		if (s1.size() != s2.size())
		{
			return false;
		} else
		{
			Stack<Integer> temp = new Stack<>();

			boolean same = true;
			while (same && !s2.isEmpty())
			{
				int num1 = s1.pop(); // pops from stack and returns popped value
				int num2 = s2.pop();

				if (num1 % 2 != num2 % 2)
				{
					same = false;
				}
				temp.push(num1);
				temp.push(num2);
			}

			while (!temp.isEmpty())
			{
				s2.push(temp.pop());
				s1.push(temp.pop());
			}
			return same;
		}
	}
}
