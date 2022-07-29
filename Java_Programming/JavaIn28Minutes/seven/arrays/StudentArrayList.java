package seven.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class StudentArrayList {
    private String name;
    private final ArrayList<Integer> marks;
    private int sum;

    // int... variable arguments should go last
    public StudentArrayList(String name, ArrayList<Integer> marks) {
        this.name = name;
        this.marks = marks;
        this.setTotalSum();
    }

    public int getNumberOfMarks() {
        return this.marks.size();
    }

    public int getTotalSumOfMarks() {
        return this.sum;
    }

    private void setTotalSum() {
        for (int num : this.marks) {
            this.sum += num;
        }
    }

    public double getAverageMarks() {
        return (double) (this.sum / this.marks.size());
    }

    public int getMaximumMark() {
        int max = 0;
        for (int num : this.marks) {
            if (num > max) {
                max = num;
            }
        }
        return Collections.max(this.marks);
    }

    public int getMinimumMark() {
        int min = 1000;
        for (int num : this.marks) {
            if (num < min) {
                min = num;
            }
        }
        return Collections.min(this.marks);
    }

    public void addMark(int mark) {
        this.marks.add(mark);
    }

    public void removeMark(Integer mark) {
        this.marks.remove(mark);
    }
}
