// Write a method swapPairs that switches the order of values in an ArrayList of Strings in a pairwise fashion. 
// Your method should switch the order of the first two values, then switch the order of the next two, switch 
// the order of the next two, and so on. For example, if the list initially stores these values: 
// {"four", "score", "and", "seven", "years", "ago"} your method should switch the first pair, "four", 
// "score", the second pair, "and", "seven", and the third pair, "years", "ago", to yield this list: 
// {"score", "four", "seven", "and", "ago", "years"}

// If there are an odd number of values in the list, the final element is not moved. For example, if the original 
// list had been: {"to", "be", "or", "not", "to", "be", "hamlet"} It would again switch pairs of values, but 
// the final value, "hamlet" would not be moved, yielding this list: {"be", "to", "not", "or", "be", "to", "hamlet"}

import java.util.*;

public class SwapPairs 
{

	public static void main(String[] args) 
	{
		ArrayList<String> list = new ArrayList<String>(Arrays.asList("four", "score", "and", "seven", "years", "ago", "final"));
		
		System.out.println(list);
		swapPairs(list);
		System.out.println(list);
	}
	
	// Method that switched the order of ArrayList values of strings in a pairwise fashion
	
	public static void swapPairs(ArrayList<String> lst1)
	{
		for (int i = 0 ; i < lst1.size() - 1; i+=2)
		{
			String temp = lst1.get(i);
			lst1.set(i, lst1.get(i + 1));
			lst1.set(i + 1, temp);
		}
		
	}

}
