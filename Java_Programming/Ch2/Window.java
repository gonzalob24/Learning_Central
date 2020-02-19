//Write a Java program in a class named Window that produces the preceding figure as output. 
//Use nested for loops to print the repeated parts of the figure. Once you get it to work, 
//add one class constant to your program so that the size of the figure can be changed simply 
//by changing that constant's value. The example output shown is at a constant size of 3, 
//but if you change the constant, the figure should grow larger and wider proportionally.

//solve this problem using only ONE public static final constant, not multiple constants; 

/*
+===+===+
|   |   |
|   |   |
|   |   |
+===+===+
|   |   |
|   |   |
|   |   |
+===+===+
*/

public class Window {

public static final int SIZE = 3;

	public static void main(String[] args) {
		for (int times = 1; times <= 2; times++){
			for (int plus = 1; plus <= 2; plus++) {
				System.out.print("+");
				for (int equals = 1; equals <= SIZE; equals++) {
					System.out.print("=");
				}
			}
			System.out.println("+");

			for (int bars = 1; bars <= SIZE; bars++) {
				System.out.print("|");
				for (int reps = 1; reps <= 2; reps++) {
					for (int space = 1; space <= SIZE; space++){
					System.out.print(" ");
					}
					System.out.print("|");
				}
				System.out.println();
			}
		}
		for (int plus = 1; plus <= 2; plus++) {
				System.out.print("+");
			for (int equals = 1; equals <= SIZE; equals++) {
				System.out.print("=");
			}
		}
		System.out.println("+");
	}
}
