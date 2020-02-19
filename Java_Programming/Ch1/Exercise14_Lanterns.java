// Write a complete Java program in a class named Lanterns that generates the
// following three figures of output.
// Use static methods to show structure and eliminate redundancy in your
// solution.
// In particular, make sure that main contains no System.out.println statements,
// that any System.out.println statement(s)
// repeated are captured in a method that is called just once,
// and that the same System.out.println statement never appears in two places in
// the code.

public class Exercise14_Lanterns
{
	// This program draws lanterns
	public static void main(String[] args)
	{
		topOfLantern();
		midOfLantern();
		topOfLantern();
		bottomOfLantern();
	}

	public static void topOfLantern()
	{
		System.out.println("    *****");
		System.out.println("  *********");
		System.out.println("*************");
		System.out.println();
		lastPart();
	}

	public static void lastPart()
	{
		System.out.println("    *****");
		System.out.println("  *********");
		System.out.println("*************");
	}

	public static void midOfLantern()
	{
		System.out.println("* | | | | | *");
		System.out.println("*************");
	}

	public static void bottomOfLantern()
	{
		System.out.println("    *****");
		System.out.println("* | | | | | *");
		System.out.println("* | | | | | *");
		System.out.println("    *****");
		System.out.println("    *****");
	}
}
