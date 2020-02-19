//Write nested for loops that produce the following output:
/*
000111222333444555666777888999
000111222333444555666777888999
000111222333444555666777888999
*/

public class NestedNumbers {
	public static void main(String[] args) {
		for (int line = 1; line <= 3; line++) {
			for (int number = 0; number <= 9; number++) {
				for (int i = 1; i <= 3; i++) {
					System.out.print(number);
				}
			}
			System.out.println();
		}
	}
}
