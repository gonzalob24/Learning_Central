package UCB.Project1B;

public interface ASLList<type>
{
	/**
	 * Inserts an element into the back of the lists
	 */
	public void addLast(type x);

	/**
	 * returns the last element in the list
	 */
	public type getLast();

	/**
	 * gets an type from the front of the list
	 */
	public type getFirst();

	/**
	 * Gets the ith type in the list (0 is the front).
	 */
	public type get(int i);

	/**
	 * Inserts an type into the given position
	 */
	public void insert(type x, int index);

	/**
	 * Returns the number of types in the list.
	 */
	public int size();

	/**
	 * Deletes type from back of the list and
	 * returns deleted type.
	 */
	public type removeLast();

	/**
	 * Deletes type from the front of the list and
	 * returns deleted type.
	 */
	public type removeFirst();

	/**
	 * checks if the SLList is empty
	 */
	public boolean isEmpty();

	/**
	 * inserts an element at the beginning of the list
	 */
	public void addFirst(type x);

	/**
	 * Displays the array by default unless it is overridden
	 */
	default public void print()
	{
		for (int i = 0; i < size(); i++)
		{
			System.out.print(get(i) + " ");
		}
		System.out.println();
	}
}
