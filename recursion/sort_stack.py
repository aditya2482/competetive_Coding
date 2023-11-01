def sort(stack):
    def insert(a,stack):
        if len(stack) == 0:
            stack.append(a)
            return 
        temp = stack.pop()
        insert(a,stack)
        stack.append(temp)

    if len(stack) == 0:
        return
    a = stack.pop()
    sort(stack)
    insert(a,stack)

stack = [10,9,8,7,6]
sort(stack)
for i in stack:
    print(i)








