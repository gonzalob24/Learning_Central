public interface ListInterface<T>
{
    /**
    * Inserts items at the front of the list
    */
    void addFront(T value);

    /**
    * removes and returns the first item of the list
    */
    T removeFirst();

    /**
    * Inserts items at the back of the list
    */
    void addLast(T value);

    /**
    * Inserts an item at the ith position
    */
    void insert(T value, int position);

    /**
    * Display the items of the list
    */
    void display();


}
