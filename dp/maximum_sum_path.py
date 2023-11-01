array = [[1,2,3],
        [4,5,6],
        [7,8,9]]

# pd -  we have to find the maximum sum from the starting position to the last position - 00 to len(row),len(col)

row = len(array)
col = len(array)

mem=[]
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    mem.append(temp)

mem[0][0] = array[0][0]

for i in range(row):
    for j in range(col):
        print(i,j)
        if i == 0 and j == 0:
            mem[i][j] = array[i][j]
            print(mem[i][j])
        else:
            mem[i-1][j] = mem[i-1][j] if i!=0 else float('inf')
            mem[i][j-1] = mem[i][j-1] if j!=0 else float('inf')
            mem[i][j] = array[i][j] + min(mem[i-1][j],mem[i][j-1])
            print(mem[i][j])
            

        

print(mem)