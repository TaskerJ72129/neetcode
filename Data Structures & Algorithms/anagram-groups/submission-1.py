class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First attempt, no hints, brute force
        output = [[]]
        output[0].append(strs[0])
        # print(output)
        for i in range(1, len(strs)):
            # print(output)
            foundAnagram = False
            for n in range(len(output)):
                # print(f"strs[i] = {sorted(strs[i])}")
                # print(f"output[n][0] = {sorted(output[n][0])}")
                if sorted(strs[i]) == sorted(output[n][0]):
                    output[n].append(strs[i])
                    foundAnagram = True
                    continue
            if foundAnagram == False:
                output.append([strs[i]])
        return output