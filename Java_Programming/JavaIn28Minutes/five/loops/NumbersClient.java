package five.loops;

public class NumbersClient {

    public static void main(String[] args) {
        MyNumber number = new MyNumber(5);
        boolean isPrime = number.isPrime();
        System.out.println("IsPrime: " + isPrime);
        System.out.println("sum up to n: " + number.sumUpToN());
        number.printNumberTriangle();
    }


}
