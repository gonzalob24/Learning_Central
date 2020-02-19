
// Write a method named lastFirst that accepts a string as its parameter
// representing a person's
// first and last name. The method should return the person's last name followed
// by the first
// initial and a period. For example, the call lastFirst("Marla Singer") should
// return "Singer,
// M." . You may assume that the string passed consists of exactly two words
// separated by a single space.

import java.util.*;

public class LName
{
	public static void main(String[] args)
	{
		System.out.println(lastFirst("Maria Singer"));

	}

	// Method that will accept a string and return last name, first name initial
	public static String lastFirst(String name)
	{
		String last = "";
		for ( int i = name.indexOf(" ") + 1; i < name.length(); i++ )
		{
			last += name.charAt(i);
		}

		return last + ", " + name.charAt(0) + ".";
	}
}