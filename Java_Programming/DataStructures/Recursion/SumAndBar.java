/*
 * PROGRAMMER: Gonzalo Betancourt
 * 
 * COURSE: CSCI 2315-02 Data Structures
 * 
 * DATE: October 2, 2019
 * 
 * ASSIGNMENT: Homework #3
 * 
 * ENVIRONMENT: Mac OS, Windows or Linux
 * 
 * FILES INCLUDED: Program Solving document, screen shot of working code and
 * SumAndBar source file
 * 
 * PURPOSE: Program will perform recursion in summing a fractions from 1 +
 * 1/2...1/n)
 * 
 * PRECONDITIONS: n cannot be zero
 * 
 * OUTPUT: sum of fractions from 1 t0 1/(n-1)
 * 
 * POSTCONDITIONS: the program will return a sum as a double
 * 
 * ALGORITHM: 1 + 1/2 ... + 1/n
 * 
 * 
 * EXAMPLE: x = 1 + 1/2 + 1/3 + 1/4 = 2.083.
 * 
 * 
 */

package Recursion;

import java.util.*;

public class SumAndBar
{

	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		System.out.println("This application will calculate the solution for the following function: ");
		System.out.println("x = 1 + 1/2 + 1/3 + 1/4 + ... 1/(n-1) + 1/n\n");
		System.out.print("Please enter an integer: ");
		int n = input.nextInt();

		System.out.printf(" = %2.3f", sum(n));
		System.out.println("\n\n");

		System.out.print("Please enter an integer from (1 - 10): ");
		int maxStars = input.nextInt();
		starBars(1, maxStars);

		// String test = recursivebar(n2);
		// recursivebar(n2);
		// stars(5);
		// stars(4);
		// halfDiamond(4);
		// stars2(4);
		// printStars(2);
		input.close();
	}

	// pre: n >=1
	// post: sum > 0
	// Program that will accept an integer and return the sum as a fraction
	public static double sum(int n)
	{
		double sum = 0;
		if ((double) n == 1)
		{
			System.out.print("x = 1");
			return 1;
		} else
		{
			sum += (double) 1 / n + sum(n - 1);
			System.out.print(" + 1/" + n);
			return sum;
		}
	}

	// method that recursively prints the number of stars in a
	// increasing and decreasing way
	public static void starBars(int start, int end)
	{
		printStars(start);
		if (start < end)
		{
			starBars(start + 1, end);
			printStars(start);
		}
	}

	// Method that prints however many stars you tell it
	public static void printStars(int numOfStars)
	{
		if (numOfStars == 1)
		{
			System.out.println("*");
		} else
		{
			System.out.print("*");
			printStars(numOfStars - 1);
		}
	}

	/*
	 * 
	 * 
	 * The code below is not part of my program
	 * I was simply working on trying to make the stars patter
	 * by using only one recursive call.
	 * 
	 * 
	 * 
	 * 
	 */
	// pre: n >= 1 || n <= 10
	// post:
	public static String ten(int n)
	{
		String top = "";
		String bottom = "";
		if (n == 0)
		{
			return "";
		} else

		{
			top += "*" + ten(n % 10 - 1);
			bottom += "*";
			System.out.print(top);
			System.out.println();

			// s = "";
			// ten(n % 10 - 1);
			// s += "*";
			// System.out.println(s);

			// System.out.print(s);
			// System.out.print(s);
			// ten(n % 10 - 1);
			return top;
		}
	}

	// Method that will print the number of stars in a bar format
	public static String halfDiamond(int n)
	{
		String s = "";
		if (n == 0)
		{
			return "";
		} else
		{
			s += "*" + halfDiamond(n - 1);
			System.out.println(s);
			return s;
		}
	}

	public static void stars(int n)
	{
		if (n == 0)
		{
			return;
		} else
		{
			System.out.print("*");
			stars(n - 1);
		}
	}

	public static void stars2(int n)
	{

		if (n == 0)
		{
			return;
		} else
		{

			stars(n);
			System.out.println();
			stars2(n - 1);

		}
	}
}
