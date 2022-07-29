package seven.arrays;

public class Student {
    private String name;
    private final int[] marks;
    private int sum;

    // int... variable arguments should go last
    public Student(String name, int... marks) {
        this.name = name;
        this.marks = marks;
        this.setTotalSum();
    }

    public int getNumberOfMarks() {
        return this.marks.length;
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
        return (double) (this.sum / this.marks.length);
    }

    public int getMaximumMark() {
        int max = 0;
        for (int num : this.marks) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

    public int getMinimumMark() {
        int min = 1000;
        for (int num : this.marks) {
            if (num < min) {
                min = num;
            }
        }
        return min;
    }
}
