class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch in "+-*/":
                last, secL = stack.pop(), stack.pop()
                if ch == '/':
                    stack.append(math.ceil(secL/last) if secL/last < 0 else math.floor(secL/last))
                elif ch == '+':
                    stack.append(secL + last)
                elif ch == '-':
                    stack.append(secL - last)
                else:
                    stack.append(secL * last)
            else:
                stack.append(int(ch))

        return stack.pop()