// Class ArrayIntList can be used to store a list of integers.

public class ArrayIntList1
{
	private int[] elementData; // list of integers
	private int size;          // current number of elements in the list

	// constructs a list with a capacity of 100
	public ArrayIntList1()
	{
		elementData = new int[100];
		size = 0;
	}

	// returns a comma-separated, bracketed version of the list
	public String toString()
	{
		if (size == 0)
		{
			return "[]";
		} else
		{
			String result = "[" + elementData[0];
			for (int i = 1; i < size; i++)
			{
				result += ", " + elementData[i];
			}
			result += "]";
			return result;
		}
	}

	// appends the given value to the end of the list
	public void add(int value)
	{
		elementData[size] = value;
		size++;
	}
}
