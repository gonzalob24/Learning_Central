class TreeNode:

    def __init__(self, info, lchild=None, rchild=None):
        self.info = info
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # using recursion to insert items into a binary search tree
    def add(self, value):
        self.root = self._add(self.root, value)

    def _add(self, pNode, value):
        if pNode is None:
            pNode = TreeNode(value)
        elif value <= pNode.info:
            pNode.lchild = self._add(pNode.lchild, value)
        else:
            pNode.rchild = self._add(pNode.rchild, value)

        return pNode

    def display(self):
        self._display(self.root, 0)
        print()

    def _display(self, pNode, level):
        # Base case
        if pNode is None:
            return

        self._display(pNode.rchild, level + 1)
        # insert the correct number of spaces
        for i in range(level):
            print("   ", end="")
        print(pNode.info)

        # Call the left side
        self._display(pNode.lchild, level + 1)

    def height(self):
        return self._height(self.root)

    def _height(self, pNode):
        if pNode is None:
            return 0
        height_left = self._height(pNode.lchild)
        print("Height is ", height_left, " ", pNode.info)
        height_right = self._height(pNode.rchild)

        if height_left > height_right:
            return 1 + height_left
        else:
            return 1 + height_right

    def search(self, value):
        return self._search(self.root, value) is not None

    def _search(self, pNode, value):
        if pNode is None:
            return
        elif value < pNode.info:
            return self._search(pNode.lchild, value)
        elif value > pNode.info:
            return self._search(pNode.rchild, value)
        else:
            return pNode

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, pNode):
        if pNode is None:
            return
        print(pNode.info, end=" ")
        self._preorder(pNode.lchild)
        self._preorder((pNode.rchild))

    def preorder_iterative(self):
        """
        running time is O(n)
        when using iteration I need to use a stack.
        """
        # create and append root node to stack
        treeStack = []
        treeStack.append(self.root)

        while len(treeStack) > 0:
            # First pop item from the stack and print it
            popped_node = treeStack.pop()
            print(popped_node.info, end=" ")

            # push right and left child nodes of popped node
            if popped_node.rchild is not None:
                treeStack.append(popped_node.rchild)
            if popped_node.lchild is not None:
                treeStack.append(popped_node.lchild)

    def lowest_common_ancestor(self, num1, num2):
        """
        find the lowest common ancestor for a BST
        """
        pNode = self.root

        while pNode is not None:
            if pNode.info > num1 and pNode.info > num2:
                pNode = pNode.lchild
            elif pNode.info < num1 and pNode.info < num2:
                pNode = pNode.rchild
            else:
                return pNode.info

if __name__ == "__main__":
    bt1 = BinaryTree()
    bt1.add(20)
    bt1.add(22)
    bt1.add(8)
    bt1.add(4)
    bt1.add(12)
    bt1.add(10)
    bt1.add(14)
    # bt1.add(77)
    # bt1.add(40)
    # bt1.add(39)
    # bt1.add(52)
    # bt1.add(51)
    # bt1.add(38)
    bt1.display()
    bt1.preorder()
    print()
    bt1.preorder_iterative()
    print()
    print(bt1.lowest_common_ancestor(10, 14))
