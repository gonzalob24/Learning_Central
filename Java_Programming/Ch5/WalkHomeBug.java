import java.util.*;

public class WalkHomeBug 
{

	public static void main(String[] args) 
	{
		Random rand = new Random();
		walkHome(2, rand);
		System.out.println("----------------------");
		walkTwo(2, rand);
	}
	public static void walkHome(int start, Random rand)
	{
		int total = 0;
		int end = 0;
		int distance = start;
		int steps = start;
		System.out.println("Starting at " + steps);
		while(distance != end)
		{
			System.out.print("*");
			for (int i = 1; i <= steps; i++)
			{
				System.out.print("-");
			}
			System.out.println("|^|");
			int num = rand.nextInt(5) - 2;
			System.out.println("moving " + num + " step(s)");
			if (num <= 0)
			{
				distance += Math.abs(num);
				steps += Math.abs(num);
			} else 
			{
				distance -= num;
				steps -= num;
			}
			total += Math.abs(num);
		}
		System.out.println("*|^|");
		System.out.println("made it home in " + total + " step(s)");
	}
	
	//take two
	public static void walkTwo(int start, Random rand)
	{
		int total = 0;
		int distance = start;
		System.out.println("Starting at " + start);
		while(distance > 0)
		{
			System.out.print("*");
			for (int i = 1; i <= distance; i++)
			{
				System.out.print("-");
			}
			System.out.println("|^|");
			
			int steps = rand.nextInt(5) - 2;
			if (steps > distance)
			{
				steps = distance;	
			}
			distance -= steps;
			total += Math.abs(steps);
			System.out.println("moving " + steps + " step(s)");
		}
		System.out.println("*|^|");
		System.out.println("made it home in " + total + " step(s)");
	}
}
