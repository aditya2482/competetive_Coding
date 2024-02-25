def set_zero(matrix, i, j,n,m):
    # set that row x
    for col in range(m):
        if matrix[i][col] == 0:
            pass
        else:
            matrix[i][col] = "x"
    
    for row in range(n):
        if matrix[row][j] == 0:
            pass
        else:
            matrix[row][j] = "x"
    
                
    return matrix
        
    
    

def zeroMatrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                set_zero(matrix, i, j,n,m)
                
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "x":
                matrix[i][j] = 0
    
    return matrix

# Example usage:
my_matrix = [
    [2, 4, 3, 5],
    [1, 0, 0, 6],
    [2 ,3, 6, 0]
]

result_matrix = zeroMatrix(my_matrix, 3, 4)
print(result_matrix)
