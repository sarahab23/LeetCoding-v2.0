class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch =='[':
                stack.append(ch)
            else: 
                if not stack: return False
                if ch == ')':
                    if stack[-1] == '(': stack.pop()
                    else: return False
                if ch == '}':
                    if stack[-1] == '{': stack.pop()
                    else: return False
                if ch == ']':
                    if stack[-1] == '[': stack.pop()
                    else: return False


        if not stack: return True
        else: return False
            
            
            
