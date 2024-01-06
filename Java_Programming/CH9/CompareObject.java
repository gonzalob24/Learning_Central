import java.awt.*;

public class CompareObject {

    private Object o1;
    private Object o2;

    // java will not know that these are Point objects so I will need to cast them into point objects
    public CompareObject(Object o1, Object o2) {
        this.o1 = o1;
        this.o2 = o2;
    }

    public boolean equals() {
        Point p1 = (Point) this.o1;
        Point p2 = (Point) this.o2;
        return p1.getX() ==p2.getX() && p1.getY() == p2.getY();
    }
}
