# First Binary tree program will update comments and code later

from collections import deque


class Node:  # Node that represents a single Node in a binary tree
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self):
        self.root = None  # Reference to the root node of the binary tree

    def is_empty(self):
        return self.root is None  # true of root is None

    def display(self):  # displays binary tree from left to right
        self._display(self.root, 0)
        print()

    # private recursive method
    def _display(self, p, level):
        if p is None:  # Base case for recursion
            return

        self._display(p.rchild, level + 1)
        print()

        for i in range(level):
            print("    ", end='')
        print(p.info)

        self._display(p.lchild, level + 1)



        #self._display(p.lchild, level + 1)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, p):
        if p is None:  # p refers to the root of the subtree
            return

        print(p.info, end=' ')
        self._preorder(p.lchild)  # recursive calls
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None:  # p refers the root of the subtree
            return

        self._inorder(p.lchild)
        print(p.info, end=' ')
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, p):
        if p is None:  # p refers to the root of the subtree
            return

        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, end=' ')

    def level_order(self):  # All nodes are visited level by level BFS
        if self.root is None:
            print("Tree is empty")
            return

        qu = deque()
        qu.append(self.root)  # Append root node of the tree first

        while len(qu) != 0:
            p = qu.popleft()
            print(p.info, end=' ')

            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)

    def height(self):
        return self._height(self.root)

    def _height(self, p):
        if p is None:  # p refers to the root node of the tree
            return 0

        h_left = self._height(p.lchild)
        print("h is ", h_left, " ", p.info)
        h_right = self._height(p.rchild)

        if h_left > h_right:
            return 1 + h_left
        else:
            return 1 + h_right

    def create_tree(self):
        self.root = Node('G')
        self.root.lchild = Node('P')
        self.root.rchild = Node('I')
        self.root.lchild.lchild = Node('J')
        self.root.rchild.lchild = Node('L')
        self.root.rchild.rchild = Node('k')
        self.root.rchild.rchild.rchild = Node('F')


if __name__ == '__main__':
    bt = BinaryTree()
    bt.create_tree()
    bt.display()


    print("Preorder: ")
    bt.preorder()
    print()

    print("Inorder: ")
    bt.inorder()
    print()

    print("Postorder: ")
    bt.postorder()
    print()

    print("Level order: ")
    bt.level_order()
    print("\n\n")

    print("Height of tree is ", bt.height())

