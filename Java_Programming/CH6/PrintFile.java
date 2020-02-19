//Write a method named printEntireFile that prompts the user for a file name and prints 
//the contents of that file to the console as output. You may assume that the file exists. 
//For example, if the file example.txt contains the following input data:
import java.util.*;
import java.io.*;

public class PrintFile 
{

	public static void main(String[] args) 
			throws FileNotFoundException

	{
		Scanner console = new Scanner(System.in);
		printEntireFile(console);
	}
	//Method that prints the entire file
	public static void printEntireFile(Scanner console) 
			throws FileNotFoundException
	{
		System.out.print("Type a file name: ");
		String name = console.next();
		Scanner output = new Scanner(new File(name));
		
		while(output.hasNextLine())
		{
			System.out.println(output.nextLine());
		}
		
		
	}

}
