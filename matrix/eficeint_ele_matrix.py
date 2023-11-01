def find_ele(matrix,j,i,target):
    try:
        starting_point = matrix[j][i]
        if target ==  starting_point:
            print("element found at index", j ,i)
        if starting_point < target:
            j=j+1
            find_ele(matrix,j,i,target)
        if starting_point > target:
            i = i-1
            starting_point = matrix[j][i]
            find_ele(matrix,j,i,target)
    except:
        print("element not found")



matrix = [[1,2,3],[4,5,6],[7,8,9]]
i = len(matrix)-1
j = 0
find_ele(matrix,j,i,8)



