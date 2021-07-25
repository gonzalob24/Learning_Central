package UCB.Project1B;

import UCB.Project1.SLList;
//import edu.princeton.cs.algs4.In;

public class VengefulSLList<Any> extends SLList<Any>
{
	// you can also declare this in a constructor

	SLList<Any> deletedItems;   //going to keep track of the deleted items in the list

	public VengefulSLList()
	{
		// if we do not include the super() java will implicitly call super constructor
		super();  // call ths super classes constructor.
		deletedItems = new SLList<>();
	}

	public VengefulSLList(Any x)
	{   // if we do not explicitly call super(x) java will implicitly call the default constructor above
		// w/oyt anny parameters.
		super(x);  // call ths super classes constructor.
		deletedItems = new SLList<>();
	}

	/**
	 * prints deleted items
	 */
	public void printLostItems()
	{
		deletedItems.print();
	}

	@Override
	public Any removeLast()
	{
		Any x = super.removeLast();
		deletedItems.addLast(x);
		return x;
	}

	public static void main(String[] args)
	{
		VengefulSLList<Integer> vs1 = new VengefulSLList<>();
		vs1.addLast(0);
		vs1.addLast(1);
		vs1.addLast(5);
		vs1.addLast(10);
		vs1.addLast(13);
		vs1.print();
		vs1.removeLast();
		vs1.removeLast();
		System.out.println("The deleted items are: ");
		vs1.deletedItems.print();

	}
}
