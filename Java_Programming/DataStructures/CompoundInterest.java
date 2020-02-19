
/*
 * PROGRAMMER: Gonzalo Betancourt
 * 
 * COURSE: CSCI 2315-02 Data Structures
 * 
 * DATE: September 11, 2019
 * 
 * ASSIGNMENT: Homework #1 Problem 2
 * 
 * ENVIRONMENT: Eclipse IDE, MacOS
 * 
 * FILES INCLUDED: Java Source code, Screen shot of working code, problem
 * solving document
 * 
 * PURPOSE: The program is to calculate the total investment and total earnings
 * when the interest rate and principal amount is given.
 * 
 * INPUT: interest rate in decimal 0.00 and principal amount in dollars.
 * 
 * PRECONDITIONS: Interest rate and principal must be positive values
 * 
 * OUTPUT: output will be yearly print statements that show the total investment
 * and total earnings
 * 
 * POSTCONDITIONS: The total earning will be more than the principal amount
 * after 40 years. At $500 per month investment with 6% rate and $2000 initial
 * investment the account should have at least 1 million.
 * 
 * ALGORITHM: Ask the user for interest rate and principal amount.
 * rate = a #
 * principal = a #
 * call compounding formula and print yearly results
 * Total = (Total + (Monthly * 12)) * (IntRate + 1)
 * 
 * ERRORS: If an error occurs the program will exit
 * 
 * EXAMPLE:  
 * Please enter an interest rate (0.00): 6
 * Please enter an initial investment: 2000
 * 
 * Year Total Invested Total Earned
 * 
 * 1 $8000.00 $8480.00
 * 2 $14480.00 $15348.80
 * 3 $21348.80 $22629.73
 * 4 $28629.73 $30347.51
 * 
 */

import java.util.*;

public class CompoundInterest
{

	public static void main(String[] args)
	{
		// Creates a Scanner object to ask user for input
		Scanner console = new Scanner(System.in);

		problem2Intro();
		System.out.print("Please enter an interest rate (0.00): ");
		double rate = console.nextDouble();
		System.out.print("Please enter an initial investment: ");
		double principal = console.nextDouble();
		System.out.println();
		compounding(rate, principal);
	}

	// Introduction to problem 2
	public static void problem2Intro()
	{
		System.out.println("This program will calculate the compounding interest with a for loop.");
		System.out.println("You will need to input an interest rate in decimal form and start");
		System.out.println("with a principle investment of $2, 000.00, the code will run for 40 years");
		System.out.println("and output 40 annual totals.\n\n");

	}

	// Calculates and displays the total annual outputs for 40 years.
	public static void compounding(double rate, double principal)
	{
		double intRate = rate / 100 + 1;
		double monthly_investment = 500;
		double total_earned = 0;
		double initial_investment = principal;
		double total_investment = initial_investment;

		System.out.printf("%-5s %-15s %-15s", "Year", "Total Invested", "Total Earned");
		System.out.println("\n");
		for ( int years = 1; years <= 40; years++ )
		{
			total_investment += (monthly_investment * 12);
			total_earned = total_investment * intRate;
			System.out.printf("%-8d $%-13.2f $%-1.2f", years, total_investment, total_earned);
			total_investment = total_earned;
			System.out.println();
		}
		System.out.println();
	}
}
