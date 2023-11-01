def shortest_path(graph,node,d,distance,parent):
    distance[node] = d
    for child in graph[node]:
        if parent !=child:
            shortest_path(graph,child,distance[node]+1,distance,node)


edges = [[0,1],[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[5,6]]
nodes = [1,2,3,4,5,6,7]

graph = {}
distance = {}


for node in range(7):
    graph[node] = []
    distance[node] = None

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

start = 0
distance[start] = 0
shortest_path(graph,start,0,distance,-1)



