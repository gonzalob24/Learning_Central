import java.util.*;
import java.io.*;

public class CountWordsArrayList
{

	public static void main(String[] args) throws FileNotFoundException
	{
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the name of the file: ");
		String file = input.next();
		Scanner file1 = new Scanner(new File(file));

		ArrayList<String> list1 = new ArrayList<String>();
		int count = 0;

		while (file1.hasNext())
		{
			String word = file1.next();
			if (word.endsWith("s"))
			{
				list1.add(word);
				count++;
			}
		}

		System.out.println(list1 + " the number of plural words are " + count);

	}

}
