
public class MultiCounter 
{

	public static void main(String[] args) 
	{
		int num = 229231007;
		int[] count = new int[10];
		
		while (num > 0)
		{
			int digit = num % 10;//get a digit and add to proper counter
			count[digit]++;  //increment that particular index
			num = num /10;
		}
		
		for (int nums : count)
		{
			System.out.print(nums + " ");
		}
	}

}
