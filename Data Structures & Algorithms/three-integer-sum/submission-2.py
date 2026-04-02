class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two Pointers on each element to get Three sum
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointers (two sum solution)
            l,r = i + 1, len(nums)-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output
