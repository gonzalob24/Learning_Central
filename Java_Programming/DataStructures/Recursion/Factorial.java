package Recursion;

public class Factorial
{

	public static void main(String[] args)
	{
		System.out.println("n =  1: " + fact(1));
		System.out.println("n =  5: " + fact(5));
		System.out.println("n = 10: " + fact(10));
		System.out.println("n = 25: " + fact(25));
		System.out.println("n = 50: " + fact(200));

		int MyInt = 6;
		int a = fact(MyInt);

		System.out.printf("The factorial of %d is : %d\n", MyInt, a);

	}

	// Program that will perform the factorial of the number
	public static int fact(int n)
	{
		if (n == 1)
		{
			return 1;
		} else
		{
			return fact(n - 1) * n;
		}
	}
}
