//Program that will compare two applicants for college admission. I will be using SAT or ACT, 
//GPA and the transcript multiplier.

import java.util.*;

public class Admit {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		intro();
		reportResults(console, 1, 2);

		
	}

	//Static method that will introduce to the user what the progrom will be doing.
	public static void intro() {
		System.out.println("This program compares two applicants to");
		System.out.println("determine which one seems like the stronger");
		System.out.println("applicant.  For each candidate I will need");
		System.out.println("either SAT or ACT scores plus a weighted GPA.");	
		System.out.println();

	}

	//Static method that will capture information from each user
	public static double satScores(Scanner console) {
		System.out.print("    SAT math? ");
		int satMath = console.nextInt();
		System.out.print("    SAT critical reading? ");
		int satReading = console.nextInt();
		System.out.print("    SAT writing? ");
		int satWrtiting = console.nextInt();

		double satScore = ( 2 * satMath + satReading + satWrtiting ) / 32;
		return satScore;
	}

	//Static method that gets GPA scores 
	public static double actScores(Scanner console) {
		System.out.print("    ACT English? ");
		int actEnglish = console.nextInt();
		System.out.print("    ACT math? ");
		int actMath = console.nextInt();
		System.out.print("    ACT reading? ");
		int actReading = console.nextInt();
		System.out.print("    ACT science? ");
		int actScience = console.nextInt();

		double actScore = ( actEnglish + 2 * actMath + actReading + actScience ) / 1.8;
		return actScore;
	}

	//Gets and returns GPA information 
	public static double gpa(Scanner console) {
		System.out.print("    overall GPA? ");
		double gpa = console.nextDouble();
		System.out.print("    max GPA? ");
		double maxGPA = console.nextDouble();
		System.out.print("    Transcript Multiplier? ");
		double transcript_mult = console.nextDouble();

		double gpaScore = (gpa / maxGPA) * 100 * transcript_mult;
		return gpaScore;
	}

	//method that determines which set of test scores the student needs to report
	public static double student(Scanner console, int student_number) {
		System.out.println("Information for applicant #:" + student_number);
		System.out.print("    do you have 1) SAT scores or 2) ACT scores? ");
		int choice = console.nextInt();

		double testScore = 0;
		if ( choice == 1) {
			testScore = satScores(console);
		} else { // choice == 2
			testScore = actScores(console);
		}

		System.out.printf("    exam score = %.1f\n", testScore);

		double gpaScore = gpa(console);
		System.out.printf("    GPA score = %.1f\n", gpaScore);
		System.out.println();

		return testScore + gpaScore;
	}

	//method that displays the results, it takes the number 1 and 2 for the number of student.
	public static void reportResults(Scanner console, int studentOne, int studentTwo) {
		double overallScore1 = student(console, studentOne);
		double overallScore2 = student(console, studentTwo);

		System.out.printf("First applicant overall score  = %.1f\n", overallScore1);
		System.out.printf("Second applicant overall score = %.1f\n", overallScore2);

		if ( overallScore1 > overallScore2 ) {
			System.out.println("The first applicant seems to be better");
		} else { // overallScore2 > overallScore1
			System.out.println("The second applicant is better");
		}
	}
}







