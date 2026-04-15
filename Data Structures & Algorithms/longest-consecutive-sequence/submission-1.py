class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        sortedNums = sorted(nums)
        print(sortedNums)
        longest = 1
        cur = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i] == sortedNums[i-1]:
                cur += 0
                # print(f"same: cur = {cur}")
            elif sortedNums[i] == sortedNums[i-1] + 1:
                cur += 1
                # print(f"consec: cur = {cur}")
            else:
                # print(f"else: cur = {cur}")
                if cur > longest:
                    longest = cur
                cur = 1
        if cur > longest:
            longest = cur
        return longest