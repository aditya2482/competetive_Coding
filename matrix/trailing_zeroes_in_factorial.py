# finding the no of 5/25/125/625 ....... as no of 5 is always less than 2 and every 5 is corresponding to trailing zeroes.

def find_trailing_zeroes(n):
    res = 0
    for i in range(5,n,i*5):
        res = res+n/i
    return res

print(find_trailing_zeroes(n))