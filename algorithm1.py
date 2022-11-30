'''
Kruskal's Algorithm

Multiple Graph Representations:

1. Graph w/ (Vertices, Edges) classes
2. Matrix Representation ? (probably faster since classes will have bigger overhead for accesses)

'''
########### Disjoint Set ###########

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

# returns parent of given vertex
# ds = disjoint_sets
# v = vertex
def find(ds, v):
    if ds[v].parent != v:
        ds[v].parent = find(ds, ds[v].parent)
    return ds[v].parent

# combines the two subsets that contain u and v
# ds = disjoint_sets that contains all of our subsets
def union(ds, u, v):    
    # u rank bigger
    if ds[u].rank > ds[v].rank:
        ds[v].parent = u
    # v rank bigger
    elif ds[v].rank > ds[u].rank:
        ds[u].parent = v
    # same rank, choose one, increment rank by one
    else:
        ds[v].parent = u
        ds[u].rank += 1

########### Disjoint Set ###########


def adding_edge_creates_no_cycle(edge, disjoint_sets):
    '''
    IN:
        edge - [id, startid, endid, length]
        disjoint_sets - list of Subset() objs, initially universal set of (v, 0) for (parent, rank)
    OUT:
        True if adding edge to our MST (represented by our disjoint_sets) doesn't create a cycle
        False otherwise

    Should use disjoint set data structure
    with "union by rank" and "path compression" 
    
    '''
    # compare parents of vertices of this new edge
    v = edge[1]
    u = edge[2]

    v_parent = find(disjoint_sets, v)
    u_parent = find(disjoint_sets, u)

    if(v_parent == u_parent):
        # creates a cycle
        return False
    else:
        # does not create a cycle
        # update disjoint sets with union
        union(disjoint_sets, v_parent, u_parent)
        # then return True
        return True


def Kruskals_Algo(mst, graph):
    '''
    IN:
        mst - is a graph object that we will use to hold the (verteces, edges) for the Minimum Spanning Tree output
        graph - undirected, connected, weighted graph
            graph.edges - list of Edge objs
            graph.vertices - list of Vertex objs
    OUT:
        MST from graph
        min_dist - the total distance of wiring (sum of all edge weights) for this MST

        min_dist, mst
    '''

    # sort the Edges in order of increasing weight (Length)
    # store edges like [id, start, end, length] 
    n = len(graph.edges)
    l = [[0,0,0,0.0] for i in range(n)]
    for i, edge in enumerate(graph.edges):
        l[i][0] = edge.id  # int 
        l[i][1] = edge.start.id  # int
        l[i][2] = edge.end.id  # int
        l[i][3] = edge.length  # float
    # sort along the 3rd axis (weights, smallest to largest)
    l.sort(key=lambda e: e[3])

    min_dist = 0
    mst_num_edges = 0
    graph_num_vert = len(graph.vertices)
    # create universal set of vertices (you are your own parent, rank 0)
    disjoint_sets = [Subset(graph.vertices[i].id, 0) for i in range(len(graph.vertices))]
    
    # loop thru edges from smallest to biggest weight
    for e in l:
        # stop if have |E| = |V| - 1
        if mst_num_edges == graph_num_vert - 1:
            break

        if adding_edge_creates_no_cycle(e, disjoint_sets):
            min_dist += e[3]
            mst_num_edges += 1
            mst.add_edge(e[0], e[1], e[2], e[3])

    return min_dist, mst
