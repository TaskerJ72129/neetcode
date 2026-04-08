class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimal time complexity because no sorting
        # convert to tuple because Lists and arrays are mutable and cannot be used as dictionary keys directly
        
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())