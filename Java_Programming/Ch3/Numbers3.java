//program that takes two integers as parameters and returns the larger of the two absolute values. A call of 
//largerAbsVal(11, 2) would return 11, and a call of largerAbsVal(4, -5) would return 5.

import java.util.*; //for scanner

public class Numbers3 {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		System.out.println("Please type in any two digits and "); 
		System.out.print("I will return the larger of the the absolute values: ");

		int one = console.nextInt();
		int two = console.nextInt();

		System.out.println(largerAbsVal(one, two));
	}

	//method that prints the largest abs value between two digits
	public static int largerAbsVal(int one, int two) {
		return Math.max(Math.abs(one), Math.abs(two));
	}
}
