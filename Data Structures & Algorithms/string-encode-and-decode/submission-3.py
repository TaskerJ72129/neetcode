class Solution:
    # first attempt brute force
    # problem when the seperator is in the input
    # got help with getting a valid seperator 
    def encode(self, strs: List[str]) -> str:
        stringOut = ""
        for s in strs:
            stringOut += s
            stringOut += "\#"
        return stringOut

    def decode(self, s: str) -> List[str]:
        listOut = s.split("\#")
        listOut.pop()
        return listOut