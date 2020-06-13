class Solution:
    def validPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1
        while s[a] == s[b] and a < b:
            a += 1
            b -= 1
        if a == b:
            return True
        elif s[a + 1:b + 1] == s[a + 1:b + 1][::-1]:
            return True
        elif s[a:b] == s[a:b][::-1]:
            return True
        else:
            return False


s = Solution()
assert s.validPalindrome('acdcac') is True
assert s.validPalindrome('abca') is True
assert s.validPalindrome('a') is True
assert s.validPalindrome('abaa') is True
assert s.validPalindrome('aba') is True
assert s.validPalindrome('abac') is True
