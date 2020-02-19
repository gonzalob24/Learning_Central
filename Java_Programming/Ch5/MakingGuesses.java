//Write a method named makeGuesses that will guess numbers between 1 and 50 inclusive until it 
//makes a guess of at least 48. It should report each guess and at the end should report the 
//total number of guesses made. Below is a sample execution:

import java.util.*;

public class MakingGuesses 
{

	public static void main(String[] args)
	{
		Random rand = new Random();
		makeGuesses(rand);

	}
	
	//method that will guess the numbers between 1 and 50 inclusive until it makes a guess
	//of at least 48
	
	public static void makeGuesses(Random rand)
	{
		int guesses = 0;
        int number;
		
		do
		{
			guesses++;
			number = rand.nextInt(50) + 1;
            System.out.println("guess = " + number);
		}while (number <= 48);
		System.out.println("total guesses = " + guesses);
	}
}
