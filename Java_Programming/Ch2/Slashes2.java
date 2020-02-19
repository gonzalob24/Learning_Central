//Modify the Slashes program to use a global constant for the figures height
/*
SIZE 7						        SIZE 4
!!!!!!!!!!!!!!!!!!!!!!		!!!!!!!!!!!!!!
\\!!!!!!!!!!!!!!!!!!//		\\!!!!!!!!!!//
\\\\!!!!!!!!!!!!!!////		\\\\!!!!!!////
\\\\\\!!!!!!!!!!//////		\\\\\\!!//////
\\\\\\\\!!!!!!////////
\\\\\\\\\\!!//////////
*/

public class Slashes2 {

public static final int HEIGHT = 7;

	public static void main(String[] args) {
		for (int line = 1; line <= HEIGHT; line++) {
			for (int bslash = 1; bslash <= (2 * line - 2); bslash++) {
				System.out.print("\\");
			}
			for (int mark = 1; mark <= (-4 * line + (HEIGHT * 4 + 2)); mark++) {
				System.out.print("!");
			}
			for (int fslash = 1; fslash <= (2 * line - 2); fslash++) {
				System.out.print("/");
			}
			System.out.println();
		}
	}
}
