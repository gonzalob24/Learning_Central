public class TryCatchService
{
    //private int number;

    public int sumAll(int number)
    {   
        int sum = 0;
        int ones = number % 10; //1
        int tens = (number % 100) / 10;
        int hundreds = (number % 1000) / 100;
        int thousands = (number % 10000) / 1000;
        int tenthou = number / 10000;
        
        return sum = ones + tens + hundreds + thousands + tenthou;
    }
}