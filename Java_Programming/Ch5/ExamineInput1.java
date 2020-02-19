//This program will examin input

import java.util.*;

public class ExamineInput1 {
	public static void main(String[] args) {
		System.out.println("This program examines the ways");
		System.out.println("a toke can be read.");
		System.out.println();

		Scanner console = new Scanner(System.in);

		System.out.print("token? ");
		System.out.println(" hasNextInt = " + console.hasNextInt() ); //we can interpret a token as an int
		System.out.println(" hasNextDouble = " + console.hasNextDouble() ); //we can also interpret as a double

		System.out.println("hasNext = " + console.hasNext() ); //we can read it as a string
	}

}