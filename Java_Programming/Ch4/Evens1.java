
// Simple program that prompts the user for a value of n and
// prints if it is even or odd

import java.util.*;

public class Evens1
{
	public static void main(String[] args)
	{
		Scanner console = new Scanner(System.in);
		System.out.print("number? ");
		int num = console.nextInt();

		// conditional execution
		// relational expressions: <expression> operator <expression>
		// relational operators: <, >, <=, >=, ==, !=

		if (num % 2 == 0)
		{
			System.out.println("this number is even!");
		} else
		{
			System.out.println("this number is odd!");
		}
	}
}