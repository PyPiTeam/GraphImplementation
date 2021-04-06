# The main purpose of this application is to take in a graph, and to find a shortest path from one node to another node
# This program uses the pseudocode from this video: https://www.youtube.com/watch?v=oDqjPvD54Ss
# Had to make a few changes from the pseudocode since I am using an object here

# Instead of enqueue, it is put
# Instead of dequeue, it is get
# Instead of isEmpty, it is empty
from queue import Queue

class graphImp() :

  def __init__(self, graph, numNodes) :
    self.graph = graph
    self.numNodes = numNodes
    self.toTraverse = Queue(maxsize=numNodes)

  def listAllNodes(self):
    for node in self.graph:
      print(node, end = " ")
    print()

  def listAllNodesAndConnections(self):
    for node in self.graph:
      print("%s ->" % (node), end=" ")
      for adjacents in self.graph[node]:
        print("%s" % (adjacents), end=" ")
      print()

  def addNode(self, nodeName, nodeAdjacents):
    self.graph[nodeName] = nodeAdjacents
    for node in nodeAdjacents:
      self.graph[node].append(nodeName)

  def removeNode(self, nodeName):
    del self.graph[nodeName] 
    for node in self.graph:
      if nodeName in self.graph[node]:
        self.graph[node].remove(nodeName)

  def shortestPath(self, startNode, endNode):

    def solve(self, startNode):
      self.toTraverse.put(startNode)

      visited = {}
      for node in self.graph:
        visited[node] = False
      visited[startNode] = True

      prev = {}
      for node in self.graph:
        prev[node] = None

      while(not self.toTraverse.empty()):
        node = self.toTraverse.get()
        neighbors = self.graph[node]

        for nextt in neighbors:
          if not visited[nextt]:
            self.toTraverse.put(nextt)
            visited[nextt] = True
            prev[nextt] = node
      
      return prev

    def reconstructPath(self, startNode, endNode, prev):
      path = []
      at = endNode
      while at != None:
        path.append(at)
        at = prev[at]
      
      path.reverse()

      if path[0] == startNode:
        return path
      return []

    prev = solve(self, startNode)

    path = reconstructPath(self, startNode, endNode, prev)
    return path

  def shortestPathLen(self, startNode, endNode):
    dist = len(self.shortestPath(startNode, endNode)) - 1 
    print(dist)
    return dist

      #print(toBeTraversed)
      
      




graph = {"A": ["B", "C", "F"], 
 "B": ["A", "D"], 
 "C": ["A", "E", "F"], 
 "D": ["B", "E"], 
 "E": ["C", "D"], 
 "F": ["A", "C"]}

numNodes = 6

graphObject = graphImp(graph, numNodes)

graphObject.listAllNodesAndConnections()

print(graphObject.shortestPath("A", "E"))
graphObject.shortestPathLen("A", "E")

  

