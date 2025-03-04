class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res, maxFreq = 0, 0, 0, 0
        charCount = defaultdict(int)

        while r < len(s):
            charCount[s[r]] += 1
            maxFreq = max(maxFreq, charCount[s[r]])
            if (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res
