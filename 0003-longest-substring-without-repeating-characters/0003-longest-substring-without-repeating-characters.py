class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charPos = {}
        l, r, maxLength = 0, 0, 0

        while r < len(s):
            if s[r] not in charPos:
                charPos[s[r]] = r
                maxLength = max(maxLength, r - l + 1)
                r += 1
            else: 
                getPos = charPos[s[r]]
                while l <= getPos:
                    del charPos[s[l]]
                    l += 1

        return maxLength