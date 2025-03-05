class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedBrackets = {"]":"[", ")":"(", "}":"{"}

        for ch in s:
            if ch in closedBrackets:
                if stack and stack[-1] == closedBrackets[ch]: stack.pop()
                else: return False
            else:    
                stack.append(ch)
        
        return True if not stack else False