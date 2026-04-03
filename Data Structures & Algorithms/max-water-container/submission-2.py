class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # First Attempt
        # max_water = min(leftMax, rightMax) * width
        l, r = 0, len(heights) - 1
        leftMax, rightMax = 0, 0
        maxArea = 0
        while l < r:
            width = r - l
            print(leftMax, rightMax)
            print(f"width: {width}")
            area = min(heights[l], heights[r]) * width
            print(f"area: {area}")
            if area > maxArea:
                leftMax, rightMax = l, r
                maxArea = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea


