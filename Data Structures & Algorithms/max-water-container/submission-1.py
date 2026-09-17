class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxwater = 0

        while l<r:
            width = r-l
            if heights[l] > heights[r]:
                water = width*heights[r]
                maxwater = max(water, maxwater)
                r-=1
            else:
                water = width*heights[l]
                maxwater = max(water, maxwater)
                l+=1

        return maxwater