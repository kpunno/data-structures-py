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
        
            
list = LinkedList(None)
while (input("Enter any button to continue\nType <exit> to exit\n... ") != "exit"):
    print("Linked list creator")
    print("Your list so far: ")
    list.showList()
    print("-------------------")
    if (list.front != None):
        # First node
        node_name = input("Enter a name for another node: ").__str__()
        location = input("Should we add it at the front or back?\n<f> for front\n<b> for back\n... ")
        if (location == "f"):
            list.pushFront(LinkedList.Node(node_name))
        else:
            list.pushBack(LinkedList.Node(node_name))
    else:
        # Any nodes after first node is pushed
        node_name = input("Enter a name for your first node: ").__str__()
        list.pushFront(LinkedList.Node(node_name))
    print("Your linked list so far: ...")
    list.showList()
    print("====================================")



