
def Prims_Algo_1(mst, graph):
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