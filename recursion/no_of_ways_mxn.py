def mxn(m,n):
    if m ==1 or n ==1 :
        return 1 
    
    ans = mxn(m-1,n)+mxn(m,n-1)
    return ans

print(mxn(3,3))