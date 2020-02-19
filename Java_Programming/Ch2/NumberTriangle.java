//Write for loops to produce the following output:
/*
1
22
333
4444
55555
666666
7777777
*/

public class NumberTriangle {
	public static void main(String[] args) {
		for (int line = 1; line <= 7; line++) {
			for (int i = 1; i <= line; i++) {
				System.out.print(line);
			}
			System.out.println();
		}
	}
}
