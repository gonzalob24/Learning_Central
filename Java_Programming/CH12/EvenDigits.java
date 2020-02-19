/*
 * Write a method evenDigits that accepts an integer parameter n and that
 * returns the integer formed by removing the odd digits from n. The following
 * table shows several calls and their expected return values:
 * 
 * Call Valued Returned
 * 
 * evenDigits(8342116); ----- 8426
 * evenDigits(4109); -------- 40
 * evenDigits(8); ----------- 8
 * evenDigits(-34512);------- -42
 * evenDigits(-163505);------ -60
 * evenDigits(3052); -------- 2
 * evenDigits(7010496); ----- 46
 * evenDigits(35179); ------- 0
 * evenDigits(5307); -------- 0
 * evenDigits(7); ----------- 0
 * 
 * If a negative number with even digits other than 0 is passed to the method,
 * the result should also be negative, as shown above when -34512 is passed.
 * Leading zeros in the result should be ignored and if there are no even digits
 * other than 0 in the number, the method should return 0, as shown in the last
 * three outputs.
 * 
 */
public class EvenDigits
{

	public static void main(String[] args)
	{
		// String test = evenDigits(8342116);
		// System.out.println(test);

		int test2 = evenDigits2(412);
		System.out.println(test2);
	}

	// Static method that returns answer in String format
	public static String evenDigits(int n)
	{
		String num_string = "";
		if (n == 0)
		{
			return "";
		} else
		{
			int test_num = n % 10;
			if (test_num % 2 == 0)
			{
				num_string = test_num + num_string;
				return evenDigits(n / 10) + num_string;
			} else
			{
				return evenDigits(n / 10);
			}
		}
	}

	// Static method that returns the answer as an int.
	public static int evenDigits2(int n)
	{
		if (n == 0)
		{
			return 0;
		} else
		{
			int test_num = n % 10;
			if (test_num % 2 == 0)
			{
				return test_num + evenDigits2(n / 10) * 10;
			} else
			{
				return evenDigits2(n / 10);
			}
		}
	}
}
