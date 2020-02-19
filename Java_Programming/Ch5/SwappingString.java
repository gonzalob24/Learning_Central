//Write a method named swapPairs that accepts a String as a parameter and returns that String with 
//each pair of adjacent letters reversed. If the String has an odd number of letters, the last 
//letter is unchanged. For example, the call swapPairs("forget") should return "ofgrte" and the call 
//swapPairs("hello there") should return "ehll ohtree".

public class SwappingString 
{

	public static void main(String[] args) 
	{
		String line = swapPairs("example");
		System.out.println(line);
			
	}
	//Method that swaps adjacent characters in a string
	public static String swapPairs(String line)
	{
		String result = "";
		for (int index1 = 0; index1 < line.length() / 2; index1++)
		{
			result += line.charAt(2 * index1 + 1);
			result += line.charAt(2 * index1);
			
		}
		
		if (line.length() % 2 != 0)
		{
			result += line.charAt(line.length() - 1);
		}
		
		return result;
	}
}
