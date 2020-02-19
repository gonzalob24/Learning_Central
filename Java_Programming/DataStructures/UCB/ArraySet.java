package UCB;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ArraySet<T> implements Iterable<T>
{
	private T[] items;  // array
	private int size; // the next item to be added will be at position size

	public ArraySet()
	{
		this.items = (T[]) new Object[100];
		this.size = 0;
	}

	/* Returns true if this map contains a mapping for the specified key.
	 */
	public boolean contains(T x)
	{
		for (int i = 0; i < size; i += 1)
		{
			if (items[i].equals(x))
			{
				return true;
			}
		}
		return false;
	}

	/* Associates the specified value with the specified key in this map. */
	public void add(T x)
	{
		if (x == null)
		{
			throw new IllegalArgumentException("Can't add null to an ArraySet");
		}
		if (contains(x))
		{
			return;
		}
		items[size] = x;
		size += 1;
	}

	/* Returns the number of key-value mappings in this map. */
	public int size()
	{
		return size;
	}

	public T getItem(int index)
	{
		return items[index];
	}

	/*
	@Override
	public String toString()
	{
		StringBuilder printSB = new StringBuilder("[");
		for (int i = 0; i < size; i++)
		{
			printSB.append(items[i].toString());
			printSB.append(", ");
		}
		printSB.append(items[size - 1]);
		printSB.append("]");
		return printSB.toString();
	}
	*/
	@Override
	public String toString()
	{
		List<String> listOfItems = new ArrayList<>();
		for (T item : this)
		{
			listOfItems.add(item.toString());
		}
		return "[" + String.join(",", listOfItems) + "]";
	}

	/**
	 * The Object allows fodr generic representation
	 * First I will need to cast other to an ArraySet
	 */

	public static <Glerp> ArraySet<Glerp> of(Glerp... stuff) // var arg og Glerps, variable number of arguments
	{
		//static methods can't access T so make the method generic
		ArraySet<Glerp> returnSet = new ArraySet<Glerp>();
		for (Glerp x : stuff)
		{
			returnSet.add(x);
		}
		return returnSet;
	}

	@Override
	public boolean equals(Object other)
	{
		if (this == other)
		{
			return true;
		}
		if (other == null)
		{
			return false;
		}
		if (other.getClass() != this.getClass())
		{
			return false;
		}
		ArraySet<T> o = (ArraySet<T>) other;
		if (o.size() != this.size())
		{
			return false;
		}
		for (int i = 0; i < size; i++)
		{
			if (!o.contains(items[i]))
			{
				return false;
			}
		}
		return true;
	}

	public Iterator<T> iterator()
	{
		return new ArraySetIterator();
	}

	private class ArraySetIterator<T> implements Iterator<T>
	{
		private int position;

		public ArraySetIterator()
		{
			position = 0;
		}

		@Override
		public boolean hasNext()
		{
			return position < size();
		}

		@Override
		public T next()
		{
			T returnItem = (T) getItem(position);
			position++;
			return returnItem;
		}
	}
}