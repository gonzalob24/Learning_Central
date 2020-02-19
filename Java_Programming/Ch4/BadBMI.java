// A poorly designed version of the BMI case study program.  This program
// handles one person's BMI, but it would be difficult to modify it to handle
// two because of the bad decomposition and chaining.

import java.util.*;

public class BadBMI {
    public static void main(String[] args) {
        System.out.println("This program reads data for one");
        System.out.println("person and computes his/her body");
        System.out.println("mass index and weight status.");
        System.out.println();

        Scanner console = new Scanner(System.in);
        person(console);
    }

    public static void person(Scanner console) {
        System.out.println("Enter next person's information:");
        System.out.print("height (in inches)? ");
        double height = console.nextDouble();
        getWeight(console, height);
    }

    public static void getWeight(Scanner console, double height) {
        System.out.print("weight (in pounds)? ");
        double weight = console.nextDouble();
        reportStatus(console, height, weight);
    }

    public static void reportStatus(Scanner console, double height,
                                    double weight) {
        double bmi = weight / (height * height) * 703;
        System.out.println("Person #1 body mass index = " + bmi);
        if (bmi < 18.5) {
            System.out.println("underweight");
        } else if (bmi < 25) {
            System.out.println("normal");
        } else if (bmi < 30) {
            System.out.println("overweight");
        } else {
            System.out.println("obese");
        }
    }
}
