def dfs(graph,node,visited=set()):
    print(node)
    visited.add(node)
    count = 0
    if graph[node]:
        for child in graph[node]:
            if child not in visited:
                count+=dfs(graph,child)
    
    return count+1

edges = [[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[5,6]]
nodes = [1,2,3,4,5,6]
graph = {}

for i in range(7):
    graph[i] = []
for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)


answer = {}
for i in nodes:
    answer[i] = dfs(graph,i)

print(answer)
# print(dfs(graph,start))

