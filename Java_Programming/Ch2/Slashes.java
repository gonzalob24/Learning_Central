//Use nested for loops to capture the structure of the figure.
/*
!!!!!!!!!!!!!!!!!!!!!!
\\!!!!!!!!!!!!!!!!!!//
\\\\!!!!!!!!!!!!!!////
\\\\\\!!!!!!!!!!//////
\\\\\\\\!!!!!!////////
\\\\\\\\\\!!//////////
*/

public class Slashes {
	public static void main(String[] args) {
		for (int line = 1; line <= 6; line++) {
			for (int bslash = 0; bslash <= (2 * line - 2); bslash++) {
				System.out.print("\\");
			}
			for (int mark = 1; mark <= (-4 * line + 26); mark++) {
				System.out.print("!");
			}
			for (int fslash = 0; fslash <= (2 * line - 2); fslash++) {
				System.out.print("/");
			}
			System.out.println();
		}
	}
}
