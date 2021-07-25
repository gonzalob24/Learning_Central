package UCB.Project1B;

import java.io.*;
import java.util.*;

//import edu.princeton.cs.algs4.In;

/**
 * This class outputs all palindromes in the words file in the current directory.
 */

public class PalindromeFinder
{
	public static void main(String[] args) throws FileNotFoundException
	{
		int minLength = 4;
		Scanner in = new Scanner(new File("words.txt"));
		Palindrome palindrome = new Palindrome();

		while (in.hasNext())
		{
			String word = in.nextLine();
			if (word.length() >= minLength && palindrome.isPalindrome(word))
			{
				System.out.println(word);
			}
		}
	}
}

