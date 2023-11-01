class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)
        for n in nums:
            if (n-1) not in nums:
                curr_len = 1
                while (n+curr_len) in nums:
                    curr_len+=1
                max_len = max(curr_len,max_len)
        return max_len if len(nums) != 1 else 1

        