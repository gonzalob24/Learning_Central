// Write a complete Java program in a class named StarFigures that generates the
// following output.
// Use static methods to show structure and eliminate redundancy in your
// solution.

/*
 *****
 *****
 * *
 *
 * *
 *****
 *****
 * 
 * *
 *
 * *
 *****
 *****
 *
 *
 *
 *****
 *****
 * 
 * *
 *
 * *
 */

public class Exercise13_StarFigures
{
	public static void main(String[] args)
	{
		bar();
		x();
		System.out.println();
		bar();
		x();
		bar();
		System.out.println();
		line();
		bar();
		x();
	}

	public static void bar()
	{
		System.out.println("*****");
		System.out.println("*****");
	}

	public static void x()
	{
		System.out.println(" * *");
		System.out.println("  *");
	}

	public static void line()
	{
		System.out.println("  *");
		System.out.println("  *");
		System.out.println("  *");
	}
}
