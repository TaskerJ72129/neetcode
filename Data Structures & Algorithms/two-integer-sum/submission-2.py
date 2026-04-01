class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {} # value : index
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums_hashmap:
                return [nums_hashmap[difference], i]
            else:
                nums_hashmap[nums[i]] = i
                