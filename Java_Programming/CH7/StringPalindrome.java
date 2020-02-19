//Write a method isPalindrome that accepts an array of Strings as its argument 
//and returns true if that array is a palindrome (if it reads the same forwards 
//as backwards) and /false if not. For example, the array 
//{"alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"} is a palindrome, 
//so passing that array to your method would return true. Arrays with zero or 
//one element are considered to be palindromes.


public class StringPalindrome 
{
	public static void main(String[] args) 
	{
		String[] one = {"alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"};
		System.out.println(isPalindrome(one));
	}
	
	//method that determines of the String array is palindrome or not
  //I feel like there is a better solution because I am comparing the entire string twice
  //I will try another solution later. In which I cut my array in half and compare both half only one time.
	public static boolean isPalindrome(String[] array)
	{
		boolean flag = true;
		if (array.length == 0 || array.length == 1)
		{
			flag = true;
		}
		else
		{	
			int count = 0;
			for (int i = array.length - 1; i >= 0; i--)
			{
				if (array[count].equals(array[i]))
				{
					flag = true;
				}
				else
				{
					flag = false;
				}
				count++;
			}
		}
		
		return flag;
	}
}
