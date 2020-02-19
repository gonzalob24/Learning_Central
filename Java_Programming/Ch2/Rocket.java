//This program will draw a rocket made up of variou sfigures
//n any given execution your program will produce just one version of this figure, 
//but it should be possible to change the value of the program constant to have your 
//program produce a figure of a different size.

/*
     /**\
    //**\\
   ///**\\\
  ////**\\\\
 /////**\\\\\
+=*=*=*=*=*=*+
|../\..../\..|
|./\/\../\/\.|
|/\/\/\/\/\/\|
|\/\/\/\/\/\/|
|.\/\/..\/\/.|
|..\/....\/..|
+=*=*=*=*=*=*+
|\/\/\/\/\/\/|
|.\/\/..\/\/.|
|..\/....\/..|
|../\..../\..|
|./\/\../\/\.|
|/\/\/\/\/\/\|
+=*=*=*=*=*=*+
     /**\
    //**\\
   ///**\\\
  ////**\\\\
 /////**\\\\\

*/

public class Rocket {

public static final int SIZE = 5;

	public static void main(String[] args) {
		drawTip();
		figureLine();
		triangleBody();
		valleyBody();
		figureLine();
		valleyBody();
		triangleBody();
		figureLine();
		drawTip();


	}

	//This static method draws the tip shape of the rocket
	public static void drawTip() {
		for (int line = 1; line <= (SIZE * 2 - 1); line++) {
			for (int space = 1; space <= (-line + SIZE * 2); space++) {
				System.out.print(" ");
			}
			for (int fslash = 1; fslash <= line; fslash++) {
				System.out.print("/");
			}
			System.out.print("**");
			for (int bslash = 1; bslash <= line; bslash++) {
				System.out.print("\\");
			}
			System.out.println();
		}
	}

	//This static method draws part of the top body of the rocket
	public static void triangleBody() {
		for (int line = 1; line <= SIZE; line++) {
			System.out.print("|");
			for (int dots = 1; dots <= (-line + SIZE); dots++) {
				System.out.print(".");
			}
			for (int triangle = 1; triangle <= line; triangle++) {
				System.out.print("/\\");
			}
			for (int moreDots = 1; moreDots <= (-2 * line + SIZE * 2); moreDots++) {
				System.out.print(".");
			}
			for (int triangle = 1; triangle <= line; triangle++) {
				System.out.print("/\\");
			}
			for (int dots = 1; dots <= (-line + SIZE); dots++) {
				System.out.print(".");
			}
			System.out.println("|");
		}
	}

	//Static method draws the +=* shape accross the rocket
	public static void figureLine() {
		System.out.print("+");
		for (int reps = 1; reps <= SIZE * 2; reps++) {
			System.out.print("=*");
		}
		System.out.println("+");
	}

	//Draws the bottom half of the body of part of the rocket
	public static void valleyBody() {
		for (int line = 1; line <= SIZE; line++) {
			System.out.print("|");
			for (int dots = 1; dots <= (line - 1); dots++) {
				System.out.print(".");
			}
			for (int valley = 1; valley <= (-line + (SIZE + 1)) ; valley++) {
				System.out.print("\\/");
			}
			for (int moreDots = 1; moreDots <= (2 * line - 2); moreDots++) {
				System.out.print(".");
			}
			for (int valley = 1; valley <= (-line + (SIZE + 1)); valley++) {
				System.out.print("\\/");
			}
			for (int dots = 1; dots <= (line - 1); dots++) {
				System.out.print(".");
			}
			System.out.println("|");
		}
	}

}















