import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

recent_result = 0

arr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []

for i in arr:
    if i in ["+","-","*","/"]:
        val1 = stack.pop()
        val2 = stack.pop()
        recent_result = ops[i](int(val2),int(val1))
        stack.append(recent_result)
    else:
        stack.append(i)

print(stack)