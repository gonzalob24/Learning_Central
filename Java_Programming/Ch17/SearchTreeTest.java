import java.util.Queue;

public class SearchTreeTest
{
	public static void main(String[] args)
	{
		SearchTree<Integer> intTree = new SearchTree<Integer>();
		intTree.add(15);
		intTree.add(1);
		intTree.add(10);
		intTree.add(3);
		intTree.add(17);
		intTree.add(20);
		intTree.add(11);
		intTree.add(4);
		intTree.add(7);
		intTree.add(18);
		intTree.add(27);
		intTree.printInorder();
		intTree.printPreorder();
		intTree.printPostorder();
		intTree.printSideways();
	}
}
