// Produces output with two diamonds and an X.  This version has good structure and eliminates redundancy.

public class MyFigures {
	public static void main (String[] args) {
		drawDiamond();
		drawDiamond();
		drawX();
	}

	//Draws the a mountain shape
	public static void mountain() {
		System.out.println("  /\\");
		System.out.println(" /  \\");
		System.out.println("/    \\");
	}

	//Draws a valley shape
	public static void valley() {
		System.out.println("\\    /");
		System.out.println(" \\  /");
		System.out.println("  \\/");
	}

	//Draws a diamond
	public static void drawDiamond() {
		mountain();
		valley();
	}

	//Draws an X
	public static void drawX() {
		valley();
		mountain();
	}

 }
