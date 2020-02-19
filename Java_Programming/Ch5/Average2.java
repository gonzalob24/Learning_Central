//Write a method named printAverage that accepts a Scanner for the 
//console as a parameter and repeatedly prompts the user for numbers. 
//Once any number less than zero is typed, the average of all 
//non-negative numbers typed is displayed. Display the average as a 
//double, and do not round it. For example, a call to your method 
//might look like this:

/*
Type a number: 7
Type a number: 4
Type a number: 16
Type a number: -4
Average was 9.0
*/

import java.util.*;

public class Average2 {

	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		printAverage(console);
		

	}
	//Method that diplays the integers inputed and displays as a double.
	//Sentinal value is any number < 0;
	public static void printAverage(Scanner console) {
		double sum = 0.0;
    int count = 0;
    System.out.print("Type a number: ");
		int number = console.nextInt();
     	
    if ( number >= 0 ){
	    while (number >= 0) {
			  sum = number + sum;
				System.out.print("Type a number: ");
				number = console.nextInt();
        count++;
			}
			System.out.println("Average was " +  (double) sum/count);
		}
	}
}
