class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True
        s = "".join(char.lower() for char in s if char.isalnum())
        reverse_s = s[::-1]
        print(s)
        print(reverse_s)
        return s == reverse_s