// Examples of char type and usage
public class CharExamples {
   public static void main(String[] args) {
      String word = "computer";
      
      // Print each letter on their own line
      for (int i = 0; i < word.length(); i++) {
         char c = word.charAt(i);
         System.out.println(c);
      } 
      System.out.println();
      
      System.out.println(doubleLetters(word));
   }
   
   // Takes a String word and returns the word with each letter
   // repeated twice.
   public static String doubleLetters(String word) {
      // NOTE: Example of a cumulative algorithm!
      String result = "";
      for (int i = 0; i < word.length(); i++) {
         result = result + word.charAt(i) + word.charAt(i);
      }
      return result;
   }
}