//two integer parameters, a min and a max, and prints the numbers in the range from min to max inclusive in a square pattern. 

import java.util.*; //for the scanner

public class Numbers {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		System.out.print("Please type in min and max number: ");
		int min = console.nextInt();
		int max = console.nextInt();

		printSquares(min, max);

	}
	//method that prints the numbers in a square pattern
	public static void printSquares(int min, int max) {

		for (int i = min; i <= max; i++) { //prints the first row min - max
			System.out.print(i);
		}
 		System.out.println();
    
    //prints the rest in a square pattern
 		for (int line = min + 1; line <= max; line++) {
	 		for (int j = line; j <= max; j++) {
	 			System.out.print(j);
	 		}
	 		for (int end = min; end <= line - 1; end++) {
	 			System.out.print(end);
 			}
 			System.out.println();
 		}	
	}
}
