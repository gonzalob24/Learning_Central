//Computer will generate a number and ask the user to try and guess what the number is.
//If the guess is incorrect the computer will give a hint and tell the user
//if any of the digits are correct, the order does not matter.


import java.util.*;

public class NumberGuess {
	public static void main(String[] args) {
		intro();

		Scanner console = new Scanner(System.in);

		//pick a random number from 0 to 99
		Random rand = new Random();
		int number = rand.nextInt(100);

		System.out.print("Pick a number form 00 to 99: ");

		int guess = getGuess(console);
		int numGuesses = 1;

		//give hints until the correct guess is reached
		while (guess != number) {
			int numMathces = matches(number, guess);
			System.out.println("The number is incorrect. (hint: " + numMathces + " digists match) ");
			guess = getGuess(console);
			numGuesses++;
		}

		System.out.println("You got the number right in " + numGuesses + " tries.");
	}

	//Method that will calculate the number of digits that match what the user has input
	public static int matches(int number, int guess) {
		int numMathces = 0;

		if ( (guess / 10 == number / 10) || (guess / 10 == number % 10) ) {
			numMathces++;
		}

		if ( (guess / 10 != guess % 10) && ( (guess % 10 == number / 10) || (guess % 10 == number % 10) ) ) {
			numMathces++;
		}

		return numMathces;
	}

	//Methat that wll give an intro to the program
	public static void intro() {
		System.out.println("Try to guess  my two-digit number, and I will tell you how");
		System.out.println("many digists from your guess appear in my number.");
		System.out.println();
	}

	//Method that will test user input for invalid data guess < 0 and guess > 99
	public static int getInt(Scanner console, String prompt) {
		System.out.print(prompt);
		while ( !console.hasNextInt() ) {
			console.next(); //to discard the input
			System.out.println("Not an integer: try again: ");
			System.out.print(prompt);
		}

		return console.nextInt();
	}

	//Method that gets the guess
	public static int getGuess(Scanner console) {
		int guess = getInt(console, "Your guess? ");
		while ( guess < 0 || guess >= 100 ) {
			System.out.println("Out of range; try again.");
			guess = getInt(console, "Your guess? ");
		}

		return guess;
	}
}














