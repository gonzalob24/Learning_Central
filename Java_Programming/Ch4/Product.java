//Write code to produce a cumulative product by multiplying together many 
//numbers that are read from the console. Match the following format:

/*
How many numbers? 4
Next number --> 7
Next number --> 2
Next number --> 3
Next number --> 15
Product = 630
*/

import java.util.*;
public class Product {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		System.out.print("How many numbers? ");
		int numbers = console.nextInt();
		System.out.println("Product = " + cumulative(console, numbers));
		
		
	}

	public static int cumulative(Scanner console, int numbers) {
		int count = 1;
		for (int i = 1; i <= numbers; i++) {
			System.out.print("Next number --> ");
			int next = console.nextInt();

			count *= next;
		}
	return count;
	}
}