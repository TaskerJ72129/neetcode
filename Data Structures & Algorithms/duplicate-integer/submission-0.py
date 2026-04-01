class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for n in range(len(nums)):
                if n!= i and nums[n] == nums[i]:
                    return True
        return False