/*
 * PROGRAMMER: Gonzalo Betancourt
 * 
 * COURSE: CSCI 2315-02 Data Structures
 * 
 * DATE: September 18, 2019 
 * 
 * ASSIGNMENT: Homework 2
 * 
 * ENVIRONMENT: Mac OS, Windows or Linux
 * 
 * FILES INCLUDED: LowHighPair source code, screen shots of working code, problem solving document 
 * 
 * PURPOSE: This program will pull the low and high elements of an array after every pass
 * 			and store the elements in anothe array and display the results
 * 
 * PRECONDITIONS: The array can only accept integer values 
 * 
 * OUTPUT: displays the low, high pair values of the array
 * 
 * POSTCONDITIONS: all elements of the array are to be used
 * 
 * ALGORITHM:
 * traverse the array
 * get min and max values
 * store min and max in another array
 * delete min and max index of original array
 * repeat the process until all elements of original array are used
 *
 * EXAMPLE: 
 * Please enter the size of the array: 3
 * Please enter a value to fill array: 1
 * Please enter a value to fill array: 2
 * Please enter a value to fill array: 3
 *
 * The current values in the array are:
 * [1, 2, 3]
 *
 * The values in low, high format after each pass.
 * If the array is odd the high will print first.
 * [3, 1, 2]
 * 
 */


package BigO;

import java.util.*;

public class LowHighPair 
{

	public static void main(String[] args) 
	{
		ArrayList<Integer> a1 = new ArrayList<Integer>();
		
		Scanner input = new Scanner(System.in);
		System.out.print("Please enter the size of the array: ");
		int arraySize = input.nextInt(); //Size of the array
		
		//User will input array values to fill array
		while (arraySize - 1 >= 0)
		{
			System.out.print("Please enter a value to fill array: ");
			int num = input.nextInt();
			a1.add(num);
			arraySize--;
		}
		System.out.println("\nThe current values in the array are:");
		System.out.println(a1.toString());
		System.out.println();
		System.out.println("The values in low, high format after each pass.");
		System.out.println("If the array is odd the high will print first.");
		arrayLowHigh(a1);
		

	}
	//Application that will grab in pairs the low and and high values in the array after each pass
	public static void arrayLowHigh(ArrayList<Integer> array1)
	{
		ArrayList<Integer> results = new ArrayList<Integer>();
		
		int length_array = array1.size();
		int final_max = 0;
		
		//find max of array if array is odd length
		if (length_array % 2 != 0)
		{
			for (int n : array1)
			{
				if (n > final_max)
				{
					final_max = n;
				}
			}
			//remove final_max from array1
			array1.remove(array1.indexOf(final_max));
			results.add(final_max);
		}
		

		for (int i = 0; i < array1.size(); i++)
		{
			int max = -999;
			int min = 999;
			int n;
			for (n = 0; n < array1.size(); n++)
			{
				if (array1.get(n) < min)
				{
					min = array1.get(n);
				}
			}
			array1.remove(array1.indexOf(min));
			results.add(min);
			int n2;
			length_array = array1.size();
			
			for (n2 = 0; n2 < array1.size(); n2++)
			{
				if (array1.get(n2) > max)
				{
					max = array1.get(n2);
				}
			}
			array1.remove(array1.indexOf(max));
			results.add(max);
			i--;
		}
		
		System.out.println(results.toString());
	}
}
