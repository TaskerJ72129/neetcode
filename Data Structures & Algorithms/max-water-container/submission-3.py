class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # First Attempt
        # max_water = min(leftMax, rightMax) * width
        # Got stuck on how to move the pointers and had to get the hint
        # that you just move the lower height pointer
        l, r = 0, len(heights) - 1
        leftMax, rightMax = 0, 0
        maxArea = 0
        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width
            if area > maxArea:
                leftMax, rightMax = l, r
                maxArea = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea


