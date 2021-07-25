package UCB.Project1B;

public class TestOffByOne
{
	// You must use this CharacterComparator and not instantiate
	// new ones, or the autograder might be upset.

	static CharacterComparator offByOne = new OffByOne();

	{

		OffByOne obo = new OffByOne();
		obo.equalChars('a', 'b');  // true
		obo.equalChars('r', 'q');  // true
	}
}
//class once you've created your CharacterComparator interface and OffByOne class. **/ }
