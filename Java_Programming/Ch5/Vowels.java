public class Vowels {
	public static void main(String[] args) {

		//isAllVowels();
		String vowels = "aeiouAEIOUn";
		String test = "neeiou";

       	for ( int i = 0; i < test.length(); i++) {
       		int index = test.charAt(i);
       		System.out.println( vowels.indexOf(index) );
       }
   }
}