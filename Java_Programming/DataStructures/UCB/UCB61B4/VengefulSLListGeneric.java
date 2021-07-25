package UCB.UCB61B4;

import UCB.UC61B3.SLListGeneric;

public class VengefulSLListGeneric<Item> extends SLListGeneric<Item> {
    SLListGeneric<Item> deletedItems;

    public VengefulSLListGeneric() {
        // need to call super
        super();
        deletedItems = new SLListGeneric<Item>();
    }

    public VengefulSLListGeneric(Item x) {
        super(x);
        deletedItems = new SLListGeneric<Item>();
    }

    @Override
    public Item removeLast() {
        // call super class methods with work super
        Item x = super.removeLast();
        deletedItems.addLast(x);
        return x;
    }

    /** Prints deleted items. */
    public void printLostItems() {
        deletedItems.print();
    }


    public static void main(String[] args) {
        VengefulSLListGeneric<Integer> vs1 = new VengefulSLListGeneric<Integer>();
        vs1.addLast(1);
        vs1.addLast(5);
        vs1.addLast(10);
        vs1.addLast(13);
        // vs1 is now: [1, 5, 10, 13]


        vs1.removeLast();
        vs1.removeLast();
        // After deletion, vs1 is: [1, 5]

        // Should print out the numbers of the fallen, namely 10 and 13.
        System.out.print("The fallen are: ");
        vs1.printLostItems();
    }
}
