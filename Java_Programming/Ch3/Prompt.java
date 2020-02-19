//Write code to read an integer from the user, then print that number multiplied by 2. 
//You may assume that the user types a valid integer. A sample run of the code would produce the following:

import java.util.*; //for the scanner

public class Prompt {
	public static void main(String[] args) {

		Scanner console = new Scanner(System.in);
		System.out.print("Type an integer: ");
		int number = console.nextInt();
		System.out.println(number + " times 2 = " + number * 2 );
	}
}