class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers Attempt
        l, r = 0, len(numbers)-1
        while l < r:
            #print([l+1, r+1])
            while numbers[l] + numbers[r] > target:
                #print(r)
                r -= 1
            while numbers[l] + numbers[r] < target:
                l += 1
            # if numbers[l] + numbers[r] != target:
            #     l += 1
            # if numbers[l] + numbers[r] != target:
            #     r -= 1

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

        return [l+1, r+1]
            