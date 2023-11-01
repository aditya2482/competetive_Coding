# removing element from a given index list.

def kille(arr,pos,n,defe = []):
    if len(arr) == 0:
        print(defe)
        return
    q = pos.pop(0) 
    element = arr.pop(q-1)
    defe.append(element)
    kille(arr,pos,n-1,defe)

arr = [2,6,1,4,2]
pos = [3,1,3,1,1]
n = len(arr)
kille(arr,pos,n,defe=[])