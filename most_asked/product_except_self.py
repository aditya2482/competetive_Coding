class Solution:
    def productExceptSelf(self, nums):
        sol = []
        lmul,rmul = [1]*len(nums),[1]*len(nums)

        lmul[1] = nums[0]
        rmul[len(nums)-2] = nums[len(nums)-1]

        for i in range(2,len(nums)):
            lmul[i] = lmul[i-1]*nums[i-1]

        for i in range(len(nums)-3,-1,-1):
            rmul[i] = rmul[i+1]*nums[i+1]

        for i,j in zip(lmul,rmul):
            sol.append(i*j)

        return sol
        

nums = [1,2,3,4]
sol = Solution()
sol.productExceptSelf(nums)