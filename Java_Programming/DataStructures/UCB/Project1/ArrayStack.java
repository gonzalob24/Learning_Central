package UCB.Project1;

import java.util.*;

public class ArrayStack<Any>
{
	private int topOfStack;
	private int size;
	private Any[] stack;

	private static final int STACK_SIZE = 5;

	public ArrayStack()
	{
		stack = (Any[]) new Object[STACK_SIZE];
		topOfStack = -1;  // initially topOfStack is -1
		size = 0;
	}

	/**
	 * method that will initialize stack with a certain size
	 */
	public ArrayStack(int maxSize)
	{
		stack = (Any[]) new Object[maxSize];
		topOfStack = -1;
		size = 0;
	}

	//method that will push an element to the top of the stak
	public void push(Any x)
	{
		topOfStack++;
		if (topOfStack == this.stack.length)
		{
			doubleArray();
		}
		this.stack[topOfStack] = x;
		size++;
	}

	//method that will remove an element from the stack
	public void pop()
	{
		if (isEmpty())
		{
			throw new IllegalStateException("Stack is Empty");
		}
		this.stack[topOfStack] = null;
		size--;
		topOfStack--;
	}

	/**
	 * display the top element of the stack
	 */
	public Any peek()
	{
		if (isEmpty())
		{
			System.out.println("Stack is empty");
			throw new EmptyStackException();
		}
		return stack[topOfStack];
	}

	//method that will double the size of the stack if it is full
	public void doubleArray()
	{
		Any[] temp = this.stack;
		this.stack = (Any[]) new Object[this.stack.length * 2];
		for (int i = 0; i < temp.length; i++)
		{
			this.stack[i] = temp[i];
		}
	}

	//method that checks if the stack is empty
	public boolean isEmpty()
	{
		return topOfStack == -1;
	}

	/**
	 * will return true of the stack is full
	 */
	public boolean isFull()
	{
		return size == stack.length - 1;
	}

	//display the ArrayStack
	public void display()
	{
		System.out.println(Arrays.toString(stack));
	}

	//size of the stack
	public int size()
	{
		return this.size; //ot return topOsStack + 1
	}
}
