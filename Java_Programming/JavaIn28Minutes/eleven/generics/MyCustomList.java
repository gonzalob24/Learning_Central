package eleven.generics;

import java.util.ArrayList;

// If i want to use this generics class only with numbers ad this
// MyCustomList<T extends Number>
// this restricts the classes that can be used
public class MyCustomList<T>{

    ArrayList<T> list = new ArrayList<>();

    public void addElement(T element) {
        list.add(element);
    }

    public void removeElement(T element) {
        list.remove(element);
    }

    public T get(int index) {
        return list.get(index);
    }

    @Override
    public String toString() {
        return "MyCustomList{" +
                "list=" + list +
                '}';
    }
}
