package nine.inheritance;

public class MainRunner {

    public static void main(String[] args) {
        Student student = new Student("Mary");
        student.setName("Alexa");
        student.setEmail("test@me.com");
        System.out.println(student.getEmail());
        System.out.println(student instanceof Person);

        // Object is at top of inheritance
        // every class extends the Object class by default they don't extend anything,
        // it is the root of the class hierarchy
        Person person = new Person("Alison");
        person.setEmail("alexa@gmail.com");
        System.out.println(person);

        // Polymorphism: being able to create different types of objects with the same code
        // and behave differently depending on the type of object used.
        Person stu = new Student("Alison");
    }
}
