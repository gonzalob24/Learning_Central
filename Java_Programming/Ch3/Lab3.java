
public class Lab3 
{

	public static void main(String[] args) 
	{
		int number = 42;
        for (int i = 1; i <= 1000; i++) {
            number = number * 37 % 103;
        }
        System.out.println(number);
        int number2 = number * number;
        System.out.println("result = " + number2);

	}

}
