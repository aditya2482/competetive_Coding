def selection_sort(aray):
    for i in range(0,len(aray)):
        for j in range(0,len(aray)):
            if aray[i] < aray[j]:
                aray[i],aray[j] = aray[j],aray[i]
    return aray


aray = [3,2,9,2,0,1]
print(selection_sort(aray))