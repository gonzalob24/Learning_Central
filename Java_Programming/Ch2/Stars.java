//Write for loops to produce the following output:
//*****
//*****
//*****
//*****

public class Stars {

	public static final int LINES = 20;
	public static void main(String[] args) {
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 5; j++){
				System.out.print("*");
			}
			System.out.println();
		}
		System.out.println();
		drawCone();
	}

	public static void drawCone() {
		for (int i = 1; i <= LINES; i++) {
			for (int k = LINES; k > i; k--) {
				System.out.print(" ");
			}
			for (int j = 1; j <= i * 2 - 1; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
