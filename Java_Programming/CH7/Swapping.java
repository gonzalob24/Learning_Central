//Write a method named swapPairs that accepts an array of strings as a parameter and switches 
//the order of values in a pairwise fashion. Your method should switch the order of the first 
//two values, then switch the order of the next two, switch the order of the next two, and 
//so on. For example, if the array initially stores these values:
import java.util.*;
public class Swapping 
{
	public static void main(String[] args)
	{
		String[] a = {"four", "score", "and", "seven", "years", "ago"};
		swapPairs(a);
		System.out.println(Arrays.toString(a));
		
		int[] numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
		for ( int i = 1; i < 10; i++)
		{
			numbers[i] = numbers[i - 1];
		}
		System.out.println(Arrays.toString(numbers));
	}
	
	public static void swapPairs(String[] array1)
	{
		for (int i = 0; i < array1.length - 1; i+=2)
		{
			String first = array1[i + 1];
			array1[i + 1] =  array1[i];
			array1[i] = first;
		}
	}
}
