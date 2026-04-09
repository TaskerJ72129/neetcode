class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First attempt hashmap
        freqElements = defaultdict(int) # element : frequency
        out = []

        for e in nums:
            freqElements[e] += 1
        # print(freqElements)
        
        sortedFreq = sorted(freqElements.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            out.append(sortedFreq[i][0])

        return out

