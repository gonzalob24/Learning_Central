package nine.inheritance;

public class MainRunner {

    public static void main(String[] args) {
        Student student = new Student();
        student.setName("Alexa");
        student.setEmail("test@me.com");
        System.out.println(student.getEmail());
        System.out.println(student instanceof Person);
    }
}
