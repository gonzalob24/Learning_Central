// Write a complete Java program in a class named EggStop that generates the
// following output.
// Use static methods to show structure and eliminate redundancy in your
// solution.

/*
 * ______
 * / \
 * / \
 * \ /
 * \______/
 * 
 * ______
 * / \
 * / \
 * \ /
 * \______/
 * +--------+
 * 
 * ______
 * / \
 * / \
 * | STOP |
 * \ /
 * \______/
 * +--------+
 */

public class Exercise15_EggStop
{
	public static void main(String[] args)
	{
		topofEgg();
		bottomofEgg();
		System.out.println();
		topofEgg();
		bottomofEgg();
		line();
		System.out.println();
		topofEgg();
		stop();
		bottomofEgg();
		line();
	}

	public static void topofEgg()
	{
		System.out.println("  ______");
		System.out.println(" /      \\");
		System.out.println("/        \\");
	}

	public static void bottomofEgg()
	{
		System.out.println("\\        /");
		System.out.println(" \\______/");
	}

	public static void line()
	{
		System.out.println("+--------+");
	}

	public static void stop()
	{
		System.out.println("|  STOP  |");
	}
}
