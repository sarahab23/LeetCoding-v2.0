class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        lengthS1 = len(s1)
        l, match, r = 0, 0, lengthS1
        countS1, permut = [0] * 26, [0] * 26

        for i in range(lengthS1):
            countS1[ord(s1[i]) - ord('a')] += 1
            permut[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            match += (1 if countS1[i] == permut[i] else 0)


        while r < len(s2):
            if match == 26: return True

            indexR = ord(s2[r]) - ord('a')
            permut[indexR] += 1
            if countS1[indexR] == permut[indexR]: match += 1
            elif countS1[indexR] + 1 == permut[indexR]: match -= 1
            r += 1

            indexL = ord(s2[l]) - ord('a')
            permut[indexL] -= 1
            if countS1[indexL] == permut[indexL]: match += 1
            elif countS1[indexL] == permut[indexL] + 1: match -= 1             
            l += 1
        
        return match == 26
