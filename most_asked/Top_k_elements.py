from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

cs = Counter()
for i in nums:
    cs[i]+=1

ans = []
[ans.append(i[0]) for i in cs.most_common(k)]

print(ans)