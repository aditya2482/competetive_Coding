graph = [[1,4,10],[1,2,1],[2,3,2],[3,4,4],[1,3,10],[2,4,2],[4,3,3]]

row = 5
col =5

final_graph = []
for i in range(0,row):
    temp = []
    for j in range(0,col):
        temp.append(999999999)
    final_graph.append(temp)


for i in range(row):
    for j in range(col):
        if i == j:
            final_graph[i][j] =0


for i,j,k in graph:
    final_graph[i][j] = k



# floyd-warshall-implementation

for k in range(1,row):
    for i in range(1,row):
        for j in range(1,col):
            if final_graph[i][k] + final_graph[k][j] < final_graph[i][j]:
                print()
                final_graph[i][j] = final_graph[i][k] + final_graph[k][j]


for i in final_graph:
    print(i)



