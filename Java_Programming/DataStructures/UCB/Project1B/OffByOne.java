package UCB.Project1B;


/**
 * A class for off-by-1 comparators.
 */
public class OffByOne implements CharacterComparator
{
	@Override
	public boolean equalChars(char x, char y)
	{
		if (Math.abs(x - y) == 1)
		{
			return true;

		} else
		{
			return false;
		}


	}
}
