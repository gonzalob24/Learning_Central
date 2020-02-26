package Project1;

import java.util.Arrays;

public class ArrayQueue<Any>
{
	private Any[] array;
	private int size;
	private int back;
	private int front;

	private static final int DEFAULT_SIZE = 5;  //default size of the array

	public ArrayQueue()
	{
		array = (Any[]) new Object[DEFAULT_SIZE];
		back = -1;
		front = 0;
		size = 0;
	}

	//method that will enqueue. Adding elements to a que is always from the back.
	// adding an element to ArrayQueue
	public void enqueue(Any x)
	{
		if (this.size == this.array.length)
			doubleArray();
		back = increment(back);
		array[back] = x;
		size++;
	}

	// return and remove an element from the arrayQueue using deque
	public Any dequeue()
	{
		if (isEmpty())
		{
			throw new IllegalStateException("ArrayQueue is empty");
		}
		size--;
		Any removedValue = this.array[front];
		this.array[front] = null;
		front = increment(front);
		return removedValue;
	}

	// method that will double the size of the ArrayQueue if more elements need to be enqueued.
	// use an array expansion multiply DEFAULT_SIZE * 2
	public void doubleArray()
	{
		Any[] tempArray = this.array;
		this.array = (Any[]) new Object[this.array.length * 2];

		//copy all of the elements to array
		for (int i = 0; i < tempArray.length; i++)
		{
			this.array[i] = tempArray[i];
			front = 0;
			back = size - 1;
		}


	}

	//method that will check if the ArrayQueu is empty
	public boolean isEmpty()
	{
		return size == 0;
	}

	//method that will display the elements of the queue
	public void display()
	{
		System.out.println(Arrays.toString(array));
	}

	//private method that will increment the rear of the ArrayQueue
	//the rear will reset to 0 of at any given time rear == array.length
	private int increment(int x)
	{
		if (++x == this.array.length)
		{
			x = 0;
		}
		return x;
	}
}
