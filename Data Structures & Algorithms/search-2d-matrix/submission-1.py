class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first try
        # initial thought: first check first/last num of each sublist/row to check which sublist the target is in
        # then preform regular binary search on that sublist

        for row in matrix:
            print(row[0] <= target <= row[-1])
            if row[0] <= target <= row[-1]:
                l, r = 0, len(row) - 1

                while l<=r:
                    m = (l+r) // 2
                    if row[m] < target:
                        l = m + 1
                    elif row[m] > target:
                        r = m - 1
                    else:
                        return True
        return False