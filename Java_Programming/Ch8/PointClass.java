public class PointClass {
  private int x;
  private int y;

  // another constructor
  public PointClass() {
    this(0,0);
  }

  // PointClass Constructor
  public PointClass(int initialx, int initialy) {
    // x = initialx;
    // y = initialy;
    setLocation(initialx, initialy);
  }

  // add dx and dy to point
  public void translate(int dx, int dy) {
    // this.x += dx;
    // this.y += dy;
    setLocation(x + dx, y + dy);
  }

  // returns distance form origin
  public double distanceFromOrigin() {
    return Math.sqrt(x *x + y * y);
  }

  // Prints point (x, y)
  public String toString() {
    return "(" + x + ", " + y + ")";
  }

  // Get x coord
  public int getX() {
    return this.x;
  }

  // Get y -coord
  public int getY() {
    return this.y;
  }

  // Set new location
  public void setLocation(int newX, int newY) {
    this.x = newX;
    this.y = newY;
  }
}