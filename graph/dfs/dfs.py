def dfs(graph,node,visited=set()):
    print(node)
    visited.add(node)
    if graph[node]:
        for child in graph[node]:
            if child not in visited:
                dfs(graph,child)


nodes = [[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[5,6]]
start = 1
graph = {}

for i in range(7):
    graph[i] = []
for (u,v) in nodes:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph,start)














