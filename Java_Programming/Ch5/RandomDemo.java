import java.util.*;

public class RandomDemo {
    public static void main(String[] args) {
        Random r = new Random();
        
        // a random number between 0-9 inclusive
        int randomNum = r.nextInt(10); 
        System.out.println(randomNum);
        
        // a random number between 1-21 inclusive
        randomNum = r.nextInt(21) + 1;
        System.out.println(randomNum);
        
        // a random number between 14-18 inclusive
        randomNum = r.nextInt(5) + 14;
        System.out.println(randomNum);

        // a random even number between 10-16 inclusive
        // 10, 12, 14, 16
        //  0,  1,  2,  3
        //  0   2   4   6
        randomNum = r.nextInt(4) * 2 + 10;
        System.out.println(randomNum);

    }
}