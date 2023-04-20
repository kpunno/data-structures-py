
from linkedlist import LinkedList

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