// This file contains some examples of methods that students
// might be asked to write for the midterm.

import java.util.*;

public class Methods1 {
    public static void main(String[] args) {
        Random r = new Random();
        boolean result = seven(r);
        System.out.println();
        System.out.println("result = " + result);
        System.out.println();

        int sum = digitSum(935);
        System.out.println("sum = " + sum);
        System.out.println();

        roll7();
        System.out.println();
         
        String text = insertDashes("hello");
        System.out.println("insertDashes returned " + text);
    }
	
    // Write a static method called digitSum that takes an
    // integer n as a parameter and that returns the sum of the
    // digits of n.  You may assume n is not negative.
    public static int digitSum(int n) {
        int sum = 0;
       // n = 935
       // 9 + 3 + 5
       // 5 + 3 + 9
       // n % 10 -> 5
       // n / 10 -> 93
       // 935, 93, 9, 0
        while (n > 0) {
            int digit = n % 10;
            n = n / 10;
            sum = sum + digit;
        }
        return sum;
    }
	
    // Write a static method called seven that takes a Random
    // object as a parameter and that uses the random object to
    // generate up to 10 numbers between 1 and 30 inclusive,
    // printing them and stopping if the "lucky number" 7 comes
    // up and returning whether or not that happened.
    public static boolean seven(Random r) {
        for (int i = 1; i <= 10; i++) {
            int next = r.nextInt(30) + 1;
            System.out.print(next + " ");
            if (next == 7) {
                return true;
            }
        }
        return false;
    }

    // Write a static method called roll7 that simulates the
    // rolling of two dice until their sum is equal to 7.  The
    // method should print each roll and its sum and show a count
    // of how many rolls it took to get to 7, as in:
    //     3 + 5 = 8
    //     2 + 1 = 3
    //     1 + 4 = 5
    //     3 + 4 = 7
    //     sum of 7 after 4 rolls
    // You must exactly reproduce the format of this sample
    // execution.
    public static void roll7() {
        Random r = new Random();
        int sum = 0; // anything except 7, prime the loop
        int count = 0;
        while (sum != 7) {
            int roll1 = r.nextInt(6) + 1;
            int roll2 = r.nextInt(6) + 1;
            count++;
            sum = roll1 + roll2;
            System.out.println(roll1 + " + " + roll2 + " = " + sum);
        }
        System.out.println("sum of 7 after " + count + " rolls");
    }

    // Write a static method called insertDashes that takes a string
    // as a parameter and that returns a new string where in between
    // each pair of letters of the old string is a dash.  
    // For example, insertDashes("hello") should return "h-e-l-l-o".
    public static String insertDashes(String s) {
        String result = "";
        if (s.length() > 0) { // test to handle insertDashes("") case
            result += s.charAt(0); // fencepost, pull out one character
            for (int i = 1; i < s.length(); i++) {
                result += "-" + s.charAt(i);
            }
        }
        return result;
    }
}
