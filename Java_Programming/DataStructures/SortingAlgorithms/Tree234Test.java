package SortingAlgorithms;

/*
 * PROGRAMMER: Gonzalo Betancourt
 *
 * COURSE: CSCI 3352-02 Adv. Data Structures
 *
 * DATE: April 15, 2020
 *
 * ASSIGNMENT: Programing Assignment: 2-3-4 Tree 
 *
 * ENVIRONMENT: Mac OS, Windows or Linux
 *
 * FILES INCLUDED: TreeData, Tree234Node, Tree234 class file and Tree234Test Driver file
 *
 * PURPOSE: Implement 2-3-4 tree and a sort method. 
 *          Ran my program on some sample data, random generated.
 *          Choose arrays with at least 20 elemsts 
 *          
 *          I used a random generator to create the array then sorted it with program
 *
 * PRECONDITIONS:
 *            Store the integers in an integer array
 *            All positive integers
 *
 * OUTPUT: Array of how numbers are stored in tree and 
 *         In order traversal to show Sorted array
 *
 * POSTCONDITIONS: The program will return a sorted array
 *
 * ALGORITHMS:
 *            2-3-4 tree
              Allow 1, 2, or 3 keys per node.
              2-node: one key, two children.    
              3-node: two keys, three children.
              4-node: three keys, four children.
              
              Sort(array)
			Check if node is a leaf:
				Get all data from leaf
				Rearrange items in array
				Increment count
			If not leaf:
				Get total items + 1
				Call recursive sort1(get child of node, array, count)
				If current count is less than items in current node
					Add data to array
					Increment count       
              
 * Sample Output:
    Calling the sort method to sort the array:
    25 50 13 0 0 5 15 16 34 39 27 31 35 40 50 73 53 62 77 78
   
    Shows the Inorder Traversal of the tree
    0 0 5 13 15 16 25 27 31 34 35 39 40 50 50 53 62 73 77 78 

 */
import  java.util.Random;


public class Tree234Test
{
	public static void main(String[] args)
	{
		// I will generate random numbers to put inside tree
		Random r = new Random();

		// Create a Tree234 object
		Tree234 tree234 = new Tree234();

		int[] arr1 = new int[20];
		// I will use a for loop to generate the random numbers
		for (int i = 0; i < 20; i++)
		{
			// insert each random number to the tree
			int n = r.nextInt(80);
			arr1[i] = n;
		}
        
        System.out.println("I will sort the randomly generated numbers \n using a 2-3-4 Tree");
		sort(arr1);
               
	}

	public static void sort(int[] array)
	{
		Tree234 tree1 = new Tree234();
		//insert the values into the tree

		for (int i = 0; i < array.length; i++)
		{
			tree1.add(array[i]);
		}
       
		System.out.println("Calling the sort method to sort the array.");
		tree1.sort1(array);
        tree1.printTree();
        
        System.out.println("\n\nShows the Inorder Traversal of the tree");
        tree1.inorderTraversal();
	}
}
