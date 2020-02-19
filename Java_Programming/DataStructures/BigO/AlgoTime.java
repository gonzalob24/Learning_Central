/*
 * Code that analysis algorithm and calculates running time
 */
package BigO;

import java.util.*;

public class AlgoTime
{

	public static void main(String[] args)
	{
		int[] arrayTest = { 10, 20, 50, 100, 200 };
		Random random = new Random();
		AlgorithmAnalysis first = new AlgorithmAnalysis();
		for ( int i = 0; i < arrayTest.length; i++ )
		{
			// I will create the specified array each time through the loop
			int[] aTest = new int[arrayTest[i]];

			// Fillign array random integers with the range of integers between
			// -10 to 10.
			for ( int j = 0; j < arrayTest[i]; j++ )
			{
				aTest[j] = 1 + random.nextInt(20) - 10;
			}

			// calculating the time for each algorithm
			long startTime1 = System.nanoTime();
			int sum3 = first.maxSubsequenceSumLinear(aTest);
			long startTime2 = System.nanoTime();
			int sum2 = first.maxSubsequenceSumQuadratic(aTest);
			long startTime3 = System.nanoTime();
			int sum1 = first.maxSubsequenceSumCubic(aTest);
			long endTime = System.nanoTime();
			
			System.out.println("\n");
			
			// The following is the time taken for each algorithm
			System.out.println("Algorithm running time for input size " + arrayTest[i]);
			System.out.println("Cubic = " + (endTime - startTime3) + " nanoseconds");
			System.out.println("Quadratic  = " + (startTime3 - startTime2) + " nanoseconds");
			System.out.println("Linear = "  + (startTime2 - startTime1) + " nanoseconds");
		
		}
	}
}
