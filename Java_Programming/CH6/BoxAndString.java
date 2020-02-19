import java.util.*;
import java.io.*;

public class BoxAndString 
{

	public static void main(String[] args) 
	throws FileNotFoundException 
	{
		Scanner input = new Scanner(System.in);
		//File fname = new File("text.txt");
		printBox(input, 12);
		
		
	}
	
	public static void printBox(Scanner input, int length)
			throws FileNotFoundException
	{
	
		System.out.print("Enter file name: ");
		String name = input.next();
		File fname = new File(name);
		Scanner output = new Scanner(fname);
		System.out.print("+-");
		for (int i = 0; i < length; i++)
		{
			System.out.print("-");
		}
		System.out.println("-+");

		while (output.hasNextLine())
		{	
			String line = output.nextLine(); //prints the line
			//System.out.println(line.length()); //length of a string
			System.out.print("| " + line);
			for (int i = 0; i < length - line.length(); i++)
				System.out.print(" ");
			System.out.println(" |");
		}
		System.out.print("+-");
		for (int i = 0; i < length; i++)
		{
			System.out.print("-");
		}
		System.out.println("-+");
	}

}
