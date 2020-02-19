package UCB.Project1;

public class SLListStackTest
{
    public static void main(String[] args)
    {
        SLListStack<Integer> stack1 = new SLListStack<>();
        stack1.push(3);
        stack1.push(4);
        stack1.push(5);
        stack1.push(22);
        stack1.push(17);
        stack1.display();
        int popped_item = stack1.pop();
        System.out.println("After popping : " + popped_item);
        stack1.display();
    }
}
