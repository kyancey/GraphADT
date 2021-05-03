from GraphADT import GraphADT
from GraphADT import Vertex

if __name__ == "__main__":
    vertex_a = Vertex("A")
    vertex_b = Vertex("B")
    vertex_c = Vertex("C")
    vertex_d = Vertex("D")
    vertex_e = Vertex("E")
    vertex_f = Vertex("F")

    g = GraphADT()
    g.add_vertex(vertex_a)
    g.add_vertex(vertex_b)
    g.add_vertex(vertex_c)
    g.add_vertex(vertex_d)
    g.add_vertex(vertex_e)
    g.add_vertex(vertex_f)

    g.add_undirected_edge(vertex_a, vertex_b)
    g.add_undirected_edge(vertex_c, vertex_a)
    g.add_undirected_edge(vertex_d, vertex_a)
    g.add_undirected_edge(vertex_e, vertex_d)
    g.add_undirected_edge(vertex_f, vertex_e)

    print(g["B"])
    pass