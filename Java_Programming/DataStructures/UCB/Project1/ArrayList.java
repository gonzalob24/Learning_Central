package UCB.Project1;

import UCB.Project1B.ASLList;

/**
 * Invariants:
 * addLast: will be added to position zero
 * size: the number of items in our list is size.
 * getLast: the item we want to return is at position size - 1
 */

public class ArrayList<type> implements ASLList<type>
{
	private int size;
	private type[] items;
	private static int R_FACTOR = 2;

	public ArrayList()
	{
		//use this syntax because java does not allow us to create
		//arrays of generic objects.
		items = (type[]) new Object[5];
		size = 0;
	}

	/**
	 * Inserts X into the back of the list.
	 */
	@Override
	public void addLast(type x)
	{
		if (size == items.length)
		{
			resize();
		}
		items[size] = x;
		size++;
	}

	/**
	 * Inserts x type into the given int position
	 */
	public void insert(type x, int position)
	{
		type[] temp = (type[]) new Object[items.length + 1];
		System.arraycopy(items, 0, temp, 0, position);
		temp[position] = x;

		System.arraycopy(items, position, temp, position + 1, items.length - position);
		items = temp;
	}

	/**
	 * insert an element at the start of the list
	 */
	public void addFirst(type x)
	{
		insert(x, 0);
	}

	/**
	 * Returns the item from the back of the list.
	 */
	public type getLast()
	{
		return items[size - 1];
	}

	/**
	 * Gets the ith item in the list (0 is the front).
	 */
	public type get(int i)
	{
		return items[i];
	}

	/**
	 * gets an item from the front of the list
	 */
	public type getFirst()
	{
		return get(0);
	}

	/**
	 * Returns the number of items in the list.
	 */
	public int size()
	{
		return size;
	}

	/**
	 * Deletes item from back of the list and
	 * returns deleted item.
	 */

	/**
	 * checks if the SLList is empty
	 */
	public boolean isEmpty()
	{
		return size == 0;
	}

	public type removeLast()
	{
		type last_item = getLast();
		size--;
		items[size] = null;
		return last_item;
	}

	/**
	 * removes the first element from the array and returns the value
	 */
	public type removeFirst()
	{
		type first_item = getFirst();
		type[] temp = (type[]) new Object[items.length - 1];
		System.arraycopy(items, 1, temp, 0, items.length - 1);

		items = temp;
		size--;
		return first_item;
	}

	/**
	 * Doubles the array when size == array.length
	 */
	public void resize()
	{
		type[] temp = items;
		items = (type[]) new Object[size * R_FACTOR];  // doubles the size of the array
		System.arraycopy(temp, 0, items, 0, size);
	}

}


