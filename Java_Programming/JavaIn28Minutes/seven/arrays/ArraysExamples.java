package seven.arrays;

import edu.princeton.cs.algs4.In;

import java.util.ArrayList;
import java.util.Arrays;

public class ArraysExamples {
    public static void main(String[] args) {
        int[] nums = {1,2,3,4};
        int sum = 0;
        for(int n : nums) {
            sum += n;
        }
        System.out.println("sum: " + sum);

        int[] marks2 = new int[4];
        marks2[3] = 10;
        System.out.println("marks2: " + Arrays.toString(marks2));
        System.out.println("marks2: " + marks2[3]);

        double[] values = new double[4];
        values[0] = 4;
        System.out.println("values[0]: " + values[0]);

        //
        int[] values2 = {100, 99, 95, 96, 100};
        int[] values3 = {100, 99, 95, 96, 100};
        for (int value: values2) {
            System.out.println(value);
        }

        System.out.println("values 2 and 3 are equal: " + Arrays.equals(values2, values3));
        System.out.println("values 2 and marks2 are equal: " + Arrays.equals(values2, marks2));
        int[] grades = {0, 90, 56, 80};
//        Student student1 = new Student("Alexa", grades);
        // I can also use variable arguments
        Student student1 = new Student("Alexa", 0, 90, 56, 80);
        System.out.println(student1.getNumberOfMarks());
        System.out.println(student1.getTotalSumOfMarks());
        System.out.println(student1.getMaximumMark());
        System.out.println(student1.getMinimumMark());
        System.out.println(student1.getAverageMarks());

        Student[] students = new Student[5];
        Student[] studentsTwo = {new Student("Alison", 1,2,3,4), new Student("ALexa", grades)};

        String[] daysOfTheWeek = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        String longest = "";
        for (String day : daysOfTheWeek) {
            if (day.length() > longest.length()) {
                longest = day;
            }
        }
        System.out.println(longest);

        ArrayList<Integer> aList = new ArrayList<>();
        aList.add(1);
        ArrayList<Integer> aListGrades = new ArrayList<>(Arrays.asList(0, 90, 56, 80));
        StudentArrayList studentAList = new StudentArrayList("ALexa", aListGrades);
        System.out.println("Alist: " + studentAList.getNumberOfMarks());
        System.out.println("Alist: " + studentAList.getTotalSumOfMarks());
        System.out.println("Alist: " + studentAList.getMaximumMark());
        System.out.println("Alist: " + studentAList.getMinimumMark());
        System.out.println("Alist: " + studentAList.getAverageMarks());
        studentAList.addMark(200);
        System.out.println(studentAList.getMaximumMark());
        studentAList.removeMark(200);
        System.out.println(studentAList.getMaximumMark());
    }
}
