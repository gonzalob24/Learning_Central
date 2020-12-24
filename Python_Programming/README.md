# Python

This folder has problems from various books I have read. Like How to Think like a Computer Scientist and Data Structures and Algorithms.

I may not do all of the problems from each chapter since a lot of it is just for review.

## Time Complexity

    - Time
    - Space
    - BigO
        - Compare two functions f(n) and g(n) for very large values of n.
        - f(n) is O(g(n)) is there exists some positive real constant c and integer n_0 >= 0 for all n >= n_0: f(n) <= cg(n)

## Lists (Python Arrays are faster)

    - copy.copy(A) vs copy.deepcopy(A): Use import copy
        - Relevant for compund objects
    - I can also use slicing to copy arrays
    - think about storing elements in a stack or queue for temporary storage
    - Once I have a brute force solution. Look into time complexity and determine why it is slow. what is impacting its performance. Time/Space complexity.

## Linked Lists

    - Why is the head used? To keeep track of the list. It points to the beginning of the list
    - When a list is created head = None
    - Similar to Lists except in the way items are inserted and deleted.
    -

## Trees

    - understand tree traversal: Inorder, Preorder, Postorder, Level Order
    - Recursion makes it easier to travers trees.
    - Try to use helper functions to make traversal easier
    -

## Recursion

    - Use when:

        - problem breaks down into smaller similar subproblems
        - Graphs, trees, permutations, combinations

    - List out different test cases
    - Think about the stack and the order in which items are removed from the stack

    - Find base case: There can be more than one base case
    - Find recursive case

    - Time complexity:

    - Space complexity

    - Working with arrays or strings:

        - Create a helper function and maintain a reference to the index of the array. This avoids copying the array and reduces time complexity.

## Greedy

    - Choose the next piece that offers most obvious and immediate benefit.
    - Works great for problems where choosing a locally optimall solution also leads to the optimal solution
    - Think about it in terms of layers of a brick wall (local solution) --> after many layers we get a wall (optimal solution)

## Dynamic Prgramming

    - Try to viualize the problem in a tree structure.
    - Think about what goes inside each node
    - What are my branch factors. How do I get from one node to the next
    - The leafs will be my base cases.

## Collections

    - Math
    - max, sum can be used on array
    - name.count(char) --> counts cahracters in a string
    - collections.count(object) --> create dictionary very easily
    - Use deque
        - rotate() method
    - sorted(array_name) --> nlog(n)

## Hashing

    - dict
        - Can't have duplicate keys but can have duplciate values
        - no order
    - set
        - no duplcates
        - name.add(item)
        - name.remove(item)
        - name1 - name2 --> difference
        - name1 & name2 --> intersection
        - key in name:
         (a, b) and (c, d) are symmetric pairs iff, a = d and b = c
