# Two Pointer

target = 9
class Solution:
    def twoSum(self, numbers):
        i,j = 0,len(numbers)-1
        while i < j:
            curr = numbers[i]+numbers[j]
            if curr > target:
                j-=1
            elif curr < target:
                i+=1
            else:
                return [i+1,j+1]
        # TLE
        # for i in range(0,len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]i = 0
