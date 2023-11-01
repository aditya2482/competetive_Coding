class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        max_water = 0
        distance = 0
        heights = 0
        while l < r:
            distance = r - l 
            heights = min(height[l],height[r])
            max_water = max(max_water,heights*distance)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return max_water
