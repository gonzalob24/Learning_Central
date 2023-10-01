// Write a complete Java program in a class named TwoRockets that generates the
// following output.
// Use static methods to show structure and eliminate redundancy in your
// solution.
// Note that there are two rocket ships next to each other.
// What redundancy can you eliminate using static methods? What redundancy
// cannot be eliminated?

public class Exercise11_TwoRockets
{
	public static void main(String[] args)
	{
		cone();
		box();
		usa();
		box();
		cone();
	}

	// This static method produces the top of the rockets
	public static void cone()
	{
		System.out.println("   /\\       /\\");
		System.out.println("  /  \\     /  \\");
		System.out.println(" /    \\   /    \\");
	}

	// This static method produces part of the body of the rocket
	public static void box()
	{
		System.out.println("+------+ +------+");
		System.out.println("|      | |      |");
		System.out.println("|      | |      |");
		System.out.println("+------+ +------+");
	}

	// This static method produces the box with the words United State
	public static void usa()
	{
		System.out.println("|United| |United|");
		System.out.println("|States| |States|");
	}
}
