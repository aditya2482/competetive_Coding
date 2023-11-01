from collections import defaultdict
strs = ["a"]

lis = defaultdict(list)
sol = []

for i in range(len(strs)):
    temp = strs[i]
    temp = ''.join(sorted(temp))
    lis[temp].append(strs[i])

for key,value in lis.items():
    sol.append(value)
        
print(sol)

