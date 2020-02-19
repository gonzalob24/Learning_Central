public class SLLTest
{
    public static void main(String[] args)
    {
        SLList<Integer> list1 = new SLList();
        list1.addFront(1);
        list1.addFront(12);
        list1.addLast(57);
        list1.addFront(13);
        list1.addFront(787);
        list1.addLast(5009);
        list1.removeFirst();
        list1.insert(44, 3);
        list1.display();

    }
}
