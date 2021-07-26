package UCB.UCB61B4;

import java.util.Comparator;

public class CompareDogsMain {

//    public static MyComparable max(MyComparable[] items){
//    public static Comparable max(Comparable[] items){
//        int maxDex = 0;
//        for (int i = 0; i < items.length; i += 1) {
//            int cmp = items[i].compareTo(items[maxDex]);
//            if (cmp > 0) {
//                maxDex = i;                 }}
//        return items[maxDex];
//    }
    public static void main(String[] args) {
//        Dog[] dogs = {new Dog("Elyse", 3), new Dog("Sture", 9),
//                new Dog("Benjamin", 15)};
//        Dog maxDog = (Dog) Maximizer.max(dogs);
//        maxDog.bark();
        Dog d1 = new Dog("Elyse", 3);
        Dog d2 = new Dog("Sture", 9);
        Dog d3 = new Dog("Benjamin", 15);
        Dog[] dogs = new Dog[]{d1, d2, d3};
        Dog d = (Dog) Maximizer.max(dogs);
        d.bark();
        Comparator<Dog> nc = Dog.getNameComparator();
        if(nc.compare(d1, d3) > 0) {
            d1.bark();
        } else {
            d3.bark();
        }
    }

}
