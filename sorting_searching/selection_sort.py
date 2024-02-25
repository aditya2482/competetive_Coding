def selection_sort(array):
    for i in range(0,len(array)-1):
        mini = array[i]
        for j in range(i+1,len(array)):
            if array[j] < mini:
                min_index = j
                mini = array[j]
                array[j],array[i] = array[i],array[j]
    return array
    


print(selection_sort([1,6,5,11,10,9]))
    
