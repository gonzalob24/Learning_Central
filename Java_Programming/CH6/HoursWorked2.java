import java.io.*;
import java.util.*;

public class HoursWorked2
{
    public static void main(String[] args) throws FileNotFoundException
    {
        Scanner input = new Scanner(new File("hours2.txt"));

        while (input.hasNextLine())
        {
            String text = input.nextLine();
            processLine(text);
        }
    }
    //process the given string line by line and selecting different pieces from it
    //recall why previus code did not work. While loop was rading next number as a
    //double and not int for the ID of the second person. And name was read as int not string
    public static void processLine(String text)
    {
        Scanner data = new Scanner(text);
        int id = data.nextInt();
        String name = data.next();
        double sum = 0;

        while (data.hasNextDouble())
        {
            sum += data.nextDouble();
        }
        System.out.println("Total hours worked by " + name + " (id# " + id + ") = " + sum);
    }
}