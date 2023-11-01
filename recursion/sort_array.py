def sort(array):
    def insert (a,array):
        if len(array) == 0 or array[-1] <= a:
            array.append(a)
            return
        temp = array.pop()
        insert(a,array)
        print("indeide-isnert",array)
        array.append(temp)
    
    print("array-entry",array)
    if len(array) == 1:
        return 
    a = array.pop()
    print(a,array)
    sort(array)
    insert(a,array)


array = [4,9,7,6]
sort(array)
for ele in array:
    print(ele)
