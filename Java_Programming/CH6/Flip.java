//program flips output lines

import java.util.*;
import java.io.*;

public class Flip {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner input = new Scanner(new File("flips.txt") );

		flipLines(input);
	}

	//method that flips the lines of the output
	public static void flipLines(Scanner input) {
		while ( input.hasNextLine() ) {
			String one = input.nextLine();
			
			if ( input.hasNextLine() ) {
				String two = input.nextLine();
				System.out.println(two);
			}
			
			System.out.println(one);
		}
	}
}