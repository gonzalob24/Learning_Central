//Write a method called min that takes three integers as parameters and returns the smallest of the three values, 
//such that a call of min(3, -2, 7) would return -2, and a call of min(19, 27, 6) would return 6. 
//Use Math.min to write your solution.

public class Minimum {
	public static void main(String[] args) {
		System.out.println(min(3, 6, 9));

	}

	//static method called min
	public static int min(int a, int b, int c) {
		int min1 = Math.min(a, b);
		int min2 = Math.min(min1, c);

		return min2; 

	}
}
