class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute Force Attempt
        for n in range(len(numbers)):
            for m in range(len(numbers)):
                if numbers[n] + numbers[m] == target and numbers[n] < numbers[m]:
                    return [n+1,m+1]
