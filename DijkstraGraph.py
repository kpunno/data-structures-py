
class DjikstraGraph:
    def __init__(self, length):
        self.length = length
        self.the_graph = [[]] * length
        for i in range(length):
            temp = []
            temp.append(i)
            self.the_graph[i] = temp

    def display(self):
        print(self.the_graph)

the_graph = DjikstraGraph(8)
the_graph.display()