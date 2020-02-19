//Write a method named isVowel that returns whether a String is a vowel 
//(a single-letter string containing a, e, i, o, or u, case-insensitively).


public class Vowel {
	public static void main(String[] args) {

		//String letter = console.nextLine();
	   
		System.out.println(isVowel('A'));
		System.out.println(isVowel('e'));
		String one = "A";

	
	
		
			
	}
	//method that will return the vowel of the character
	public static boolean isVowel(char c) {
		c = Character.toLowerCase(c);

		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
	
	}
}