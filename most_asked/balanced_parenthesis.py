# "{}}" --> two closed brackets per one open brackets

def balance_count(s):
    a = len(s)
    count_operation = 0
    stack = []
    close_count = 0

    for i in range(0,a):
        # first case when open bracket
        if (s[i] == "("):
            if (close_count > 0): #if we encounter opening bracket and one closing is present - one more closing req+ 1 
                count_operation+=1 #one closing bracket
                stack.pop()                        # pop beacuse we go 2 closing bracket for the open bracket
            stack.append(s[i])  # pusing opening bracket to stack and close_count to 0 as now balanced 
            close_count = 0
        
        elif not stack:            # case when no openning bracket at the begining - close bracket
            stack.append("(")
            count_operation+=1 # adding one opening bracket.
            close_count = 1 # we have one closing bracket now
            
        else:
            close_count = (close_count+1)%2
            if close_count == 0:
                stack.pop()

        count_operation+=len(s)*2 - close_count
        return count_operation

if __name__ == "__main__":
    s = "))("
    print(balance_count(s))