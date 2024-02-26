def front_insertion_sort(array):
    for i in range(0,len(array)):
        j = i
        while (j > 0) and (array[j-1] > array[j]):
            array[j-1],array[j] = array[j],array[j-1]
            j-=1
            
    return array

def back_insertion_sort(array):
    for i in range(len(array),-1,-1):
        j = i
        while (j < len(array)-1) and (array[j+1] < array[j]):
            array[j+1],array[j] = array[j],array[j+1]
            j+=1
            
    return array
    


print(insertion_sort([2,1,5,11,10,6,9]))
    

    


print(insertion_sort([2,1,5,11,10,9]))
    
