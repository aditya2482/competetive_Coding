from collections import Counter

def maxDuplicates(array):
    ans = float('-inf')
    dict = Counter(array)
    for key in dict:
        if dict[key] > ans:
            ans = max(ans,dict[key])
        else:
            pass
    key = list(filter(lambda x: dict[x] == ans,dict))
    return max(key)


array = [1,1,1,1,2,2,2,2,3]
print(maxDuplicates(array))