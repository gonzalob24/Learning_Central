// Mixed examples from the book

import java.util.*;  //for the scanner

public class Mixed {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		/*
		System.out.print("What is your favorite color: ");
		String name = console.next();

		if ( name.equalsIgnoreCase("blue") ) {
			System.out.println("Mine too!");
		}
		*/

		int numBills1 = spending(console, "John");

		System.out.println("John needs " + numBills1 + " bills");
	}

	public static int spending(Scanner console, String name) {
		System.out.print("How much will " + name + " be spending? ");
		double amount = console.nextDouble();

		int numBills = (int) (amount / 20.0);

		if ( numBills * 20.0 < amount ) {
			numBills++;
		}

		return numBills;
	}
}