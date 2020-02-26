package DataStructures.UCB.Lab2;

import java.util.*;

import edu.princeton.cs.algs4.In;

public class IntListDriver
{
    public static void main(String[] args)
    {
        IntList l = new IntList(1, null);
        l.addToFront(2);
        l.addToFront(3);
        l.addToFront(10);
        System.out.println(l.toString());
        System.out.println(l.size());



    }

    /**
     * Returns an IntList identical to L, but with
     * each element incremented by x. L is not allowed
     * to change.
     */
    public static IntList incrList(IntList L, int x)
    {
        //IntList p = this;
        if (L.rest == null)
        {
            return L;
        }
        return L.rest;
    }

    /**
     * Returns an IntList identical to L, but with
     * each element incremented by x. Not allowed to use
     * the 'new' keyword.
     */
    public static IntList dincrList(IntList L, int x)
    {
        /* Your code here. */
        return L;
    }
}
