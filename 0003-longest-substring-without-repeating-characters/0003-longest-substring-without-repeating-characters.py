class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r, maxLength = 0, 0, 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength