package Recursion;

public class Palindrome
{

	public static void main(String[] args)
	{
		boolean test = isPal("zerorez");
		System.out.println(test);
	}

	// Program that checks to see if the word is a palindrome
	public static boolean isPal(String s)
	{
		if (s.length() == 0 || s.length() == 1)
		{
			return true;
		} else if (s.charAt(0) == s.charAt(s.length() - 1))
		{
			return isPal(s.substring(1, s.length() - 1));
		} else
		{
			return false;
		}
	}
}
