// A program to read in any number of real numbers from a file and find
//   the minimum and maximum values read. Assumes the file contains at
//   least one number and no other tokens.
//
// Note the use of .hasNextDouble() to determine if there are tokens remaining
//   in the file.
import java.io.*;
import java.util.*;

public class FindMinAndMax2 {
   public static void main(String[] args) throws FileNotFoundException {
      Scanner input = new Scanner(new File("numbers2.txt"));
      
      double number = input.nextDouble();
      System.out.println("Read number: " + number);
      
      double min = number;
      double max = number;
      int count = 1;
      
      while (input.hasNextDouble()) {
         number = input.nextDouble();
         count++;
         System.out.println("Read number: " + number);

         if (number > max) {
            max = number;
         }
         if (number < min) {
            min = number;
         }
      }
      
      System.out.println();
      System.out.println("Read " + count + " numbers.");
      System.out.println("Maximum value: " + max);
      System.out.println("Minimum value: " + min);
   }
}