
public class Gpa {
	public static void main(String[] args) {
		double gpa = 3.2;
		double credits = gpa * 3;
		if (Math.abs (credits - 9.6) < 0.1 ) {
			System.out.println("You earned enough credits");	
		}
		System.out.printf("%.1f \n", credits);
	}
}