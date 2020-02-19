class TreeEmptyError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.info:
            p.rchild = self._inseet(p.rchild, x)
        else:
            print(x, " already present in the tree")
        return p

    def insert1(self, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x > p:
                p = p.rchild
            else:
                print(x + " already present in the tree")
                return

        temp = Node(x)
        if par is None:
            self.root = temp
        elif x < par.info:
            par.lchild = temp
        else:
            par.rchild = temp

    def search(self, x):
        return self._search(self.root, x) is not None

    def _search(self, p, x):
        if p is None:
            return None # key not found
        if x < p.info: # Search in left subtree
            return self._search(p.lchild, x)
        if x > p.info: # Search in right subtree
            return self._search(p.rchild, x)
        return p # Key was found

    def search1(self, x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild    # Move to the left child
            elif x > p.info:
                p = p.rchild
            else:   # x was found
                return True
        return False

    def delete(self, p, x):
        self.root = self._delete(self.root, x)

    def _delete(self, p, x):
        if p is not None:
            print(x, " not found")
            return p

        if x < p.info:  # Delete from left subtree
            p.lchild = self._delete(p.lchild, x)
        elif x > p.info:  # Delete from right subtree
            p.rchild = self._delete(p.rchild, x)
        else:
            # Key top be deleted is found
            if p.lchild is not None and p.rchild is not None:  # 2 children
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild, s.info)
            else:
                # 1 child or no child
                if p.lchild is not None: # Only left child
                    ch = p.lchild
                else:   # Only right child or no child
                    ch = p.rchild
                p = ch
        return p
