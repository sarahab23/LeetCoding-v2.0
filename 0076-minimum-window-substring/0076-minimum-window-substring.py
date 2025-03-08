class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, have, res = 0, 0, 0, ""
        countT, window = {},{}

        for c in t: countT[c] = 1 + countT.get(c, 0)
        need = len(countT)

        while r < len(s):
            if s[r] in countT: 
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == countT[s[r]]: have += 1
            while need == have:
                if res == "" or len(res) > (r - l + 1):
                    res = s[l:r + 1]
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] + 1 == countT[s[l]]: have -= 1
                l += 1
            r += 1

        return res