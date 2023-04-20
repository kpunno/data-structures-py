
### Graph Implementation

class Graph:
    def __init__(self, number_of_verts):
        self.adj_list = [[] for i in range(number_of_verts)]
        self.num_v = number_of_verts
        self.num_e = 0

    def add_vertex(self):
        self.adj_list.append([])
        self.num_v += 1

    def add_edge(self, from_idx, to_idx, weight=1):
        if from_idx < 0 or from_idx >= self.num_v or to_idx < 0 or to_idx >= self.num_v\
            or [(to, weight) for to, weight in self.adj_list[from_idx] if to == to_idx]:
            return False
        else:
            self.adj_list[from_idx].append((to_idx, weight))
            self.num_e += 1
            return True

    def num_edges(self):
        return self.num_e

    def num_verts(self):
        return self.num_v

    def has_edge(self, from_idx, to_idx):
        if 0 <= from_idx < self.num_v and 0 <= to_idx < self.num_v\
            and [(to, weight) for to, weight in self.adj_list[from_idx] if to == to_idx]:
            return True
        else:
            return False

    def edge_weight(self, from_idx, to_idx):
        if from_idx < 0 or from_idx >= self.num_v or to_idx < 0 or to_idx >= self.num_v:
            return None
        for vertex, weight in self.adj_list[from_idx]:
            if vertex == to_idx:
                return weight
        return None

    def get_connected(self, v):
        if v < 0 or v >= self.num_v:
            return []
        return self.adj_list[v]

    def display(self):
        print("updated adj_list ->")
        for i in range(self.num_v):
            print(self.adj_list[i])

graph = Graph(4)
graph.add_edge(1, 2)
graph.display()
print(graph.add_edge(1, 2))
graph.display()