//write nested for loops to produce the following output, with each line 60 characters wide:
/*
         |         |         |         |         |         |
123456789012345678901234567890123456789012345678901234567890
*/

public class Output60 {
	public static void main(String[] args) {
		for (int times = 1; times <= 6; times++) {
			for (int space = 1; space <= 9; space++) {
				System.out.print(" ");
			}
			System.out.print("|");
		}
		System.out.println();

		for (int num = 1; num <= 6; num++) {
			for(int i = 1; i <= 9; i++) {
				System.out.print(i);
			}
			System.out.print("0");
		}
		System.out.println();
	}
}
