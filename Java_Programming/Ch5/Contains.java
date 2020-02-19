//The following code attempts to examine a String and return whether it
//contains a given letter. A flag named found is used.

public class Contains {
	public static void main(String[] args) {
		isLetter("hello", 'l');
	}

	//method that examens a string and checks to see if the given letter
	//is in the string
	public static boolean isLetter(String sentence, char character) {
		boolean foundChar = false;

		for (int i = 0; i < sentence.length(); i++) {
			if (sentence.charAt(i) == character ) {
				foundChar = true;
			}
		}
		return foundChar;
	}
}
