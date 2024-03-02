def main(array):
    curr_max = 0
    maxx = 0
    for i in range(0,len(array)-1):
        if array[i] == 1 and array[i+1] == array[i]:
            maxx+=1
            continue
        curr_max = max(maxx,curr_max)
        maxx = 0




    return 0 if sorted(list(set(array)))[0] ==0 and len(set(array)) ==1 else curr_max+1

print(main([0,0,0,1]))
