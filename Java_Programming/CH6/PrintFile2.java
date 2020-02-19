//you are asked to write a method named printEntireFile that prompts the user for a 
//file name and printed that file's contents to the console. Modify your code from 
//that problem into a new method named printEntireFile2 that will repeatedly prompt 
//until the user types the name of a file that exists on the system.
import java.util.*;
import java.io.*;

public class PrintFile2 
{

	public static void main(String[] args) 
			throws FileNotFoundException
	{
		Scanner console = new Scanner(System.in);
		printEntireFile2(console);
	}
	
	//Method that will ask for file name check if it exists and print entire file
	public static void printEntireFile2(Scanner console)
			throws FileNotFoundException
	{
		System.out.print("Type a file name: ");
		String name = console.nextLine();
		File fname = new File(name);
		
		while (!fname.exists())
		{
			System.out.print("File does not exist enter a new file name: ");	
			name = console.nextLine();
			fname = new File(name);
		}
		
		Scanner output = new Scanner(fname);
		
		while(output.hasNext()) 
		{
			System.out.println(output.nextLine());
		}
		
	}

}
