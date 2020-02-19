public class SLLStackTest
{
    public static void main(String[] args)
    {
        SLLStack<Integer> st1 = new SLLStack();
        st1.push(1);
        st1.push(45);
        st1.push(17);
        st1.push(12);
        st1.push(451);
        st1.push(172);
        st1.display();
        st1.pop();
        st1.display();
    }
}
