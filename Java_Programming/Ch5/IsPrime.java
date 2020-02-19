//The program attempts to examine a number and return whether that number is
//prime (i.e., has no factors other than 1 and itself). A flag named prime is
//used.

public class IsPrime {
	public static void main (String[] args) {
		System.out.println(isPrime(14));
      System.out.println(isPrime(17));
      System.out.println(isPrime(24));
      System.out.println(isPrime(45));

	}

	//Method that returns true or false if a number is prime or not
	public static boolean isPrime(int n) {
		boolean prime = true;
      for (int i = 2; i < n; i++) {
      	if ( n % i == 0 ) {
            prime = false;
         }      
      }
      return prime;
   }
}
