class Solution:
    def isValid(self, s: str) -> bool:
        # First try
        # Got stuck with how to match the closing and opening brackets
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["} # key = closing bracket : value = opening bracket
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
