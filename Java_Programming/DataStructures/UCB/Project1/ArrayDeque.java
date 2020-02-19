package UCB.Project1;

public class ArrayDeque
{
	private int size;
	private int[] array;
	private int front;
	private int count_front;
	private int back;
	private int default_size = 8;
	private static final int R_FACTOR = 2;
	private static final double MIN_USAGE_RATIO = 0.25;

	/**
	 * created an empty array
	 */
	public ArrayDeque()
	{
		this.array = new int[default_size];
		this.back = 0;
		this.front = array.length - 1;
		this.count_front = 0;
		size = 0;
	}

	// add an item to the front of the Deque
	public void addFront(int x)
	{
		if (size == array.length)
		{
			resize();
		}
		array[front] = x;
		front--;
		count_front++;
		size++;
	}

	// method that adds an item at the end of the ArrayDeque
	public void addBack(int x)
	{
		if (size == array.length)
		{
			resize();
		}
		array[back] = x;
		back++;
		size++;
	}

	/**
	 * Returns the size of the array
	 */
	public int size()
	{
		return size;
	}

	public int getCount_front()
	{
		return count_front;
	}

	/**
	 * remove an item from the front of the list
	 */
	public int removeFront()
	{
		++front;
		if (front == array.length)
		{
			front = 0;
		}
		int front_element = array[front];
		//front ++  then front restarts to 0 up to back.
		size--;
		return front_element;
	}

	/**
	 * resize method that will expand the array size by a factor of 2
	 */
	public void resize()
	{
		int[] temp = this.array;
		int back_insert = 0;
		this.array = new int[size * R_FACTOR];
		for (int i = 0; i < count_front; i++)
		{
			array[i] = temp[++front];
		}
		for (int i = count_front; i < back + count_front; i++)
		{
			array[i] = temp[back_insert++];
		}
		front = array.length - 1;
		back = size;
		temp = null;
	}

	/**
	 * increases the index of the front element added to te deque
	 */
	// displays the contents of the ArrayDeque
	public void display()
	{
		for (int i = front + 1; i < array.length; i++)
		{
			System.out.print(array[i] + " ");
		}
		for (int i = 0; i < back; i++)
		{
			System.out.print(array[i] + " ");
		}
		//		System.out.println("\nHow they really are");
		//		for (int i = 0; i < array.length; i++)
		//		{
		//			System.out.print(array[i] + " ");
		//		}
	}
}
