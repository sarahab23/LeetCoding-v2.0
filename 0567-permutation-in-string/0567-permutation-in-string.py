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
            if countS1[i] == permut[i]:
                match += 1
        
        if match == 26: return True

        while r < len(s2):

            if countS1[ord(s2[r]) - ord('a')] == permut[ord(s2[r]) - ord('a')]:
                permut[ord(s2[r]) - ord('a')] += 1
                match -= 1
            else:
                permut[ord(s2[r]) - ord('a')] += 1
                if countS1[ord(s2[r]) - ord('a')] == permut[ord(s2[r]) - ord('a')]: match += 1

            r += 1

            if countS1[ord(s2[l]) - ord('a')] == permut[ord(s2[l]) - ord('a')]:
                permut[ord(s2[l]) - ord('a')] -= 1
                match -= 1
            else:
                permut[ord(s2[l]) - ord('a')] -= 1    
                if countS1[ord(s2[l]) - ord('a')] == permut[ord(s2[l]) - ord('a')]: match += 1
            
            l += 1
            if match == 26: return True
        
        return False
