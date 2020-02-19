package UCB;

import org.junit.Test;

import java.util.*;

import static org.junit.Assert.*;

public class TestSort
{
	/**
	 * Test Sort.sort
	 */
	@Test
	public void testSort()
	{

		String[] input = {"i", "have", "an", "egg"};
		String[] expected = {"an", "egg", "have", "i"};

		Sort.sort(input);
		System.out.println(Arrays.toString(input));
		assertArrayEquals(expected, input);
	}

	@Test
	public void testFindSmallest()
	{
		String[] input = {"i", "have", "an", "egg"};
		int expected = 2;

		int actual = Sort.findSmallest(input, 0);

		assertEquals(expected, actual);
	}
}
