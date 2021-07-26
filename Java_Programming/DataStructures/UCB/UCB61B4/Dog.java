package UCB.UCB61B4;

import javax.naming.Name;
import java.util.Comparator;

//public class Dog implements MyComparable{
public class Dog implements Comparable<Dog>{
    private String name;
    private int size;

    public Dog(String name, int size) {
        this.name = name;
        this.size = size;
    }

    public void bark() {
        System.out.println(this.name + "says: Bark!");
    }

    // removed Object from params
    @Override
    public int compareTo(Dog uddaDog) {
        // there is no o.size in Object
//        Dog uddaDog = (Dog) o;
        if(this.size < uddaDog.size) {
            return -1;
        } else if (this.size == uddaDog.size) {
            return 0;
        }
        return 1;
    }

    private static class NameComparator implements Comparator<Dog> {

        @Override
        public int compare(Dog a, Dog b) {
            return a.name.compareTo(b.name);
        }
    }

    public static Comparator<Dog> getNameComparator() {
        return new NameComparator();
    }
}
