///Writes characters and multiple times by passing arguments to the method call

public class DrawChars {
	public static void main(String[] args) {
		characters(20, '=');
		System.out.println();
		for (int i = 1; i <= 10; i++) {
			characters(i, '>');
			characters(20 - 2 * i, ' ');
			characters(i, '<');
			System.out.println();
		}
	}

	//method call that writes characters by passing some parameters
	public static void characters(int number, char ch) {
		for ( int i = 1; i <= number; i++) {
			System.out.print(ch);
		}
	}
}