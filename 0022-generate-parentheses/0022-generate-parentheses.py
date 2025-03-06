class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Rules for backtracking here - 
        # only add "(" -> if open brackets < n
        # only add ")" -> if closed brackets < open brackets
        # string is valid IIF open brackets = closed brackets = n
        res = []
        stack = []

        def backtrack(openB, closeB):
            if openB == closeB == n:
                res.append("".join(stack))
                return
            
            if openB < n:
                stack.append("(")
                backtrack(openB + 1, closeB)
                stack.pop()
            
            if closeB < openB:
                stack.append(")")
                backtrack(openB, closeB + 1)
                stack.pop()


        backtrack(0,0)
        return res