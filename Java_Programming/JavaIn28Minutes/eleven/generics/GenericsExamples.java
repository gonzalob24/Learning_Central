package eleven.generics;

import java.util.ArrayList;
import java.util.List;

public class GenericsExamples {
    // upper bound wildcard
    static double sumOfNumberList(List<? extends Number> numbers){
        double sum = 0.0;
        for(Number number : numbers) {
            sum += number.doubleValue();
        }
        return sum;
    }

    static void addValues(List<? super Number> numbers){
        numbers.add(1);
        numbers.add(1.0);
        numbers.add(1.0f);
        numbers.add(1L);
    }
    public static void main(String[] args) {
        MyCustomList<String> list  = new MyCustomList();

        list.addElement("Element 1");
        list.addElement("Element 2");

        // right now I cant use it because my implementation only supports String
        // need to create a class that is Generic not single type
        MyCustomList<Integer> list2 = new MyCustomList();
        list2.addElement(1);
        list2.addElement(2);

        System.out.println(list.get(1));
        System.out.println(list2.get(0));

        System.out.println(sumOfNumberList(List.of(1,2,3,4,5)));
        System.out.println(sumOfNumberList(List.of(1.2,2.2,3.2,4.2)));
        List<Number> empty = new ArrayList<>();
        addValues(empty);
        System.out.println(empty);


    }
}
