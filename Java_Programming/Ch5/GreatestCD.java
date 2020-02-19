//returns GCD using Euclidian Algorithm
public class GreatestCD 
{

	public static void main(String[] args) 
	{
		gcd(24, 84); //example 
		
	}
	
	public static void gcd(int a, int b)
	{
		while( b != 0)
		{
			//swap the values and continue to mod b by temp % b until its zero
			int temp = a;
			a = b;
			b = temp % b;
			
			
		}
		System.out.println(a);
			
	}

}
