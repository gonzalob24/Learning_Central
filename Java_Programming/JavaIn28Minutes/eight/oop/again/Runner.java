package eight.oop.again;

public class Runner {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(3, 4);
        System.out.println(rect);
        System.out.println(rect.getArea());

        // Customer
        Customer cust = new Customer("Alexa",
                new Address("1939 Jonathan CIR",
                "Shelby Township", "48317"));
        System.out.println(cust);
    }
}
