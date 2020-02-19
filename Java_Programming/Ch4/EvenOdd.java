
// Write Java code to read an integer from the user, then print even if that
// number is an even number
// or odd otherwise. You may assume that the user types a valid integer.

import java.util.*;

public class EvenOdd
{

	public static void main(String[] args)
	{
		Scanner console = new Scanner(System.in);

		System.out.print("Please type in an integer and I will tell you if it even or odd: ");
		int number = console.nextInt();

		if (number % 2 == 0)
		{
			System.out.println("The number " + number + " is even.");
		} else
		{
			System.out.println("The nyumber " + number + " is odd.");
		}

		console.close(); // Closing the console
	}
}
