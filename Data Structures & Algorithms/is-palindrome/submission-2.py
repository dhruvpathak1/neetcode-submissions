class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for i in s:
            if i.isalnum():
                s2 += i
        s2 = s2.lower()
        t = s2[::-1]
        return s2 == t
        