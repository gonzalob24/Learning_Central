//Write a method named digitSum that accepts an integer as a parameter and returns the sum of the 
//digits of that number. For example, the call digitSum(29107) returns 2+9+1+0+7 or 19. For negative 
//numbers, return the same value that would result if the number were positive. For example, 
//digitSum(-456) returns 4+5+6 or 15. The call digitSum(0) returns 0.

public class SumOfDigits1 
{

	public static void main(String[] args) 
	{
		System.out.println(digitSum(29107));	
	}
	
	//Method that returns the sum of the digits
	public static int digitSum(int number)
	{
		int sum = 0;
		while (number > 0)
		{
			int tempNum = number % 10;
			number /= 10;
			sum += tempNum;
		
		}
		
		return sum;
	}
}
