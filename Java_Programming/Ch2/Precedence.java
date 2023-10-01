public class Precedence {
    public static void main(String[] args) {
        System.out.println(2*-8);
        int x = 10;
//        int x = 2;
        int y = 20;
        int z;
//        System.out.println(x);
//        System.out.println("give me x and then increment: " + x++);
//        System.out.println("increment and then give me x: " + ++x);
        z = ++x * y--;
        System.out.println("increment x abd then return * give me y and then decrement (11 * 20): " + z);
    }

}
