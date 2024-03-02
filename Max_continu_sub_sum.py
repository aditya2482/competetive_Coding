def main(array,k):
    curr_sum = 0
    sub_count = 0
    max_sub = 0
    sub = []
    for i in array:
        curr_sum+=i
        sub.append(i)
        if curr_sum == k:
            max_sub = max(len(sub),max_sub)
            curr_sum = 0
            sub = []
        elif curr_sum > k:
            curr_sum = 0
            sub = []
        else:
            pass
    
    return max_sub


print(main([5,5,1,2,2],5))
