# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.upper()
        # vchr = set([chr(i) for i in range(65, 91)] + [str(i) for i in range(10)])
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if s[l] in vchr and s[r] in vchr:
        #         if s[l] != s[r]:
        #             return False
        #         r -= 1
        #         l += 1
        #     elif s[l] in vchr:
        #         r -= 1
        #     else:
        #         l += 1
        #
        # return True
        sgood = [x.lower() for x in s if x.isalnum()]
        return sgood == sgood[::-1]


s = Solution()
assert s.isPalindrome('A man, a plan, a canal: Panama') is True
assert s.isPalindrome('race a car') is False
assert s.isPalindrome('0P') is False
