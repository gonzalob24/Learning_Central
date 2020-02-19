package UCB;

public class QuickFindDS implements DisjointSets
{
	private int[] id;

	/**
	 * this algorithm is 0(N)
	 */
	public QuickFindDS(int n)
	{
		id = new int[n]; //create an empty array of size n
		for (int i = 0; i < n; i++)
		{
			id[i] = i;
		}
	}

	/**
	 * we need to iterate through the array 0(N) times
	 */
	@Override
	public void connect(int p, int q)
	{
		int pid = id[p];
		int qid = id[q];
		for (int i = 0; i < id.length; i++)
		{
			if (id[i] == pid)
			{
				id[i] = qid;
			}
		}
	}

	/**
	 * 0(1) constant time
	 */
	@Override
	public boolean isConnected(int p, int q)
	{
		return id[p] == id[q];
	}

}
