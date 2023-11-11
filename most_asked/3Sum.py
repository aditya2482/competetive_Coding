class Solution:
    def threeSum(self,nums):
        sol = []

        for i in range(len(nums)):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                sm = nums[i]+nums[l]+nums[r] 
                if sm < 0:
                    l+=1
                elif sm > 0:
                    r-=1
                else:
                    sol.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
            return sol
        

        # TLE - # for loop approach - check every case

        


                    
        
        