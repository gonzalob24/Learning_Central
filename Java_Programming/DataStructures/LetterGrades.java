
/*
 * PROGRAMMER: Gonzalo Betancourt
 *
 * COURSE: CSCI 2315-02 Data Structures
 *
 * DATE: September 11, 2019
 *
 * ASSIGNMENT: Homework #1
 *
 * ENVIRONMENT: Mac OS, Windows or Linux
 *
 * FILES INCLUDED: Java Source code, Screen shot of working code, problem
 * solving document
 *
 * PURPOSE: A problem statement of what is done
 *
 * INPUT: Data used as input described here
 *
 * PRECONDITIONS: Assumptions for correct execution of this code
 *
 * OUTPUT: Output data is indicated
 *
 * POSTCONDITIONS: Only positive integers are input if user enter any number
 * less than 0 the program will quit
 *
 * ALGORITHM: How the program works. This should be structured using short,
 * descriptive phrases that are indented appropriately. At the beginning of the
 * program, you will have an overall algorithm to describe the flow of the
 * entire program. For each nontrivial module an algorithm will describe how
 * that module works or will make a very specific reference to an existing
 * algorithm (eg.QuickSort, BinarySearch), if a well-known algorithm is used.
 *
 *
 * ERRORS: What happens in case of unexpected input (optional)
 *
 * EXAMPLE: Please enter your grade using integers 1-100 (-1 to exit): 85 Your
 * 85.00 is equivalent to a B.
 *
 * Please enter your grade using integers 1-100 (-1 to exit): 32 Your 32.00 is
 * equivalent to an F. 
 *
 *
 * HISTORY: Useful if a sequence of assignments is based on the same project
 * (optional)
 *
 */

import java.util.Scanner;

public class LetterGrades
{
	public static void main(String[] args)
	{
		// creates a scanner object to get input from the user
		Scanner console = new Scanner(System.in);

		problem1Intro();
		problem1Display(console);
	}

	// Introduce the program to the user
	public static void problem1Intro()
	{
		System.out.println("RK, this program will convert your interger grade from 1-100 ");
		System.out.println("into an equivalent letter grade.");
		System.out.println("In order to exit the program you may enter any number less than 0.\n\n");

	}

	// static method that calculated the letter grade equivalence to integer
	// grade.
	public static String letterToGrade(double grade)
	{
		String letterGrade;

		if (grade > 90)
		{
			letterGrade = "A";
		} else if (grade > 80)
		{
			letterGrade = "B";
		} else if (grade > 70)
		{
			letterGrade = "C";
		} else if (grade > 60)
		{
			letterGrade = "D";
		} else // grade is less than 60
		{
			letterGrade = "F";
		}

		return letterGrade;

	}

	// Static method that will display the results for problem 1
	public static void problem1Display(Scanner console)
	{
		System.out.print("Please enter your grade using integers 1-100 (to exit enter any value < 0): ");
		double grade = console.nextDouble(); // integer grade is stored here

		String letterGrade; // the letter grade is going to be used in the print
		while (!(grade < 0))
		{
			letterGrade = letterToGrade(grade);
			String correct = "";

			// Checks for correct grammar
			if ((letterGrade == "A") || (letterGrade == "F"))
			{
				correct = "an";

			} else
			{
				correct = "a";
			}

			System.out.printf("Your %.2f is equivalent to %s %s.\n\n", grade, correct, letterGrade);
			System.out.print("Please enter your grade using integers 1-100 (to exit enter any value < 0): ");
			grade = console.nextDouble();
		}
		System.out.println("Thank you, good bye.");
		console.close();
	}
}