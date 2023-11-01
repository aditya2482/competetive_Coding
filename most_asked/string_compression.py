from collections import Counter

def compression(s):
    li = [*s]
    li = sorted(list(set(li)))
    result = ''
    counts = Counter(s)
    for i in range(len(li)):
        if counts[li[i]] == 1:
            result+=li[i]
        else:
            result+=li[i]
            result+=str(counts[li[i]])

    return result

s = "abbccdd"
print(compression(s))





