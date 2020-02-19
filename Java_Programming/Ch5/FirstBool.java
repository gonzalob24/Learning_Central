///Program that will return a boolean expression

public class FirstBool {
	public static void main(String[] args) {
		System.out.println(isTwoUniqueDigits(29));	
	}

	//static method that will return a boolean value
	public static boolean isTwoUniqueDigits(int n) {
		return ( n >= 10 && n <= 99 && (n % 10 != n / 10) );
	}
}

