import queue

class BST:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            curr = self.root
            inserted = False
            while not inserted:
                if data < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = BST.Node(data)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(data)
                        inserted = True

    def search(self, data):
        curr = self.root
        while (curr != None):
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
            
    def breadth_first_print(self):
        the_nodes = queue.Queue()

        if self.root is not None:
            the_nodes.put(self.root)

        while not the_nodes.empty():
            curr = the_nodes.get()
            if (curr.left):
                the_nodes.put(curr.left)
            if (curr.right):
                the_nodes.put(curr.right)
            print(curr.data, end=" ")

    def recursive_search(self, data, subtree):
        if subtree is None:
            return None
        else:
            if data < subtree.data:
                return self.recursive_search(data, subtree.left)
            elif data > subtree.data:
                return self.recursive_search(data, subtree.right)
            else:
                return subtree
            
    def recursive_insert_helper(self, data, subtree):
        if (subtree == None):
            return BST.Node(data)
        elif (data < subtree.data):
            subtree.left = self.recursive_insert(data, subtree.left)
            return subtree
        else:
            subtree.right = self.recursive_insert(data, subtree.right)
            return subtree
        
    def recursive_insert(self, data):
        self.root = self.recursive_insert_helper(data, self.root)

    def print_inorder(self, subtree):
        if subtree is not None:
            self.print_inorder(subtree.left)
            print(subtree.data, end= " ")
            self.print_inorder(subtree.right)

    def print_preorder(self, subtree):
        if (subtree != None):
            print(subtree.data, end= " ")
            self.print_preorder(subtree.left)
            self.print_preorder(subtree.right)

    def print_between_helper(self, subtree, min, max):
        if (subtree is not None):
            print(subtree.data, end=" ")
            left = subtree.left
            if (left is not None and left.data >= min):
                self.print_between_helper(subtree.left,min,max)
            right = subtree.right
            if (right is not None and right.data <= max):
                self.print_between_helper(subtree.right,min,max)
        else:
            return


    def print_between(self, min, max):
        self.print_between_helper(self.root, min, max)
            
                

        

x = BST()
x.insert(2)
x.insert(5)
x.insert(1)
x.insert(4)
x.insert(50)
x.print_inorder(x.root), print()
x.breadth_first_print(), print()
x.print_preorder(x.root), print()

x.print_between(5, 50)