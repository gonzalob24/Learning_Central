package UCB.Project1;

public class SLListStack<Any>
{
    /**
     * I will implement the Single Linked List stack with out a header node.
     * since popping and pushing will only be done from the front of the list
     * The front of the list will be my top.
     */

    private SLListNode<Any> stack;
    private int size;

    /**
     * constructor to create a SLListStack
     */
    public SLListStack()
    {
        stack = new SLListNode(null, null);
        size = 0;
    }

    /**
     * return the size of the stacl
     */
    public int size()
    {
        return size;
    }

    /**
     * push an item to the stack
     */
    public void push(Any x)
    {
        stack.next = new SLListNode(x, stack.next);
        size++;
    }

    /**
     * pops and return the top item from the stack check if the stack is empty
     */
    public Any pop()
    {
        Any topOfStack = stack.next.item;
        stack.next = stack.next.next;
        size--;
        return topOfStack;
    }

    /**
     * return the top element from the stack check if stack is empty
     */
    public Any peek()
    {
        return stack.next.item;
    }

    /**
     * display the contents of the SLListStack
     */
    public void display()
    {
        SLListNode p = stack.next;

        while (p != null)
        {
            System.out.println(p.item + " ");
            p = p.next;
        }
    }

    /**
     * check if the stack is empty return true or false
     */
    public boolean isEmpty()
    {
        return size == 0;
    }

}
