str = "bacddbbabd"
lpa = [0]*len(str)

i=1
j=0
k = 1

while (i < len(str)):
    if str[i] == str[j]:
        lpa[k] = j+1
        i+=1
        j+=1
        k+=1
    else:
        if j!=0:
            j = lpa[j-1]
        else:
            lpa[k]=0
            i+=1
            k+=1
            
print((lpa[-1))
