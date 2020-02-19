// Write a complete Java program in a class named Egg2 that generates the
// following output.
// Use static methods to show structure and eliminate redundancy in your
// solution.
/*
 * _______
 * / \
 * / \
 * \ /
 * \_______/
 * -"-'-"-'-"-
 * _______
 * / \
 * / \
 * \ /
 * \_______/
 * -"-'-"-'-"-
 * \ /
 * \_______/
 * _______
 * / \
 * / \
 * -"-'-"-'-"-
 * \ /
 * \_______/
 */

public class Exercise10_Egg2
{
	public static void main(String[] agrs)
	{
		topOfEgg();
		bottomOfEgg();
		midLine();
		topOfEgg();
		bottomOfEgg();
		midLine();
		bottomOfEgg();
		topOfEgg();
		midLine();
		bottomOfEgg();
	}

	// This static method will produce the top of the egg

	public static void topOfEgg()
	{
		System.out.println("  _______");
		System.out.println(" /       \\");
		System.out.println("/         \\");
	}

	// This static methid will produce the bottom of the egg
	public static void bottomOfEgg()
	{
		System.out.println("\\         /");
		System.out.println(" \\_______/");
	}

	// This static method will produce the line
	public static void midLine()
	{
		System.out.println("-\"-'-\"-'-\"-");
	}
}
