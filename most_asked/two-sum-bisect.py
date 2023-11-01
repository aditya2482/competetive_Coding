import bisect

def twoSum(list1,target):
    list1.sort()
    lenList = len(list1)
    count = 0
    for idx,i in enumerate(list1):
        ele = target - i
        left = bisect.bisect_left(list1,ele,idx+1)
        right = bisect.bisect_right(list1,ele,idx+1)
        count = count+right-left
    return count

list1 = [1,2,3,4,5,6,7,8,9,10]
target = 10

print(twoSum(list1,target))
