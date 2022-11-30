

def Prims_Algo(mst, graph):
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
  numVisited = 0 #number of visited vertices
  outwardEdges = [] #useful edges
  verticesList = [] #list of vertices IDs we have visited
  totalVertices = len(graph.vertices) #total number of vertices
  allEdges = graph.edges #store a list of all vertices to use later
  visitedEdges = [] #store the edges we have visited
  minDist = 0 #will be returned at the end

  #print(totalVertices)
  #print("---------")

  
  curVertex = graph.vertices[0] #starting vertex ID
  numVisited += 1
  verticesList.append(curVertex.id)

  while numVisited < totalVertices:
    #add all the edges
    for e in curVertex.connectingEdges:
      if (e.start.id == curVertex.id):
        if (e.end.id not in verticesList and (e.id not in visitedEdges) and (e.id not in outwardEdges)):
          outwardEdges.append(e.id)
      elif(e.end.id == curVertex.id):
        if (e.start.id not in verticesList and (e.id not in visitedEdges) and (e.id not in outwardEdges)):
          outwardEdges.append(e.id)

    #loop through all edges to find minimum one
    smallest = float('inf')
    for edgeID in outwardEdges:
      if allEdges[edgeID].length < smallest:
        smallest = allEdges[edgeID].length #store length of smallest edge
        curEdge = edgeID #store ID of smallest edge
    

    minDist += smallest

    #change our current vertex to the new one at the end of the edge
    edge = allEdges[curEdge]
    if (edge.start.id in verticesList):
      curVertex = graph.vertices[edge.end.id]
    elif (edge.end.id in verticesList):
      curVertex = graph.vertices[edge.start.id]

    #add edge to MST
    mst.edges.append(edge)

    #remove edge from usable list
    outwardEdges.remove(curEdge)
    visitedEdges.append(curEdge)

    

      
    #add vertex to visited list and add to numVisited
    verticesList.append(curVertex.id)
    numVisited += 1
    #print(numVisited)
  
  
  

  return minDist, mst


# TODO: Implement Priority Queue, probably using a minimum binary heap

    
      
def Prims_Algo_2(mst, graph):
    totalVertices = len(graph.vertices) #total number of vertices
    allEdges = graph.edges #store a list of all vertices to use later
    minDist = 0 #will be returned at the end
    curr_mst_size = 0

    # to reduce from O(VE) need to maintain distance estimate from any node to current building tree
    

    while curr_mst_size < totalVertics - 1:
        pass