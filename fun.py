class BST:
    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
    
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        if (self.root is None):
            self.root = BST.Node(value)
        else:
            curr = self.root
            inserted = False
            while not inserted:
                # if value to insert is less than current node
                if value < curr.value:
                    # if left node is not None, keep going
                    if curr.left is not None:
                        curr = curr.left
                    # otherwise, if it is None, set to value
                    else:
                        curr.left = BST.Node(value)
                        inserted = True
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = BST.Node(value)
                        inserted = True
                        
            curr = BST.Node(value)


    def print_between(self, min, max):
        pass

node = BST.Node(2)
BST(node)
