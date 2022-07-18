package One.Intro;

import java.util.ArrayList;
import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] a1 = new int[3];
        a1[0] = 2;
        a1[1] = 3;
        a1[2] = 4;

        for (int i = 0; i < a1.length; i++) {
            System.out.println("a1: " + a1[i]);
        }
        System.out.println("-------------------");
        int[] a2 = {1,5,3,4};

        for(int a : a2) {
            System.out.println("a2: " + a);
        }

        System.out.println(Arrays.toString(a2));
        Arrays.sort(a2);
        System.out.println(Arrays.toString(a2));
    }
}
