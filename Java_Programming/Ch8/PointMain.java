public class PointMain {
  public static void main(String[] args) {
    // PointClass p1 = new PointClass();
    PointClass p1 = new PointClass(7,2);
    // p1.x = 7;
    // p1.y = 2;
    System.out.println(p1.getX());

    p1.translate(1,2);
    System.out.printf("(%d, %d)\n", p1.getX(), p1.getY());
    System.out.printf("P1 Distance from origin: %f\n", p1.distanceFromOrigin());
    // compiler automatically calls toString()
    System.out.println(p1);
  }
}