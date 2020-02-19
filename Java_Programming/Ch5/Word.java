//Program that will give the first word of the string

public class Word {
	public static void main(String[] args) {
		System.out.println(firstWord("The Lakers."));
	}

	//static method that takes in a string and returns the first word of the string
	public static String firstWord(String s) {
		int start = 0;
		while ( start < s.length() && s.charAt(start) == ' ' ) {
			start++;
		}

		int stop = start;
		while(stop < s.length() && s.charAt(stop) != ' ') {
			stop++;
		}

		return s.substring(start, stop);
	}
}