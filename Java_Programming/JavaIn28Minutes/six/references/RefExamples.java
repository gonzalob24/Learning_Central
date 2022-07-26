package six.references;

import edu.princeton.cs.algs4.In;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class RefExamples {
    public static void main(String[] args) {
        String test = "Test";
        String test2 = new String("Test");
        String test3 = "This is a lot of text in this sentence.";
        System.out.println(test.length());
        System.out.println(test.equals(test2));
        System.out.println(test.charAt(2));
        System.out.println(test3.substring(3, 10)); // start -> inclusive, end -> exclusive

        for(int i = 0; i < test3.length(); i++) {
            System.out.println(test3.charAt(i));
        }

        System.out.println(test3.indexOf("a lot"));
        System.out.println(test3.indexOf("i"));
        System.out.println(test3.lastIndexOf("i"));
        System.out.println(test3.contains("text"));

        System.out.println(test3.concat(" I was added"));
        System.out.println(test + "I was also added " + " me too: " + 23);
        System.out.println(String.join(",", "1", "2", "3"));

        System.out.println(test3.replace("t", "p"));
        System.out.println(test3);

        // "123" + "123" ... costly creating objects
        // String buffer and StringBuilder
        // can get really slow if multithreading
        StringBuffer sb = new StringBuffer("TEst");
        sb.append(" 123");
        System.out.println(sb);
        sb.setCharAt(1, 'e');
        System.out.println(sb);

        // string buffer is similar but offered in later versions of JAVA
        // does not worry about multi threading
        StringBuilder sb2 = new StringBuilder("test");

        // wrapper classes
        Integer integer1 = new Integer(5);
        Integer integer2 = new Integer(5);
        // or

        // these do not create new objects every time the above do
        Integer integer3 = Integer.valueOf(5);
        Integer integer4 = Integer.valueOf(5);
        Integer integer5 = Integer.valueOf("6");

        // auto boxing
        Integer integer6 = Integer.valueOf(7);
        // syntactic sugar coating
        Integer integer7 = 7; // this is called autoboxing and user Integer.valueOf()


        // TIME
        LocalDateTime now = LocalDateTime.now();
        LocalDate now1 = LocalDate.now();
        LocalTime now2 = LocalTime.now();
        System.out.println(now);
        System.out.println(now1);
        System.out.println(now2);
        System.out.println(now1.isLeapYear());
        System.out.println(now1.minusYears(20));
    }
}
