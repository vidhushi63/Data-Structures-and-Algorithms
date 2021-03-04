class graph:
    graph={}
    vertices=0
    def __init__(self,vertices):
        self.vertices=vertices
        for i in range(1,vertices+1):
            self.graph[i]=[]
        print(self.graph)
    def addEdges(self,edges):
        for i in edges:
            self.graph[i[0]].append(i[1])
            self.graph[i[1]].append(i[0])
        print(self.graph)
vertices=4
edges=[[1,2],[1,3],[1,4],[2,3]]
graph=graph(vertices)
graph.addEdges(edges)