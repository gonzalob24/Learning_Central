/*
 * PROGRAMMER: Gonzalo Betancourt
 * 
 * COURSE: CSCI 2315-02 Data Structures
 * 
 * DATE: September 11, 2019
 * 
 * ASSIGNMENT: Homework #1 Problem 3: GradeBook and GradeBookTest
 * 
 * ENVIRONMENT: Eclipse IDE, MacOS
 * 
 * FILES INCLUDED: Gradebook.java, GradebookTest.java, Screen shots of working
 * code and Problem Solving document
 *
 * PURPOSE: Program that takes in an Array of 30 Grades (integer) and returns
 * the maximum grade, minimum grade, average of all grades, and prints a Bar
 * Chart to show the grade distribution.
 * 
 * INPUT: An array of 30 integers
 * 
 * PRECONDITIONS: grades will be positive values
 * 
 * OUTPUT: Lowest and highest grades. overall distribution represented by a bar
 * chart
 * 
 * POSTCONDITIONS: None
 * 
 * ALGORITHM: There will be 10 students and 3 tests per student
 * Ask the user to input 30 grades into the array
 * program will display the lowest and highest grades in the array
 * Display the average test score per user (sum of test scores) / 3
 * 
 * 
 * ERRORS: if a user inputs a negative grade the program will catch the error
 * and ask the user to input valid data
 * 
 * EXAMPLE:
 * Test 1 Test 2 Test 3 Average
 * Student 1 87 96 70 84.33
 * Student 2 68 87 90 81.67
 * 
 * Lowest grade in the grade book is 65
 * Highest grade in the grade book is 100
 * 
 * Overall grade distribution: 00-09:
 * 10-19:
 * 20-29:
 * 30-39:
 * 40-49:
 * 50-59:
 * 60-69: ***
 * 70-79: ******
 * 80-89: ***********
 * 90-99: *******
 * **100: ***
 * 
 */

public class GradeBookTest
{
	// main method begins program execution
	public static void main(String[] args)
	{
		// two-dimensional array of student grades
		int[][] gradesArray = { { 87, 96, 70 }, { 68, 87, 90 }, { 94, 100, 90 }, { 100, 81, 82 }, { 83, 65, 85 },
				{ 78, 87, 65 }, { 85, 75, 83 }, { 91, 94, 100 }, { 76, 72, 84 }, { 87, 93, 73 } };

		GradeBook myGradeBook = new GradeBook("CSCI_2315 Introduction Data Structures!", gradesArray);
		myGradeBook.displayMessage();
		myGradeBook.processGrades();
	}
} // end main// end class GradeBookTest
