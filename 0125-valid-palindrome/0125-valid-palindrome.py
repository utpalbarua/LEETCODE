class Solution:
    def isPalindrome(self, s: str) -> bool:

        str1 = "".join([char for char in s if char.isalnum()])
        str1 = str1.lower()
        str2 = str1[::-1]

        return str1 == str2

        