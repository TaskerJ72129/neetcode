class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force
        result = []
        for i in range(len(temperatures)):
            if i == len(temperatures)-1:
                    result.append(0)
                    break
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    break
                if j == len(temperatures)-1:
                    result.append(0)
        return result