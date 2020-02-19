//static method printGrid that accepts two integer parameters rows and cols. 
//The output is a comma-separated grid of numbers where the first parameter (rows) 
//represents the number of rows of the grid and the second parameter (cols) represents 
//the number of columns. The numbers count up from 1 to (rows x cols). The output are displayed 
//in column-major order, meaning that the numbers shown increase sequentially down each column and 
//wrap to the top of the next column to the right once the bottom of the current column is reached. 
//Assume that rows and cols are greater than 0.

import java.util.*;

public class Numbers2 {
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);

		System.out.print("Please type in two numbers for rows and columns: ");
		int rows = console.nextInt();
		int cols = console.nextInt();

		printGrid(rows, cols);

	}

	//method printGrid that prints the numbers 1 to rows * col
	public static void printGrid(int rows, int cols) {
		int maxNumber = rows * cols;

		for (int i = 1; i <= rows; i++) {
			for ( int numbers = i; numbers <= maxNumber - rows; numbers += rows) {
				System.out.print(numbers + ", ");
			}
			for (int last = maxNumber - rows + i; last <= rows * cols; last+=rows) {
				System.out.print(last);
			}
			System.out.println();
		}
	}
}
