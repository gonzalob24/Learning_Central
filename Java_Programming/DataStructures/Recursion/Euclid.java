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
 * FILES INCLUDED: Program Solving document, Euclid.java source file, screen
 * shot of working code
 * 
 * PURPOSE: Recursive algorith that will determine the GCD of a number. Complete
 * a test plan with at least 4 test cases
 * 
 * PRECONDITIONS: must be integers
 * 
 * OUTPUT: Program will return an integer as the result
 * 
 * POSTCONDITIONS: Number will be positive or zero
 * 
 * ALGORITHM: given two number
 * if b == 0 return a.
 * else return GCD(b, a % b);
 * 
 * 
 * EXAMPLE:
 * 
 * 
 */

package Recursion;

import java.util.*;

public class Euclid
{

	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		System.out.println("Please enter two numbers so that I can give you the GCD.");
		System.out.print("Enter number 1: ");
		int num1 = input.nextInt();
		System.out.print("Enter number 2: ");
		int num2 = input.nextInt();

		System.out.printf("The GCD for %d and %d is: %d", num1, num2, gcd(num1, num2));

	}

	// Program the will determine the GCD using Euclids Algorithm.
	public static int gcd(int a, int b)
	{
		if (b == 0)
		{
			return a;
		} else
		{
			return gcd(b, a % b);
		}
	}
}
