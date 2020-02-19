// The Fibonacci numbers are a sequence of integers in which the first two
// elements are 1,
// and each following element is the sum of the two preceding elements.
// The mathematical definition of each kth Fibonacci number is the following:
// F(k):
// k > 2 : F(k-1) + F(k-2)
// k <= 2 : 1
// First 12 numbers are: 1 1 2 3 5 8 13 21 34 55 89 144

public class Fibonacci
{
	public static void main(String[] args)
	{
		int first_number = 1;
		int second_number = 0;
		int third_number;

		for (int i = 1; i <= 12; i++)
		{
			System.out.print(first_number + " ");

			third_number = first_number + second_number;
			second_number = first_number;
			first_number = third_number;
		}

		System.out.println("\nfib2 function: " + fib2(12));

	}

	public static int fib2(int n)
	{
		int i, fac = 1;

		for (i = 2; i <= n; i++)
		{
			fac += 2 * i;
		}
		return fac;
	}
}
