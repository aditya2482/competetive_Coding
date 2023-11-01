def divi(arr,num):
    count = 0
    while num != 0 :
        arr[1] = arr[1]//2
        count+=1
        num = num-1
    print(count)
    print(arr[1])
    return count*arr[1]

arr = [2,4]
num = 1
print(divi(arr,num))    