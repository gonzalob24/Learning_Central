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

public class GradeBook
{
	private String courseName; // name of course this grade book represents
	private int[][] grades; // two-dimensional array of student grades

	// two-argument constructor initializes courseName and grades array
	public GradeBook(String name, int[][] gradesArray)
	{
		courseName = name; // initialize courseName
		grades = gradesArray; // store grades
	} // end two-argument GradeBook constructor

	// method to set the course name
	public void setCourseName(String name)
	{
		courseName = name; // stores the course name
	} // end method setCourseName

	// method to retrieve the course name
	public String getCourseName()
	{
		return courseName;
	} // end method getCourseName

	// display a welcome message to the GradeBook user
	public void displayMessage()
	{
		// getCourseName gets the name of the course
		System.out.printf("Welcome to the grade book for\n%s!\n\n", getCourseName());
	} // end method displayMessage

	// perform various operations on the data
	public void processGrades()
	{
		// output grades array by calling method
		outputGrades();
		// call methods getMinimum and getMaximum
		System.out.printf("\n%s %d\n%s %d\n\n", "Lowest grade in the grade book is", getMinimum(),
				"Highest grade in the grade book is", getMaximum());
		// output grade distribution chart of all grades on all tests
		outputBarChart();
	} // end method processGrades

	// find minimum grade
	public int getMinimum()
	{
		// assume the first element of grades array is smallest
		int lowGrade = grades[0][0];
		// loop through rows
		for ( int[] studentGrades : grades )
		{
			// loop through columns of current row
			for ( int grade : studentGrades )
			{
				if (grade < lowGrade)
				{
					lowGrade = grade;
				}
			}
		}
		return lowGrade;
	}

	// find maximum grade
	public int getMaximum()
	{
		// assume first element is the highes
		int highGrade = grades[0][0];
		// loop through rows
		for ( int[] studentGrades : grades )
		{
			// loop through columns of current row
			for ( int grade : studentGrades )
			{
				if (grade > highGrade)
				{
					highGrade = grade;
				}
			}
		}
		return highGrade;
	}

	// determine average grade for particular student (or set of grades)
	public double getAverage(int[] setOfGrades)
	{
		int total = 0;
		// sum grades for one student
		for ( int grade : setOfGrades )
		{
			total += grade;
		}
		return (double) total / setOfGrades.length;
	}

	// output bar chart displaying overall grade distribution
	public void outputBarChart()
	{
		System.out.println("Grade Distribution:");
		int[] frequencies = new int[11];

		// for each grade in grade book increment the appropriate frequency
		for ( int[] studenGrades : grades )
		{
			for ( int grade : studenGrades )
			{
				++frequencies[grade / 10];
			}
		}
		// print the bar chart
		for ( int count = 0; count < frequencies.length; count++ )
		{
			if (count == 10)
			{
				System.out.printf("%5d: ", 100);
			} else
			{
				System.out.printf("%02d-%02d: ", count * 10, count * 10 + 9);
			}
			// print bar of asterisks
			for ( int stars = 0; stars < frequencies[count]; stars++ )
			{
				System.out.print("*");
			}
			System.out.println();
		}
	}

	// output the contents of the grades array
	public void outputGrades()
	{
		System.out.printf("The grades are:%n%n");
		System.out.print("	      ");
		// create a column heading for each of the tests
		for ( int test = 0; test < grades[0].length; test++ )
		{
			System.out.printf("Test%d   ", test + 1);
		}
		System.out.println("Average"); // student average column heading
		// create rows/columns of text representing array grades
		for ( int student = 0; student < grades.length; student++ )
		{
			System.out.printf("Student %2d", student + 1);
			for ( int test : grades[student] ) // output student's grades
			{
				System.out.printf("%8d", test);
			}
			// call method getAverage to calculate student's average grade;
			// pass row of grades as the argument to getAverage
			double average = getAverage(grades[student]);
			System.out.printf("%9.2f%n", average);
		}
	}
} // end class GradeBook
