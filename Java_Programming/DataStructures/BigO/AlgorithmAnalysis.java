
package BigO;

public class AlgorithmAnalysis
{
	int seqStart;
	int seqEnd;

	/*
	 * Cubic maximum contiguous subsequence sum algorithm.
	 * seqStart and seqEnd represent the actual best sequence.
	 */

	public int maxSubsequenceSumCubic(int[] a)
	{
		int maxSum = 0;

		for ( int i = 0; i < a.length; i++ )
		{
			for ( int j = i; j < a.length; j++ )
			{
				int thisSum = 0;
				for ( int k = i; k <= j; k++ )
				{
					thisSum += a[k];
				}
				if (thisSum > maxSum)
				{
					maxSum = thisSum;
					seqStart = i;
					seqEnd = j;
				}
			}

		}
		return maxSum;
	}

	/*
	 * Quadratic maximum contiguous subsequence sum algorithm. * seqStart and
	 * seqEnd represent the actual best sequence.
	 */

	public int maxSubsequenceSumQuadratic(int[] a)
	{
		int maxSum = 0;
		for ( int i = 0; i < a.length; i++ )
		{
			int thisSum = 0;
			for ( int j = i; j < a.length; j++ )
			{
				thisSum += a[j];
				if (thisSum > maxSum)
				{
					maxSum = thisSum;
					seqStart = i;
					seqEnd = j;
				}
			}
		}
		return maxSum;
	}

	/*
	 * Linear maximum contiguous subsequence sum algorithm.
	 * seqStart and seqEnd represent the actual best sequence.
	 */

	public int maxSubsequenceSumLinear(int[] a)
	{
		int maxSum = 0;
		int thisSum = 0;
		for ( int i = 0, j = 0; j < a.length; j++ )
		{
			thisSum += a[j];
			if (thisSum > maxSum)
			{
				maxSum = thisSum;
				seqStart = i;
				seqEnd = j;
			} else if (thisSum < 0)
			{
				i = j + 1;
				thisSum = 0;
			}

		}
		return maxSum;
	}

}
