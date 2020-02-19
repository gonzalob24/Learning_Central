import java.util.*;
import java.io.*;

public class ReverseFileLines
{

	public static void main(String[] args) throws FileNotFoundException
	{
		File test = new File("text.txt");
		Scanner input = new Scanner((test));
		reverse(input);
	}

	public static void reverse(Scanner input)
	{
		if (input.hasNext())
		{
			String line = input.nextLine();
			reverse(input);
			System.out.println(line);
		} else
		{
			System.out.print("");
		}
	}
}
