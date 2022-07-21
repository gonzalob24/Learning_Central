package four.conditionals;

import java.util.Scanner;

public class MenuClient {

    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Enter number 1: ");
        int num1 = console.nextInt();
        System.out.print("Enter number 2: ");
        int num2 = console.nextInt();

        System.out.println("1- Add");
        System.out.println("2- Subtract");
        System.out.println("3- Divide");
        System.out.println("4- Multiply");

        System.out.println("Select an option");
        int choice = console.nextInt();

        performOperation(choice, num1, num2);

        System.out.println(num1 == 5 ? "Yes" : "NO!!!");
    }

    public static void performOperation(int choice, int num1, int num2) {
        switch (choice) {
            case 1:
                System.out.println("Addition: " + (num2 + num2));
                break;
            case 2:
                System.out.println("Subtract: " + (num1 + num1));
                break;
            case 3:
                System.out.println("Divide: " + (num1 / num2));
                break;
            default:
                System.out.println("Multiply: " + (num1 * num2));
                break;
        }
    }
}
