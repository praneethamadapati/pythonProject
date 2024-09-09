class Solution:
    def isPalindrome(s: str) -> bool:

        for char in s:
            char.lower() if char.isalnum() else '#'
        s = ''.join(s)
        print(s)
        return s == s[::-1]

    s = "A man, a plan, a canal: Panama"
    isPalindrome(s)