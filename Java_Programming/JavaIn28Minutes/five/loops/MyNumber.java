package five.loops;

public class MyNumber {

    int num;
    public MyNumber(int num) {
        this.num = num;
    }

    public boolean isPrime() {
        for (int i = 2; i < this.num; i++) {
            if (this.num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int sumUpToN() {
        int sum = 0;
        for (int i = 1; i <= this.num; i++) {
            sum += i;
        }
        return sum;
    }

    public void printNumberTriangle() {
        for (int i = 1; i <= this.num; i++) {
            for (int nums = 1; nums <= i; nums++) {
                System.out.print(nums + " ");
            }
            System.out.println();
        }
    }

    public void printSquaresUptoLimit() {

    }

    public void printCubesUptoLimit() {

    }


}
