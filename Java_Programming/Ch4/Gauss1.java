// Simple program that prompts the user for a value of n and that computes the
// sum of the integers 1 to n.

import java.util.*;

public class Gauss1 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("number? ");
        int num = console.nextInt();
    
        int answer = calcSum(num);
        System.out.println("sum = " + answer);
    }

    // takes in a positive integer max    
    // returns the sum of 1 up to given max
    public static int calcSum(int max) {
        int sum = 0;
        for (int i = 1; i <= max; i++) {
            sum = sum + i;
        }
        return sum; 
    }
}