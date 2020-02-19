// Short program that reads a file of weather data
// and prints out the differences between each data point

import java.io.*;
import java.util.*;

public class Weather {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("weather.txt"));
        
        if (input.hasNextDouble()) { // check that the file has at least one data point
            double temp1 = input.nextDouble();
            while (input.hasNext()) {
		        double temp2 = input.nextDouble();
		        System.out.println("temp1: " + temp1 + ", temp2: " + temp2 +
				   ", difference: " + (temp2 - temp1));
		        temp1 = temp2;
            }
        }
    }
}
