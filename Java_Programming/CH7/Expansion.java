import java.util.*;

public class Expansion
{

	public static void main(String[] args)
	{
		int[] firstArray = new int[3];
		
		//filling in the array with different values
		for (int i = 0; i < firstArray.length; i++)
		{
			firstArray[i] = i*2;
		}
		
		//creating a new array with contents of  firstArray and expanding to a new length
		int[] secondArray = Arrays.copyOf(firstArray, firstArray.length + 3);
		
		//creating temp array with contents of firstArray and expanding firstArray to new size
		
		//int[] tempArray = Arrays.copyOf(firstArray, firstArray.length);
		
		firstArray = Arrays.copyOf(firstArray, firstArray.length + 3);
		
		System.out.println("firstArray is " + Arrays.toString(firstArray));
		System.out.println("secondArray is " + Arrays.toString(secondArray));
		//System.out.println("tempArray is " + Arrays.toString(tempArray));
		System.out.println("Expansion of firstArray is " + Arrays.toString(firstArray));
	}

}
