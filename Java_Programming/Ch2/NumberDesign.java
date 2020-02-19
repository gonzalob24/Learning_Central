//Write a method called printDesign that produces the following output. 
//Use nested for loops to capture the structure of the figure.
/*

-----1-----
----333----
---55555---
--7777777--
-999999999-

*/


public class NumberDesign {
	public static void main(String[] args) {
		for (int line = 1; line <= 9; line+=2) {
			for (int dash = 1; dash <= (-line / 2 + 5); dash++) {
				System.out.print("-");
			}
			for (int number = 1; number <= line; number++) {
				System.out.print(line);
			}
			for (int dash = 1; dash <= (-line / 2 + 5); dash++) {
				System.out.print("-");
			}
			System.out.println();
		}
	}
}
