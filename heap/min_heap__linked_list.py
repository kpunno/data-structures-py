
# implementation of heap sort in linked list
# uses nodes to traverse a tree

class MinHeap:
    class Node:
        def __init__(self, value):
            self.left  = None
            self.left  = None
            self.parent= None

    def minChild(self, node):
        if (node.left and node.right):
            if node.left < node.right:
                return node.left
            else:
                return node.right
        if (node.right):
            return node.right
        else:
            return None

    def __init__(self, array):
        self.tree = array
        self.sort(array)
        
        

