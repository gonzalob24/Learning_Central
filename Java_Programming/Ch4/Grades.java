// Short program to interact with a user and print out what grade they
// earned depending on the percentage they give
import java.util.*;

public class Grades {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("What percentage did you earn? ");
        int percent = console.nextInt();       

	percent = curveUp(percent);
        
        if (percent >= 90) {
            System.out.println("You got an A!");
        } else if (percent >= 80) {  // implied that percent < 90
            System.out.println("You got a B!");
        } else if (percent >= 70) {
            System.out.println("You got a C!");
        } else if (percent >= 60) {
            System.out.println("You got a D!");
        } else { // percent < 60
            System.out.println("You got a F!");
        }
        System.out.println("congrats on your grade!");
    }

    // takes a given percent and returns that percent 
    // curved up by a strange curving strategy
    public static int curveUp(int percent) {
	System.out.println("old percent: " + percent);
	int curve;
	if (percent < 50) {
	    curve = 10;
	} else { // percent >= 50
	    curve = 5;
	}
	percent = percent + curve;
	System.out.println("percent after curve: " + percent);
	return percent;
    }
}
