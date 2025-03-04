class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        length = len(s1)
        l, r = 0, length - 1
        countS1 = defaultdict(int)
        perm = defaultdict(int)

        for ch in s1:
            countS1[ch] += 1

        for i in range(r):
            perm[s2[i]] += 1

        while r < len(s2):
            perm[s2[r]] += 1
            if perm == countS1: return True
            perm[s2[l]] -= 1
            if perm[s2[l]] == 0: del perm[s2[l]]
            l += 1
            r += 1


        return False