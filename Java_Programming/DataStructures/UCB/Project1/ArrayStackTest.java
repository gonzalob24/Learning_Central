package UCB.Project1;

public class ArrayStackTest
{
    public static void main(String[] args)
    {
        ArrayStack<Integer> stack1 = new ArrayStack<>();

        stack1.push(2);
        stack1.push(33);
        stack1.push(43);
        stack1.push(99);
        stack1.push(11);
        stack1.push(123);
        stack1.display();
        System.out.println("The size is: " + stack1.size());

        stack1.pop();
        stack1.display();
        System.out.println("The size is: " + stack1.size());
    }
}
