//Program that reduces spaces when it prints out the lines of code


import java.util.*;
import java.io.*;

public class CollapseSpaces {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner input = new Scanner(new File("CollapseSpace.txt"));
		
		while ( input.hasNextLine() ) {
			String line = input.nextLine();
			Scanner newLine = new Scanner(line);

			while ( newLine.hasNext() )
				System.out.print(newLine.next() + " ");
	
			System.out.println();
		}
		
	}
	// Method call to remove spaces
	public static void removeSpace (Scanner input) {

		while ( input.hasNextLine() ) {
			String line = input.nextLine();
			Scanner newLine = new Scanner(line);

			while ( newLine.hasNext() )
				System.out.print(newLine.next() + " ");
	
			System.out.println();
		}
	}
}