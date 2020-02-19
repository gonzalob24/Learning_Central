package Recursion;

public class Fib
{

    public static void main(String[] args)
    {
        for (int i = 1; i <= 4; i++)
        {
            System.out.println("After " + i + " months " + fib(i) + " pairs of rabbits.");
        }

        System.out.println(fib(5));
    }

    // Program that calculates the fib sequence
    public static int fib(int n)
    {
        if (n <= 1)
        {
            return n;
        } else
        {
            return fib(n - 1) + fib(n - 2);
        }
    }
}
