import BinaryTree


class EmptyTreeError(Exception):
    pass


class Node:

    def __init__(self, data):
        self.info = data
        self.lchild = None
        self.rchild = None


class BinarySearchTree:

    def __init__(self):
        self.root = None  # refers to the root node of the tree and I initialize it to None

    def is_empty(self):
        return self.root is None

    # Insert values to BST with recursion
    def insert_recursion(self, some_value):
        self.root = self._insert(self.root, some_value)

    def _insert(self, p, x): # There are 2 terminating conditions
        if p is None:   # when p is None
            p = Node(x)

        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild, x)
        else:   # when x == p.info, node is already in the BST
            print(x, " already present in the tree.")

        return p

    # Search for a value in the tree using recursion
    def search_recursion(self, some_value):
        return self._search(self.root, some_value) is not None

    def _search(self, p, x):
        if p is None:
            return None  # The key was not found
        if x < p.info:  # Searches the left subtree
            return self._search(p.lchild, x)
        if x > p.info:  # Searches the right subtree
            return self._search(p.rchild, x)
        return p

    # Insert values iteratively
    def insert_iteratively(self, some_value):
        p = self.root  # refer to the root node
        par = None      # refers to parent node, its trailing p.

        while p is not None:
            par = p
            if some_value < p.info:
                p = p.lchild
            elif some_value > p.info:
                p = p.rchild
            else:
                print(some_value, " is already present in the tree.")
                return
        temp = Node(some_value)
        if par is None:
            self.root = temp
        elif some_value < par.info:
            par.lchild = temp
        else:
            par.rchild = temp

    # search for key using iteration
    def search_iteratively(self, some_value):
        # refer to the root node
        p = self.root

        while p is not None:
            if some_value < p.info:  # move to the left child
                p = p.lchild
            elif some_value > p.info: # move to the right child
                p = p.rchild
            else:  # x = p.info, found the value
                return True
        return False

    # using recursion to delete a value from a subtree
    def delete_recursion(self, some_value):
        self.root = self._delete(self.root, some_value)

    def _delete(self, p, x):
        if p is None:
            print(x, " is not found")
            return p

        if x < p.info:  # Delete from the left subtree
            p.lchild = self._delete(p.lchild, x)
        elif x > p.info:  # Delete from the left subtree
            p.rchild = self._delete(p.rchild, x)
        else:
            # to be deleted is found
            if p.lchild is not None and p.rchild is not None:  # 2 children
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild, s.info)
            else:  # 1 child or no child
                if p.lchild is not None:  # Only the left child
                    ch = p.lchild
                else:
                    ch = p.rchild   # only right child or no child
                p = ch
        return p

    # delete using iteration
    def delete_iteration(self, some_value):
        p = self.root
        par = None  # reefers to the parent node

        while p is not None:
            if some_value == p.info:
                break
            par = p    # since p is not none move parent to node p
            if some_value < p.info:
                p = p.lchild
            else: # some_value > p.info
                p = p.rchild

        # test the value of p
        if p is None:
            print(some_value, "was not found.")

        # CASE C: node with 2 children
        # Find inorder successor and its parent

        if p.lchild is not None and p.rchild is not None:
            ps = p
            s = p.rcild

            while s.lchild is not None:
                ps = s      # parent of inorder successor
                s = s.lchild    # inorder successor

            p.info == s.info
            p = s
            par = ps

        # CASE B and A: Node has 1 or no children
        if p.lchild is not None:  # node to be deleted has left child
            ch = p.lchild
        else:                     # node to be deleted has a right child
            ch = p.rchild

        if par is None:
            self.root = ch        # node to be deleted is root
        elif p == par.lchild:     # node is left child of its parent
            par.lchild = ch
        else:                     # node is right child of its parent
            par.rchild = ch

    # Look for min value using iteration
    def minimum_iteration(self):
        if self.is_empty():
            raise EmptyTreeError("Tree is empty.")
        p = self.root

        while p.lchild is not None:
            p = p.lchild
        return p.info

    # Look for max value using iteration
    def maximum_iteration(self):
        if self.is_empty():
            raise EmptyTreeError("Tree is empty.")

        p = self.root

        while p.rchild is not None:
            p = p.rchild

        return p.info

    # look for min value using recursion
    def minimum_recursion(self):
        if self.is_empty():
            raise EmptyTreeError("Tree is empty.")
        return self._min(self.root).info

    def _min(self, p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)

    # max value using recursion
    def maximum_recursion(self):
        if self.is_empty():
            raise EmptyTreeError("Tree is empty")
        return self._max(self.root).info

    def _max(self, p):
        if p.rchild is None:
            return p
        return self._max(p.rchild)


if __name__ == '__main__':
    print("Testing")
    bst = BinarySearchTree()
    bst.insert_recursion(56)
    bst.insert_recursion(38)
    bst.insert_recursion(10)
    bst.insert_recursion(70)
    bst.insert_recursion(88)
    bst.insert_recursion(99)
    bst.insert_recursion(66)
    print(bst.search_recursion(56))
