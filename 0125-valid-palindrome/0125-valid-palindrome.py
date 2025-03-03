class Solution:
    def alphaNum(self, c):
            return (ord('0') <= ord(c) <= ord('9')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z'))

    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        while low < high:
            while low < high and not self.alphaNum(s[low]):
                low += 1
            while low < high and not self.alphaNum(s[high]):
                high -= 1
            if s[low].lower() == s[high].lower():
                low, high = low + 1, high - 1
            else:
                return False

        return True