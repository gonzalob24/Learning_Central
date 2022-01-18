import java.util.Arrays;

public class ArrayBasics {
    public static void main(String[] args) {
        int[] a1 = new int[3];
        int[] a2 = {1, 2, 3};
        a1[0] = 1;
        a1[1] = 2;
        a1[2] = 3;

        System.out.println(Arrays.toString(a1));
        System.out.println(Arrays.toString(a2));
        System.out.println(a1 == a2);
        System.out.println(Arrays.equals(a1, a2));
    }
}
