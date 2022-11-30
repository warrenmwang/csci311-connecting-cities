

def Prims_Algo_2(mst, graph):
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

    print(verticesList)
    print(visitedEdges)

      
    #add vertex to visited list and add to numVisited
    print(f"Added Vertex {curVertex.id}")
    verticesList.append(curVertex.id)
    numVisited += 1
    #print(numVisited)
  
  
  

  return minDist, mst


# priority queue


# TODO: Implement Priority Queue, probably using a minimum binary heap

    
      
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
  numVisited = 0
  totalVertices = len(graph.vertices)
  totalEdges = len(graph.edges)
  minDist = 0
  allEdges = graph.edges
  visitedVertices = [None] * totalVertices
  #print(visitedVertices)

  outwardEdges = {} #Dictionary to store ID and length of outward edges

 # print(outwardEdges.get(100))

  visitedEdges = [None] * totalEdges

  curVertex = graph.vertices[0]
  curID = 0; 
  visitedVertices[curID] = int(curVertex.id)
  numVisited += 1

  while numVisited < totalVertices:

    for e in curVertex.connectingEdges:
      start = e.start.id
      end = e.end.id
      num = e.id
      #if it has never been used 
      if (visitedEdges[num] == None):
        #it has never been used but has two vertices we have already used
        if (visitedVertices[start] != None) and (visitedVertices[end] != None):
          #add edge to used list
          visitedEdges[num] = num
          #remove edge from usable dictionary
          if outwardEdges.get(num) != None:
            outwardEdges.pop(num)
        else: #never been used but has a vertex we havent added yet
          outwardEdges[num] = e.length
          

    sortedEdges = dict(sorted(outwardEdges.items(), key=lambda x:x[1]))
    #print(sortedEdges)
    smallestID = min(sortedEdges, key=sortedEdges.get)
   # print(f"Smallest edge {smallestID}")
   # print(f"Smallest length {outwardEdges.get(smallestID)}")
    minDist += outwardEdges.get(smallestID)
    edge = allEdges[smallestID]
    mst.edges.append(edge)
    
    outwardEdges.pop(smallestID) #remove the used edge from usable list
    visitedEdges[smallestID] = smallestID #add the used edge to the visited list

    curEdge = allEdges[smallestID]
    if (visitedVertices[curEdge.start.id] == None):
      curVertex = graph.vertices[curEdge.start.id]
    elif (visitedVertices[curEdge.end.id] == None):
      curVertex = graph.vertices[curEdge.end.id]

    visitedVertices[curVertex.id] = int(curVertex.id)
    numVisited +=1

  #print(f"Minimum Distance: {minDist}")
  return minDist, mst