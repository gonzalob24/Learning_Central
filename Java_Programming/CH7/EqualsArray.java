//Write a method called equals that takes in two string arrays and returns true if they are equal; that is, 
//if both arrays have the same length and contain equivalent string values at each index.
import java.util.*;

public class EqualsArray 
{
	public static void main(String[] args)
	{
		String[] array1 = {"the", "bird", "flys"};
		String[] array2 = {"the", "bird", "flys"};
		
		System.out.println(equals(array1, array2));
	}
	public static boolean equals(String[] array1, String[] array2)
	{
		if (Arrays.equals(array1, array2))
		{
			return true;
		}
		else 
		{
			return false;
		}
	}
	
	public static boolean allLess(int[] int1, int[] int2)
	{
		if (int1.length != int2.length)
		{
			return false;
		}
		else
		{	
			for (int i = 0; i < int1.length; i++)
			{
				if (int1[i] >= int2[i])
				{
					return false;
				}
			}
		}
		return true;
	}
}
