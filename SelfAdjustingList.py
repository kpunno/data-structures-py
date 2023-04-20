
class SelfAdjustingList:
    class Node:
        def __init__(self, data, next, prev):
            self.data = data
            self.next = next
            self.prev = prev
    def __init__(self, first_node):
        self.front = None
        self.back = None

    def search(self, value):
        node = self.front
        while (node.next):
            node = node.next
            if node.data == value:
                node.prev.next = node.next
                node.next.prev = node.prev
                return node