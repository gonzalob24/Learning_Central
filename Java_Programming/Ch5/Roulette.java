// This program simulates making bets at a Roulette table (betting that the
// number comes up "low" in the range of 1 to 18).

import java.util.*;

public class Roulette {
    public static void main(String[] args) {
        Random r = new Random();
        int money = 10;
        int max = money;
        while (money > 0) {
            int bet = 3;
            if (money < bet) {
                bet = money;
            }
            // instead of the assignment and if statement, we could have said:
            // int bet = Math.min(3, money);

            // this gives us 0 through 36--it doesn't include the 00 that
            // is used in American Roulette
            int spin = r.nextInt(37);

            // without the spin != 0 test, we were playing as the casino
            // and sometimes made lots of money
            if (spin != 0 && spin <= 18) {
                money = money + bet;
            } else {
                money = money - bet;
            }

            // update max
            if (money > max) {
                max = money;
            }
            System.out.println("betting $" + bet + ", spin is " + spin
                             + ", money now = $" + money);
        }
        System.out.println("max = $" + max);
    }
}
