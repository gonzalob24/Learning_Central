package ten.collections;

import java.util.*;

class DescendingStudentComparator implements Comparator<Student> {

    @Override
    public int compare(Student o1, Student o2) {
        return Integer.compare(o2.getId(), o1.getId());
    }
}

class StringLengthComparator implements Comparator<String> {

    @Override
    public int compare(String o1, String o2) {
        return Integer.compare(o1.length(), o2.length());
    }
}

public class MainRunner {

    public static void main(String[] args) {
        // List --> immutable
        List<String> words = List.of("Apple", "Bat", "Cat");
        System.out.println(words);
        System.out.println(words.size());
        System.out.println(words.contains("me"));

        // words is immutable --> will need to create ArrayList or
        // words.add("Hello");

        // These are not immutable
        List<String> wordsArrayList = new ArrayList<>(words);
        List<String> newList = List.of("Yak", "Zebra");
        wordsArrayList.add("Gonzalo");
        wordsArrayList.add(2, "Ball");
        wordsArrayList.addAll(newList);
        System.out.println(wordsArrayList);
        wordsArrayList.set(2, "Fish");
        System.out.println(wordsArrayList);
        // can remove by index or item name
        wordsArrayList.remove(5);
        wordsArrayList.remove("Gonzalo");
        System.out.println(wordsArrayList);
        Collections.sort(wordsArrayList);
        System.out.println(wordsArrayList);

        for (String item: wordsArrayList) {
            System.out.println(item);
        }

        List<String> wordsLinkedList = new LinkedList<>(words);
        wordsLinkedList.add("Alexa");

        List<String> wordsVectorList = new Vector<>(words);
        wordsVectorList.add("Alison");

        // Which one do I use:
        // DS --> Array is used for ArrayList and Vector
            // adding and deleting values can be time-consuming
            // insertion and deletion are costly
            // accessing is very fast - almost constant time
        // DS --> LinkedList elements are doubly linked
            // reference elements with a pointer
            // inserting and deleting is faster
            // accessing is more costly
        // Vector --> Thread Safe
            // almost constant access time
            // can get costly

        // Students example
        List<Student> students = List.of(
                new Student("Alexa", 110),
                new Student("Alison", 109),
                new Student("AAA", 102));
        System.out.println(students);

        List<Student> studentsAL = new ArrayList<>(students);

        // this sort can only be used with classes that implement the comparable interface
//        System.out.println(studentsAL);
        Collections.sort(studentsAL);
        System.out.println("Asc: " + studentsAL);
        // I can also pass in the comparator to studentsAL to sort items in the Array List
        studentsAL.sort(new DescendingStudentComparator());
        Collections.sort(studentsAL, new DescendingStudentComparator());
        System.out.println("Descending: " + studentsAL);

        // set: it does not care about the position
        Set<String> set = Set.of("Apple", "Bannana", "Cat");
        System.out.println(set);
//        set.add("Bannana");

        Set<String> hashSet = new HashSet<>(set);
        hashSet.add("Apple");
        System.out.println(hashSet);

        // not stored in insertion order
        // Set<Integer> numbers = new HashSet<>();

        // stored in order in which I insert them
        // Set<Integer> numbers = new LinkedHashSet<>();

        // Tree set inserts in sorted order, does not add duplicate values as well
        Set<Integer> numbers = new TreeSet<>();
        numbers.add(765432);
        numbers.add(76543);
        numbers.add(7654);
        numbers.add(765);
        numbers.add(76);
        System.out.println(numbers);

        List<Character> characters = List.of('A', 'Z', 'A', 'B', 'Z', 'F');
        // find the unique characters in sorted order
        Set<Character> sortedChars = new TreeSet<>(characters);
        System.out.println(sortedChars);

        // Queues -> insert in natural order
        Queue<String> queue = new PriorityQueue<>(new StringLengthComparator());
        queue.offer("Apple");
        queue.addAll(List.of("Cat", "Orange", "Bear"));
        queue.offer("Appl");
        System.out.println(queue);
    }
}
