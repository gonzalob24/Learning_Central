package two.oop;

public class ClassesClient {

    public static void main(String[] args) {
        Country mexico = new Country();
        Planet earth = new Planet();
        System.out.println(mexico);
        System.out.println(earth);
        mexico.comingSoon();

        earth.revolve();

        // Motor bike
        MotorBike ducati = new MotorBike(90);
        MotorBike honda = new MotorBike(120);
        System.out.println(ducati.getSpeed());
        ducati.increaseSpeed(30);
        System.out.println(ducati.getSpeed());
        ducati.start();

        // Book class
        Book artOfProgramming = new Book(200);
    }
}
