#!/usr/bin/python3

import queue

class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __del__(self):
        print("Delete Node object")

class BinaryTree:
    """
    Binary Tree
    """

    def __init__(self):
        self.root = None

    def preorder_dump(self, node):
        """
        node, left subtree, right subtree
        """
        if node is not None:
            print(node.value)
            self.preorder_dump(node.left_child)
            self.preorder_dump(node.right_child)

    def inorder_dump(self, node):
        """
        left subtree, node, right subtree
        """

        if node is not None:
            self.inorder_dump(node.left_child)
            print(node.value)
            self.inorder_dump(node.right_child)

    def postorder_dump(self, node):
        """
        left subtree, right subtree, node
        """
        if node is not None:
            self.postorder_dump(node.left_child)
            self.postorder_dump(node.right_child)
            print(node.value)

    def bfs_dump(self):
        """
        breadth_first_search
        """
        q = queue.Queue()

        q.put_nowait(self.root)

        while(q.empty() is False):
            n = q.get_nowait()
            print(n.value)

            if (n.left_child is not None):
                q.put_nowait(n.left_child)

            if (n.right_child is not None):
                q.put_nowait(n.right_child)

class BinarySearchTree(BinaryTree):

    def insert(self, node, new_node):
        """
        insert in BST
        """

        if self.root is None:
            self.root = new_node
        elif new_node.value <= node.value:
            if node.left_child is None:
                node.left_child = new_node
            else:
                self.insert(node.left_child, new_node)
        elif new_node.value > node.value:
            if node.right_child is None:
                node.right_child = new_node
            else:
                self.insert(node.right_child, new_node)

        print(new_node.value)

    def search(self, value, node, parent = None):
        """
        search in BST
        """

        if node is None:
            print("No match")
            n = None
            p = None
        elif node.value == value:
            print("match")
            n = node
            p = parent
        elif value < node.value:
            n, p = self.search(value, node.left_child, node)
        elif value > node.value:
            n, p = self.search(value, node.right_child, node)

        return n, p

    def delete(self, value):
        """
        delete in BST
        """

    def maxValue(self, node):

        if (node is not None):

            maximum = node

            while(maximum.right_child is not None):
                maximum = maximum.right_child
        else:
            maximum = None

        return maximum

    def minValue(self, node):

        if (node is not None):

            minimum = node

            while(minimum.right_child is not None):
                minimum = minimum.left_child
        else:
            minimum = None

        return minimum

def main():
    """
    This is the docString for the main() function
    """
    print("Start to run main():")

    data = [10, 12, 5, 4, 20, 8, 7, 15, 13]
    """
          10
         /  \
        5   12
       / \    \
      4  8    20
        /    /
       7    15
            /
          13
    """

    bst = BinarySearchTree()

    # insert new node into BST
    for value in data:
        new_node = Node(value)
        bst.insert(bst.root, new_node)

    # search value in BST
    n, p = bst.search(12, bst.root)
    if (n is not None):
        print("%d is found. It's parent is %d" % (n.value, p.value))

    n, p = bst.search(8, bst.root)
    if (n is not None):
        print("%d is found. It's parent is %d" % (n.value, p.value))

    n, p = bst.search(9, bst.root)
    if (n is not None):
        print("%d is found. It's parent is %d" % (n.value, p.value))

    # inorder dump
    print(bst.inorder_dump.__doc__)
    bst.inorder_dump(bst.root)

    # preorder dump
    print(bst.preorder_dump.__doc__)
    bst.preorder_dump(bst.root)

    # postorder dump
    print(bst.postorder_dump.__doc__)
    bst.postorder_dump(bst.root)

    # breadth first search dump
    print(bst.bfs_dump.__doc__)
    bst.bfs_dump()

    # minimum
    m = bst.minValue(bst.root)
    print("minimum = %d" % m.value)

    # maximum
    m = bst.maxValue(bst.root)
    print("maximum = %d" % m.value)

if __name__ ==  "__main__":
    main()
