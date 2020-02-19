//Write code that generates a random odd integer (not divisible by 2) between 50 and 99
//inclusive. Fill in the values of the sub-expressions labeled A, B, and C below.

import java.util.*;

public class RandomOddInt {
	public static void main(String[] args) {
		Random rand = new Random();

		int n = rand.nextInt(25) * 2 + 51;

		System.out.println(n);
		System.out.println(n);
	}
}
