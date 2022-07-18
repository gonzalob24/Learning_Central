package One.Intro;

public class Methods {
    public static void main(String[] args) {
        hey();
        System.out.println(sumOfThree(5,5,5));
        System.out.println(findOtherAngle(30, 42));
    }

    public static void hey() {
        System.out.println("Why oh why..");
    }

    public static int sumOfThree(int a, int b, int c) {
        return a + b + c;
    }

    public static int findOtherAngle(int a1, int a2) {
        return 180 - a1 - a2;
    }
}
