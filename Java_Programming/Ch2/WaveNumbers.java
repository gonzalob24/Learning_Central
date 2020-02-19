//Write for loops to produce the following output, with each line 40 characters wide:
/*
----------------------------------------
_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-
1122334455667788990011223344556677889900
----------------------------------------
*/

public class WaveNumbers {
	public static void main(String[] args) {
		dashes();

		for (int i = 1; i <= 10; i++) {
			System.out.print("_-^-");
		}
		System.out.println();

		for (int times = 1; times <= 2; times++) {
			for (int i = 1; i < 10; i++) {
				for (int j = 1; j <= 2; j++) {
					System.out.print(i);
				}
			}
			System.out.print("00");
		}
		System.out.println();

		dashes();
	}

	//Static method that produces the dashes
	public static void dashes() {
		for (int i = 1; i <= 40; i++) {
			System.out.print("-");
		}
		System.out.println();
	}
}
