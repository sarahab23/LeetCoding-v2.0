class Solution:
    def alphaNum(self, c):
            return (ord('0') <= ord(c) <= ord('9')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z'))
            
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while low < high:
            if not self.alphaNum(s[low]):
                low += 1
                continue
            if not self.alphaNum(s[high]):
                high -= 1
                continue
            if s[low].lower() == s[high].lower():
                low += 1
                high -= 1
            else:
                return False

        return True