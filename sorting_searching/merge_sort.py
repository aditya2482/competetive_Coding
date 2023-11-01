# Divide the list into half until atomic element is recv
# initialize the array -- break it in two equal halves


# merge given two array into single array by comparing len of each array
def merge(left_array,right_array):
    result = []
    i = j = 0
    while i <len(left_array) and j < len(right_array):
        if(left_array[i] <= right_array[j]):
            result.append(left_array[i])
            i = i+1
        else:
            result.append(right_array[j])
            j = j+1
    if i < len(left_array):
        while i < len(left_array):
            result.append(left_array[i])
            i+=1
    if j < len(right_array):
        while j < len(right_array):
            result.append(right_array[j])
            j+=1
    return result


# return two subarrays left subarray and right subarray
def divide(array):
    if (len(array) == 1) and (array != None):
        return array
    mid = len(array)//2
    left_array = divide(array[:mid])
    right_array = divide(array[mid:])
    return merge(left_array,right_array)


aray = [89,7,0,-1,73,3]
print(divide(aray))