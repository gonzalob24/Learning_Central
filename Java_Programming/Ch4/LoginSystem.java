// An example of using several String methods. This is a weak login
// system that will print out a special message given the correct password

import java.util.*;

public class LoginSystem
{
	public static void main(String[] args)
	{
		Scanner console = new Scanner(System.in);
		System.out.print("What is your full name? ");
		String name = console.nextLine();
		int spaceIndex = name.indexOf(" ");
		String firstName = name.substring(0, spaceIndex);

		System.out.print("RK, " + firstName + " what is your password? ");
		String password = console.nextLine();
		String realPassword = "jgrasp123";
		if (password.equals(realPassword))
		{
			System.out.println("you win!");
		} else
		{
			System.out.println("take a hike!");
		}

	}
}
