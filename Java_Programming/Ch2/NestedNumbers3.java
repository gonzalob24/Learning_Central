//Modify your code from NestedNUmbers to produce the following output:
/*
999999999888888887777777666666555554444333221
999999999888888887777777666666555554444333221
999999999888888887777777666666555554444333221
999999999888888887777777666666555554444333221
*/

public class NestedNumbers3 {
	public static void main(String[] args) {
		for (int line = 1; line <= 5; line++) {
			for (int number = 9; number > 0; number--) {
				for (int i = 1; i <= number; i++) {
					System.out.print(number);
				}
			}
			System.out.println();
		}
	}
}
