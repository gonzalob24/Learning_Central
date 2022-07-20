package two.oop;

public class MotorBike {
    // state -> instance variable
    // will be public if I don't make it private
    private int speed;

    public MotorBike(int speed) {
        this.speed = speed;
    }

    // behavior
    public void start() {
        System.out.println("Engine start!");
    }

    public int getSpeed() {
        return this.speed;
    }

    public void setSpeed(int speed) {
        if (speed >= 0) {
            this.speed = speed;
        }
    }

    public void increaseSpeed(int speed) {
        this.speed += speed;
    }

    public void decreaseSpeed(int howMuch) {
        this.setSpeed(this.speed - howMuch);
    }
}
