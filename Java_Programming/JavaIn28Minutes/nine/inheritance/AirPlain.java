package nine.inheritance;

public class AirPlain implements Flyable {

    @Override
    public void fly() {
        System.out.println("With fuel");
    }
}
