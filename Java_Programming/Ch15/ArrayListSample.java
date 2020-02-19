// This class includes sample client code for manipulating a list.
//
// translation from array to ArrayList:
//    String[]          => ArrayList<String>
//    new String[10]    => new ArrayList<String>()
//    a.length          => list.size()
//    a[i]              => list.get(i)
//    a[i] = value;     => list.set(i, value);
// new operations:
//     list.remove(i);     --remove the ith value
//     list.add(value);    --appends a value
//     list.add(i, value); --adds at an index
//     list.clear()        --remove all value

import java.util.*;

public class ArrayListSample
{
    public static void main(String[] args)
    {
        List<String> list = new ArrayList<String>();
        list.add("four");
        list.add("score");
        list.add("seven");
        list.add("years");
        list.add("what was next?");
        list.add("ago");
        list.add(2, "and");
        list.remove(5);
        System.out.println("list = " + list);
        System.out.println(list.indexOf("seven"));
    }
}
