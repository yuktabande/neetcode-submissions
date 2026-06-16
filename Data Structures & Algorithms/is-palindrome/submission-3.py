class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''
        for letter in s:
            if letter.isalnum():
                c += letter.lower()
        return c == c[::-1]