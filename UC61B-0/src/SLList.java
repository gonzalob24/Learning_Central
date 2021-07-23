/** Singly linked list*/
public class SLList {
    // make variables private to hide implementation details, encapsulation
    private IntNode first;
    private IntNode sentinal;
    private int sizeOfList;

//    public IntNode first;


    public SLList() {
        this.sentinal = new IntNode(999, null);
        this.sizeOfList = 0;
//        this.first = null;
    }

    public SLList(int x) {
//        this.first = new IntNode(x, null);
        this.sentinal = new IntNode(63, null);
        this.sentinal.next = new IntNode(x, null);
        this.sizeOfList+=1;
    }
    // add to the front
    public void addFirst(int x) {
//        this.first = new IntNode(x, this.first);
        this.sentinal.next = new IntNode(x, this.sentinal.next);
        this.sizeOfList+=1;
    }
    // get first element
    public int getFirst() {
//        return this.first.item;
        return this.sentinal.next.item;
    }

    // add to the end of the list
    public void addLast(int x) {
//        IntNode p = this.first;
//        while(p.next != null) {
//            p = p.next;
//        }
//        p.next = new IntNode(x, null);
        IntNode p = this.sentinal;
        while(p.next != null) {
            p = p.next;
        }
        p.next = new IntNode(x, null);

        this.sizeOfList+=1;
    }

    // print the list
    public void printList() {
        IntNode p = this.sentinal.next;
        while(p != null) {
            System.out.print(p.item + " >> ");
            p = p.next;
        }
    }

    // get size
    public int size() {
        IntNode p = this.sentinal;
        int total = 0;

        while(p != null) {
            total+=1;
            p = p.next;
        }
        return total;
    }

    public int recursiveSize() {
        return this.recurSizeHelp(this.sentinal.next);
    }

    private static int recurSizeHelp(IntNode x) {
        if(x.next == null) {
            return 1;
        }
        return 1 + recurSizeHelp(x.next);
    }

    // get size of list
    public int getSizeOfList() {
        return this.sizeOfList;
    }

    public static void main(String[] args) {

//        SLList L = new SLList(15);
        SLList L = new SLList();
        L.addFirst(10);
        L.addFirst(51);
//        L.first.next.next = L.first.next;
        L.addLast(20);
        System.out.println(L.getFirst());
        L.printList();
        System.out.println("\n" + L.size());
        System.out.println("Cached size: " + L.getSizeOfList());
        System.out.println("\nRecursive size: " + L.recursiveSize());
    }
}
