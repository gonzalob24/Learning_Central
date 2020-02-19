package UCB;

public interface DisjointSets
{
	/**
	 * connects to items p and q
	 */
	void connect(int p, int q);

	/**
	 * checks to see if two items are connected
	 */
	boolean isConnected(int p, int q);
}
