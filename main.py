import argparse
from algorithm1 import Kruskals_Algo
from algorithm2 import Prims_Algo
import time


# An edge in the graph
class Edge:

    def __init__(self, id, start, end, length):
        self.id = id  # int
        self.start = start  # Vertex()
        self.end = end  # Vertex()
        self.length = length  # float

    def __str__(self):
        return f"{self.id=} {self.start=} {self.end=} {self.length=}"


# A vertex in the graph
class Vertex:

    def __init__(self, id):
        self.id = id  # int
        self.neighbors = set()  # Vertices
        self.connectingEdges = set()  # edges that are connected to that vertex

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)


# A representation of a weighted, undirected graph
class Graph:

    def __init__(self):
        self.edges = []  # list of edges
        self.vertices = {}  # a dictionary of vertices (class Vertex)

    def add_edge(self, id, start, end, length):
        # add start and end nodes to the vertices dictionary if first encountered
        if start not in self.vertices:
            self.vertices[start] = Vertex(start)
        if end not in self.vertices:
            self.vertices[end] = Vertex(end)
        # add the edge to edge list
        new_edge = Edge(id, self.vertices[start], self.vertices[end], length)
        self.edges.append(new_edge)
        # connect start node and end node
        self.vertices[start].neighbors.add(self.vertices[end])
        self.vertices[end].neighbors.add(self.vertices[start])
        # connect the edges to the start and end node
        self.vertices[start].connectingEdges.add(new_edge)
        self.vertices[end].connectingEdges.add(new_edge)

    def __str__(self):
        out = ''
        for v in self.vertices.values():
            out += str(v) + ': ' + str(v.neighbors) + '\n'
        return out


if __name__ == '__main__':
    entire_prog_start = time.time()
    parser = argparse.ArgumentParser(description="inputfile outputfile")
    parser.add_argument('algo_to_use', type=int)
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()
    algo_to_use = args.algo_to_use
    if algo_to_use not in [1, 2]:
        print("Invalid algorithm choice. Options:\n1 - Kruskal\n2 - Prim")
        exit()
    infile = args.input_file
    outfile = args.output_file

    # read input
    with open(infile, "r") as file:
        graph = Graph()
        sum_all_weights = 0
        for line in file:
            inp = line.strip().split(" ")
            graph.add_edge(int(inp[0]), int(inp[1]), int(inp[2]),
                           float(inp[3]))
            sum_all_weights += float(inp[3])

    # basic graph info
    graph_vertices = len(graph.vertices)
    graph_edges = len(graph.edges)

    # I'm curious about graph density
    totAvgNeighbors = 0
    for v in graph.vertices.keys():
        totAvgNeighbors += len(graph.vertices[v].neighbors)

    print(f"Vertices: {graph_vertices}\nEdges: {graph_edges}")
    print(
        f"Average Vertex Degree: {totAvgNeighbors / len(graph.vertices.keys())}"
    )
    print(
        f"Baseline Comparison - Adding all weights together: {sum_all_weights}"
    )
    ##########################
    if algo_to_use == 1:
        # kruskal's
        # hand checked against test.txt, good
        MST1 = Graph()
        kruskal_start = time.time()
        min_dist1, MST1 = Kruskals_Algo(MST1, graph)
        kruskal_end = time.time()
        print("==================")
        print(f"Kruskal ran in: {kruskal_end - kruskal_start} s")
        print(f"Kruskal's Algorithm gets total min distance: {min_dist1}")
        with open(f"{outfile}", "w") as file:
            for e in MST1.edges:
                file.write(f"{e.id} {e.start} {e.end} {e.length}\n")
        print(f"MST written to {outfile}")
        print("==================")
    else:
        # prim's
        MST2 = Graph()
        prim_start = time.time()
        min_dist2, MST2 = Prims_Algo(MST2, graph)
        prim_end = time.time()
        print("==================")
        print(f"Prim ran in {prim_end - prim_start} s")
        print(f"Prims's Algorithm gets total min distance: {min_dist2}")
        with open(f"{outfile}", "w") as file:
            for e in MST2.edges:
                file.write(f"{e.id} {e.start} {e.end} {e.length}\n")
        print(f"MST written to {outfile}")
        print("==================")

    print(f"Entire program took {time.time() - entire_prog_start}")
