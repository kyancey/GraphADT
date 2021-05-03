

class Vertex:
    def __init__(self, label):
        self.label = label



class GraphADT:
    def __init__(self):
        self.adjacency_list = dict()
        self.edge_weights = dict()

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = list()

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def __getitem__(self, label):
        for vertex in self.adjacency_list:
            if vertex.label == label:
                return vertex
        raise KeyError