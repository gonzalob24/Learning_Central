public class ShowTwos
{
    public static void main(String[] args)
    {
        showTwo(120);

    }

    public static void showTwo(int number)
    {
        int count = 0;
        int tempNum = number;
        while (number % 2 == 0)
        {
        
            number = number / 2;
            count++;
        }
        System.out.print(tempNum + " = ");
        for (int i = 1; i <= count; i++)
        {
            System.out.print(2 + " * " );
        }
        System.out.println(number);
    }
}    