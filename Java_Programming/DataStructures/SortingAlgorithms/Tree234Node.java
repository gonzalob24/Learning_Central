package SortingAlgorithms;

public class Tree234Node
{
	// m value of tree
	private static final int SIZE = 4;
	private int items;
	private Tree234Node parent;
	private Tree234Node child_array[] = new Tree234Node[SIZE];
	private TreeData items_array[] = new TreeData[SIZE - 1];


	// method to add child to this node
	public void addChild(int num_ch, Tree234Node ch)
	{
		child_array[num_ch] = ch;
		if (ch != null)
		{
			ch.parent = this;
		}
	}

	// method to remove and return a child from array
	public Tree234Node removeChild(int num_ch)
	{
		// create a temp node
		Tree234Node temp = child_array[num_ch];
		child_array[num_ch] = null;
		// return the temp node
		return temp;
	}

	// Getter method to return child
	public Tree234Node getChild(int num_ch)
	{
		// return child located at the specified location
		return child_array[num_ch];
	}

	// Method to check if the node is a leaf node or not
	// returns a boolean
	public boolean checkIfLeaf()
	{
		if (child_array[0] == null)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	// Method that will get an item at a specific index
	public TreeData getData(int idx)
	{
		// return the item at that index
		return items_array[idx];
	}

	// print the node
	public void printNode()
	{
		for (int i = 0; i < items; i++)
		{
			items_array[i].printData();
		}
	}

	// methoda that will return the number of items in array
	public int getTotalItems()
	{
		return items;
	}

	// method that will help insert an item to the tree
	public int addItem(TreeData n)
	{
		// cache the items in the tree so that it makes it easier
		// to retunr the total number of items in the tree
		items++;
		int key = n.data;

		for (int i = SIZE - 2; i >= 0; i--)
		{
			if (items_array[i] ==  null)
			{
				continue;
			}
			else
			{
				int array_key = items_array[i].data;
				// check of key < array_key
				if (key < array_key)
				{
					items_array[i+1] = items_array[i];
				}
				else
				{
					items_array[i+1] = n;
					return i+1;
				}
			}
		}
		items_array[0] = n;
		return 0;
	}

	// Method that will check if the full
	public boolean checkIfFull()
	{
		if (items == SIZE - 1)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	// method that will remove an item
	public TreeData removeData()
	{
		// create a temp item that I will return
		TreeData temp = items_array[items - 1];
		items_array[items - 1] = null;
		// decrease the total items in the array by 1
		items--;
		return temp;
	}

	// getter that will return the parent of the node
	public Tree234Node getParent()
	{
		return parent;
	}
}
