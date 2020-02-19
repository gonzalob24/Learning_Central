//Write a complete class named NumbersOutput. Use two class constants instead of "magic numbers,", 
//with one constant set to 6 for the number of repetitions, and the other set to 10 for the range of numbers. 
//Put the for loop code in your class's main method.
//Use REPS = 7 and RANGE = 5

public class OutputConstant {

public static final int REPS = 7;    //number of repetitions 
public static final int RANGE = 5;  //range of numbers

	public static void main(String[] args) {
		//Prints the spaces and the | at the end of the spaces
		for (int times = 1; times <= REPS; times++) {
			for (int space = 1; space < RANGE; space++) {
				System.out.print(" ");
			}
			System.out.print("|");
		}
		System.out.println();

		//prints the numbers 
		for (int num = 1; num <= REPS; num++) {
			for(int i = 1; i < RANGE; i++) {
				System.out.print(i);
			}
			System.out.print("0");
		}
		System.out.println();

	}
}
