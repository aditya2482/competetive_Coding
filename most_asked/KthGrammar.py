# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0


# TLE
    
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        import collections

        dicts = collections.defaultdict(list)
        dicts[1].append(0)

        k=k-1

        for i in range(2,n+1):
            for elem in (dicts[i-1]):
                value = str()
                if elem == 0:
                    value = "01"
                if elem == 1:
                    value = "10"
                final = [int(i) for i in value]
                for v in final:
                    dicts[i].append(v)
        return dicts[n][k]
        

# optimised recurse

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        half = 2**(n-1)//2
        if n == 1:
            return 0
        if k > half:
            return 1 - self.kthGrammar(n,k-half) # check if k is in the other half, inverse the index in first half
        return self.kthGrammar(n-1,k) # return the previous row kth element
    
    

        

