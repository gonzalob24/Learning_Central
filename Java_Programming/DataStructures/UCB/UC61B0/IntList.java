package UCB.UC61B0;

public class IntList {
    public int first;
    public IntList rest;

    public IntList(int f, IntList r) {
        this.first = f;
        this.rest = r;
    }

    public int size() {
        if(this.rest == null) {
            return 1;
        }
        return 1 + this.rest.size();
    }

    public int ithIndex(int i) {
        if(i == 0) {
            return first;
        }
        return this.rest.ithIndex(i - 1);
    }
    public static void main(String[] args) {
        IntList L = new IntList(15, null);
        L = new IntList(10, L);
        L = new IntList(5, L);

        System.out.println(L.size());
        System.out.println(L.ithIndex(1));
    }

}
