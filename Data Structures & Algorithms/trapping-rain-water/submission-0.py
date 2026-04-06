class Solution:
    def trap(self, height: List[int]) -> int:
        # Second Try with help
        # for each i, water = min(leftWall, rightWall) - height[i]
        # arrays for maxLeft and maxRight for each i so we can know the "walls" for each water pool

        maxLeft = [0] * len(height)
        lMax = 0
        for i in range(len(height)):
            maxLeft[i] += lMax
            if height[i] > lMax:
                lMax = height[i]

        maxRight = [0] * len(height)
        rMax = 0
        for i in range(len(height) - 1, -1 , -1):
            maxRight[i] += (rMax)
            if height[i] > rMax:
                rMax = height[i]

        totalWater = 0
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water > 0:
                totalWater += water

        return totalWater


