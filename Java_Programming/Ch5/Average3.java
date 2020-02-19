//Write code that prompts for three integers, averages them, and prints the average. 
//Make your code robust against invalid input; if the user types a non-number, 
//re-prompt with the same prompt message.

import java.util.*;  //import the scanner

public class Average3 {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		int number = 0;
    
    //prompts the user for the digits 
		for (int i = 1; i <= 3; i++) {
    		System.out.print("Type an integer: ");
    		while ( !console.hasNextInt() ) {
        		console.next();     //discards the previous input
        		System.out.print("Type an integer: ");
    		}
    		int newNumber = console.nextInt();
    		number = newNumber + number;   
		}
    	double average = (number / 3.0);
    	System.out.println("Average: " + average);
	}
}
