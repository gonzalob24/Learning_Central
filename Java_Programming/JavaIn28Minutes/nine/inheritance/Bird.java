package nine.inheritance;

public class Bird implements Flyable {

    @Override
    public void fly() {
        System.out.println("With wings");
    }
}
