package eight.oop.again;

public class Rectangle {

    private int length;
    private int width;

    public Rectangle(int length, int width) {
        this.length = length;
        this.width = width;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getArea() {
        return this.width * this.length;
    }

    public int getPerimeter() {
        return 2 * (this.width + this.length);
    }

    @Override
    public String toString() {
        return "Rectangle {" +
                "length= " + length +
                ", width= " + width +
                '}';
    }
}
