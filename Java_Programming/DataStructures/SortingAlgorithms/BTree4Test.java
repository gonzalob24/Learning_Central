package SortingAlgorithms;
/*
 * PROGRAMMER: Gonzalo Betancourt
 *
 * COURSE: CSCI 3352-02 Adv. Data Structures
 *
 * DATE: April 15, 2020
 *
 * ASSIGNMENT: Programing Assignment: B Tree degree 4
 *
 * ENVIRONMENT: Mac OS, Windows or Linux
 *
 * FILES INCLUDED: B4Node, BTree4 class, BTreeeTest Driver class
 *
 * PURPOSE: Implement B Tree degree 4. 
 *          Ran my program on some sample data, random generated.
 *          Choose arrays with at least 20 elements 
 *          
 *          I used a random generator to create the array then sorted it with program
 *
 * PRECONDITIONS:
 *            Store the integers in an integer array
 *            All positive integers
 *
 * OUTPUT: Array of  numbers are stored in tree and 
 *         Inorder traversal to show sorted array
 *
 * POSTCONDITIONS: The program will return a sorted array
 *
 * ALGORITHMS:
 *            B Tree
                            
              
              
 * Sample Output:
    In order Traversal
    4 8 10 13 22 29 34 39 43 44 50 54 69 72 77 81 84 92 95 97 

 */


import  java.util.Random;


public class BTree4Test
{
    public static void main(String[] args)
    {
        // The default degree is 4
        BTree4 bt = new BTree4();
        
        Random r = new Random();
        
        for (int i = 0; i < 20; i++)
        {
            int num = r.nextInt(100);
            bt.add(num);
        }
        
        System.out.println("In order Traversal");
        bt.printTree();
    }
}