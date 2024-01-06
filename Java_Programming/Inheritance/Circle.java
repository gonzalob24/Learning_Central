public class Circle implements Shape {

    private Double r;
    private final Double pi = Math.PI;
    public Circle(Double r) {
        this.r = r;
    }
    @Override
    public double getArea() {
        // pi * r ** 2
        return this.pi * Math.pow(this.r, 2);
    }

    @Override
    public double getPerimeter() {
        return 2 * this.pi * r;
    }
}
