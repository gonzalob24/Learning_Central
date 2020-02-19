
// random number generator

import java.util.*;

public class RandomNumbers
{
	public static void main(String[] args)
	{
		Random rand = new Random(); // random number generator

		int a = rand.nextInt(100); // 0 to 99
		int b = rand.nextInt(20) + 50; // 50 to 69
		int c = rand.nextInt(100) - 20; // -20 to 79
		int d = rand.nextInt(10) * 4; // 0, 4, 8, 12, 16, 20, 24, 28, 32, 36
	}
}
