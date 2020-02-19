//Write a do/while loop that repeatedly prints random numbers between 0 and 1000 until a number above 900 
//that is, greater than or equal to 900) is printed. At least one line of output should always be printed,
//even if the first random number is above 900. Here is a sample execution:

import java.util.*;

public class Random900 {
	public static void main(String[] args) {
		Scanner consol = new Scanner(System.in);
		Random r = new Random();

		int randomNum;
		do {
			randomNum = r.nextInt(1001);
			System.out.println("Random number:" + randomNum);
		} while ( randomNum < 900 );
	}
}

