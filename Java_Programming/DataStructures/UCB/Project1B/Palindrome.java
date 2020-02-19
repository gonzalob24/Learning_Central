package UCB.Project1B;

import java.util.*;

import UCB.Project1.DIntNode;
import UCB.Project1.LinkedListDeque;

/**
 * A class for palindrome operations.
 */
public class Palindrome<Any> extends LinkedListDeque<Any>
{
	public ASLList<Character> wordToDeque(String word)
	{
		ASLList<Character> ld = new LinkedListDeque<>();

		for (int i = 0; i < word.length(); i++)
		{

			ld.addLast(word.charAt(i));
		}
		return ld;
	}

	/**
	 * wordToDeque on reverse order
	 */
	public ASLList<Character> wordToDequeReverse(String word)
	{
		ASLList<Character> ld2 = new LinkedListDeque<>();

		for (int i = 0; i < word.length(); i++)
		{

			ld2.addFirst(word.charAt(i));
		}
		return ld2;
	}

	/**
	 * Checks weather or not the word is a palindrome
	 */
	public boolean isPalindrome(String word)
	{
		return checkCharsForPalindrome(word, 0);
	}

	private boolean checkCharsForPalindrome(String word, int index)
	{
		ASLList<Character> one = wordToDeque(word);
		ASLList<Character> reverse = wordToDequeReverse(word);

		if (one.get(index) != reverse.get(index))
		{
			return false;
		}
		if (index >= one.size() - 1)
		{
			return true;
		}
		return checkCharsForPalindrome(word, index + 1);
	}
}
