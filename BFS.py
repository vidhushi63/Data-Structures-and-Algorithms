#BFS Implementation
from collections import deque
def gridToAdjecency(edges):
    graph=dict()
    for i in range(1,vertices+1):
        graph[i]=list()
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    return graph
def bfs(s,edges,vertices):
    graph=gridToAdjecency(edges)
    bfs=[]
    q=deque([])
    q.append(s)
    visited=[False]*(vertices+1)
    visited[s]=True
    while len(q)!=0:
        curr=q.popleft()
        bfs.append(curr)
        for v in graph[curr]:
            if visited[v] is not True:
                q.append(v)
                visited[v]=True
    return bfs
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
vertices = 6
ans = bfs(1, edges, vertices)
print(ans)
