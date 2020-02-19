//Write code that prompts the user for a phrase and a number of times to repeat it, 
//then prints the phrase the phrase that many times. 

import java.util.*; //for the scanner

public class Prompt2 {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		
		System.out.print("Type in a phrase: ");
		String phrase = console.nextLine();

		System.out.print("How many times would you like to repeat the phrase: ");
		int number = console.nextInt();

		for (int i = 1; i <= number; i++) {
			System.out.println(phrase);
		}
	}
}