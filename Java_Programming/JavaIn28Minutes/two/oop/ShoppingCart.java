package two.oop;

import java.util.ArrayList;

public class ShoppingCart {

    ArrayList<String> items = new ArrayList<>();

    public ShoppingCart(ArrayList<String> items) {
        this.items = items;
    }

    public void addItem(String item) {
        this.items.add(item);
    }

    public void removeItem(String item) {
        this.items.remove(item);
    }
}
