nodes = [[0,1],[0,2],[0,0],[1,2],[2,3],[3,1],[3,4]]

# matrix format
temp = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(0)
    temp.append(row)

for (u,v) in nodes:
    temp[u][v]=1
    temp[v][u]=1

# for item in temp:
#     print(item)


# adjancy format
dict = {}
for i in range(5):
    dict[i] = []


for (u,v) in nodes:
    dict[u].append(v)
    dict[v].append(u)

print(dict)