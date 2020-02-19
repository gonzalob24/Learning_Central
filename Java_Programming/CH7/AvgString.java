//Write a method averageLength of code that computes and returns the average 
//String length of the elements of an array of Strings. For example, if the 
//array contains {"belt", "hat", "jelly", "bubble gum"}, the average length 
//returned should be 5.5. Assume that the array has at least one element.



public class AvgString 
{

	public static void main(String[] args) 
	{
		String[] one = {"belt", "hat", "jelly", "bubble gum"};
		double first = averageLength(one);
		System.out.printf("%.2f", first);
	}
  
	//method that returns the average string in the array
	public static double averageLength(String[] str)
	{
		double sum = 0;
		//traverse array and get the length of each String.
		for (String one : str)
		{
			sum += one.length();
		}
		return sum / str.length;
	}
}
