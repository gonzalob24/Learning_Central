import java.awt.*;

public class Main {
    public static void main(String[] args) {

        StockTest stock1 = new StockTest("AMZN");
        System.out.println(stock1.getMarketValue());

        Point p1 = new Point(1,2);
        Point p2 = new Point(1,2);
        CompareObject compare = new CompareObject(p1, p2);
        System.out.println(compare.equals());
        System.out.println(p2 instanceof Point);
    }

//    Polymorphism
    /**
     * The reference variable does need to exactly math the type of object it refers to
     *
     * when a subclass is stored in s superclass variable.
     * Employee one = new Lawyer() --> the object referred by one is a Lawyer not an Employee object
     * no conversion is taking place
     *
     * We can create many Types of Employees and each type will behave differently because they override the
     * behavior of the Employee methods.
     *
     * UML Diagrams -> Show fields and methods
     *
     * A A 1 A 2
     * A A 1 B 2
     * C C 1 A 2
     * C C 1 D 2
     *
     *
     */


}
