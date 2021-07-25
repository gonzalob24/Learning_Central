package UCB.UCB61B4;

import UCB.UC61B3.SLListGeneric;

public class RotatingSLList<Item> extends SLListGeneric<Item> {

    /** To do: Implement RotatingSLList such that code compiles and outputs correct result. */

    /** Rotates list to the right. */
    public void rotateRight() {
        Item x = removeLast();
        addFirst(x);
    }

    public static void main(String[] args) {
        RotatingSLList<Integer> rs1 = new RotatingSLList<>();
        rs1.addLast(10);
        rs1.addLast(11);
        rs1.addLast(12);
        rs1.addLast(12);

//        rs1.rotateRight();
        rs1.print();
    }
}
