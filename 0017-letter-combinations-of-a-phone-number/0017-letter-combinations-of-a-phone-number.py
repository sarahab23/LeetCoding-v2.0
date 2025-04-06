class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res, word = [], ""
        phone = {}
        phone[2] = ["a","b","c"]
        phone[3] = ["d","e","f"]
        phone[4] = ["g","h","i"]
        phone[5] = ["j","k","l"]
        phone[6] = ["m","n","o"]
        phone[7] = ["p","q","r","s"]
        phone[8] = ["t","u","v"]
        phone[9] = ["w","x","y","z"]

        def dfs(i):
            nonlocal word
            if i == len(digits):
                res.append(word)
                return
            for c in phone[int(digits[i])]:
                word += c
                dfs(i + 1)
                word = word[:-1]

        dfs(0)
        return res