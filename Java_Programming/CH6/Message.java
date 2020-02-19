import java.util.*;
import java.io.*;

public class Message {

	public static void main(String[] args) 
	throws FileNotFoundException
	{
  		//writing output to a file
		Scanner input = new Scanner(System.in);
		System.out.print("Name of the file: ");
		String name = input.next();
		File fname = new File(name);
		PrintStream text = new PrintStream(fname);
		text.println("Testing,");
		text.println("1, 2, 3.");
		text.println();
		text.println("This is my output file.");
		
	}

}
