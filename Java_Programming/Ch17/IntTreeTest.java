public class IntTreeTest
{
    public static void main(String[] args)
    {
        IntTree tree1 = new IntTree(5);
        tree1.printPreorder();
        tree1.printInorder();
        tree1.printPostorder();
        tree1.printSideways();
        int sum = tree1.sumOfTree();
        System.out.println("Sum of nodes in tree is: " + sum);
        int levels = tree1.countLevels();
        System.out.println("Number of levels: " + levels);
        int leaves = tree1.countLeaves();
        System.out.println("Total leaf nodes: " + leaves);

        IntSearchTree t1 = new IntSearchTree();
        t1.add(20);
        t1.add(100);
        t1.add(3);
        t1.add(44);
        t1.add(25);
        t1.add(15);
        t1.add(6);
        t1.printInorder();
        t1.printSideways();

    }
}
