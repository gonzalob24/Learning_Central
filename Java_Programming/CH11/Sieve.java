import java.util.*;

public class Sieve
{

	public static void main(String[] args)
	{
		System.out.println("This program will tell you all prime");
		System.out.println("numbers up to a given max.");
		System.out.println();

		Scanner console = new Scanner(System.in);
		System.out.print("Max number is: ");
		int max = console.nextInt();

		List<Integer> primes = sieve(max);
		System.out.print("Prime numbers up to " + max + ": ");
		System.out.print(primes);
		console.close();
	}

	// Return a list of prime numbers up to a given max
	// using the sieve of Eratosthenes algorithm
	public static List<Integer> sieve(int max)
	{
		List<Integer> primes = new LinkedList<>();

		// add all numbers from 2 to max to a list
		List<Integer> numbers = new LinkedList<>();
		for ( int i = 2; i <= max; i++ )
		{
			numbers.add(i);
		}

		while (!numbers.isEmpty())
		{
			// remove a prime number from the front of the list
			int front = numbers.remove(0);
			primes.add(front);

			// remove all multiples of this prime number
			Iterator<Integer> itr = numbers.iterator(); // Iterator is used for
														// numbers because that
														// is the list we are
														// traversing
			while (itr.hasNext())
			{
				int current = itr.next();
				if (current % front == 0)
				{
					itr.remove();
				}
			}
		}
		return primes;
	}

}
