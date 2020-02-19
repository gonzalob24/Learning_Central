//Guessing game that will ask the user to input a digit from
//1-100 until the user gets it right.
//define a class constant to define the max number used in the game
//report the total number of games played
//the total number of guesses made
//the average number of guesses per game
//fewest number of guesses used in any single game


import java.util.*;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        Random rand = new Random();
        intro();
        String play = "y";
        int games = 0;
        int totalGuesses = 0;
        int bestGuess = 100000;
        int gameGuess = 0;
        
        while ( !play.equals("no") ) {
            gameGuess = playGame(console, rand);
            totalGuesses += gameGuess;
            
            if ( gameGuess < bestGuess ) {
                bestGuess = gameGuess;
            }
            
            games++;
            
            System.out.println("Do you want to play again? ");
            play = console.next();
            
            if ( play.toLowerCase().charAt(0) == 'n' ) {
                play = "no";
            }
            
        }
        gameStats(bestGuess, games, totalGuesses);
        
    }
    //introduction the the game
    public static void intro() {
        System.out.println("This program allows you to play a guessing game.");
        System.out.println("I will think of a number between 1 and");
        System.out.println("100 and will allow you to guess until");
        System.out.println("you get it. For each guess, I will tell you");
        System.out.println("whether the right answer is higher or lower");
        System.out.println("than your guess.\n");
    }
    
    //this method will get the integer value from the user and test if it is an int or not
    public static int getInt(Scanner console) {
        while ( !console.hasNextInt() ) {
            console.next();   //this discards the input
            System.out.println("Not an integer.");
            System.out.print("Your guess? ");
        }
        
        return console.nextInt();
    }
    
    //Method that will test if the guess from the user is in range
    public static int getGuess(Scanner console) {
        
        int guess = getInt(console);
        
        while (guess < 0 || guess > 100) {
            System.out.println("Out of range please try again: ");
            System.out.print("Your guess? ");
            guess = getInt(console);
        }
        
        return guess;
    }
    
    //Plays a single game with the user
    public static int playGame(Scanner console, Random rand) {
        System.out.println("I am thinking of a number between 1 and 100: ");
        System.out.print("Your guess? ");
        
        int randomGuess = rand.nextInt(100) + 1;
        int playerGuess = getGuess(console);
        int guessCount = 1;
        
        while ( playerGuess != randomGuess ) {
            
            if ( playerGuess > randomGuess ) { // //numGuess is greater than guess
                System.out.println("It's lower.");
                
            } else {
                System.out.println("It's higher. ");
                
            }
            System.out.print("Your guess? ");
            playerGuess = getGuess(console);
            guessCount++;
        }
        System.out.println("You got it right in " + guessCount + " guesses");
        
        return guessCount;
    }
    
    //reports the results of the game
    public static void gameStats(int bestGuess, int games, int totalGuesses) {
        System.out.println("Overall results");
        System.out.println(" total games = " + games);
        System.out.println(" total guesses = " + totalGuesses);
        System.out.printf(" guesses per game = %2d \n", (totalGuesses/games) );
        System.out.println(" best game = " + bestGuess);
    }
    
}