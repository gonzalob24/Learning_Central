//Write nested for loops to produce the following output:
/*
    1
   2
  3
 4
5
*/

public class SpacedNumbers {
	public static void main(String[] args) {
		for (int line = 1; line <= 5; line++) {
			for (int space = 1; space <= (-line + 5); space++) {
				System.out.print(" ");
			}
			System.out.println(line);
		}
	}
}
