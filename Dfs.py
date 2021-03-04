from collections import deque
def Graph(edges):
    graph={}
    for i in range(1,vertices+1):
        graph[i]=[]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    return graph
def dfs_util(s,graph,visited,dfs_Ans):
    visited[s]=True
    dfs_Ans.append(s)
    for adj in graph[s]:
        if visited[adj]==False:
            dfs_util(adj,edges,visited,dfs_Ans)
def dfs(s,edges,vertices):
    graph=Graph(edges)
    visited=[False]*(vertices+1)
    dfs=[]
    dfs_util(s,edges,visited,dfs)
    return dfs
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
vertices = 6
ans = dfs(1, edges, vertices)
print(ans)
