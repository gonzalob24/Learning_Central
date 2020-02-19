//Write nested for loops to produce the following output:
/*
    1
   22
  333
 4444
55555
*/

public class MoreNumbers {
	public static void main(String[] args) {
		for (int line = 1; line <= 5; line++) {
			for (int space = 1; space <= (-line +5); space++) {
				System.out.print(" ");
			}
			for (int number = 1; number <= line; number++) {
				System.out.print(line);
			}
			System.out.println();
		}
	}
}
