def binary_search(arr,low,high,value):
    if low > high:
        return False
    mid = int((low+high)//2)
    if array[mid] == value:
        return True
    elif value > arr[mid]:
        binary_search(array,mid+1,high,value)
    elif value < arr[mid]:
        binary_search(array,low,mid-1,value)
    
    return ("element not found")




array = sorted([2,7,3,9,6,4,0])
print(array)
value = 8

print(binary_search(array,0,len(array),value))