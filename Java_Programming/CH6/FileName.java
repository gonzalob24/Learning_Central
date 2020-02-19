import java.io.*;
import java.util.*;

public class FileName 
{

	public static void main(String[] args) 
			throws FileNotFoundException, IOException
	{
		Scanner console = new Scanner(System.in);
		getFileName(console);
	}
	
	public static String getFileName(Scanner console)
	throws FileNotFoundException, IOException
	{
	    System.out.println("Enter file name");
	    String name = console.nextLine();
	    File fname = new File(name);
	    
	    while(!fname.exists())
	    {
	            System.out.print("File does not exist, enter a new name: ");
	            name = console.nextLine();
	            fname = new File(name);
	            
	        
	        
	    }
	    return name;
	                  
	}

}
