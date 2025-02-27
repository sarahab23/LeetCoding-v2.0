class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # countS.get(s[i], 0) -> checking if countS[s[i]] exist, if not give value 0

        # We're doing 'countT.get(ch, 0)' instead of countT[ch], because we don't know if the T
        # map has key ch, so we check using 'countT.get(ch, 0)'
        for ch in countS:
            if countS[ch] != countT.get(ch, 0):
                return False

        return True