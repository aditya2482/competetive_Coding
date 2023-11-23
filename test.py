from collections import defaultdict

d = defaultdict(list)
d1 = defaultdict(list)

# l = [[1,0],[2,0],[3,1],[3,2]]
l = [[0,1]]
dict = {}

for i in l:
    d[i[1]].append(i[0])


# print(d,d1)
print(d)

ans = []
for i in d.keys():
    ans.append(i)
    ans.append(d[i])

for i in ans:
    if type(i) == list:
        temp = i
        print(temp)
        for i in i:
            ans.append(i)
            if temp in ans:
                ans.remove(temp)



print(ans)
print(list(set(ans)))

