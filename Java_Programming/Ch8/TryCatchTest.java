import java.util.*;

public class TryCatchTest
{
    public static void main(String[] args)
    {   
        TryCatchService firstTest = new TryCatchService();

        Scanner input = new Scanner(System.in);
        int number = 0;
        int sum = 0;
        System.out.println(String.valueOf(sum).length());

        System.out.print("Please enter a 5 digit number: ");
        try
        {
            number = input.nextInt();
            if ( (String.valueOf(number).length()) == 5)
            {    
                sum = firstTest.sumAll(number);
            }
        }
        catch (NumberFormatException ex)
        {
            System.out.println("You did not enter enoufh numbers.");
        }
        
        System.out.printf("The sum of all the integers is %d: \n\n", sum);
    }
}