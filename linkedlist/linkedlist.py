class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self, front):
        self.front= front

    def pushBack(self, objToPush):
        if (self.front == None):
            self.front = objToPush
        else:
            curr = self.front
            while (curr.next != None):
                curr = curr.next
            curr.next = objToPush

    def pushFront(self, objToPush):
        if self.front == None:
            self.front = objToPush
        else:
            objToPush.next = self.front
            self.front = objToPush

    def showList(self):
        curr = self.front
        while (curr != None):
            if (curr.next != None):
                print(curr.data, end=", ")
            else: print(curr.data, end=".")
            curr = curr.next
        print()



