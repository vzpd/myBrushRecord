# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
from exercise.myUtils import timer


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if not s and not p:
        #     return True
        # i, j = 0, 0
        # # 匹配s
        # while i < len(s) and j < len(p):
        #     if j + 1 < len(p) and p[j + 1] == '*':
        #         while j + 2 < len(p) and p[j + 2] == p[j] and p[j + 3] == '*':
        #             j += 2
        #         tempi = i
        #
        #         while tempi < len(s) and (s[tempi] == p[j] or p[j] == '.'):
        #             if self.isMatch(s[tempi:], p[j + 2:]):
        #                 return True
        #             tempi += 1
        #         else:
        #             if self.isMatch(s[tempi:], p[j + 2:]):
        #                 return True
        #             return False
        #     else:
        #         if s[i] == p[j] or p[j] == '.':
        #             i += 1
        #             j += 1
        #         else:
        #             return False
        #
        # if i < len(s):
        #     return False
        #
        # # 检查有没有剩余的p
        # while j < len(p):
        #     if j + 1 < len(p) and p[j + 1] == '*':
        #         j += 2
        #     else:
        #         return False
        #
        # return True
        # 动态规划！！！
        # 使用last记录上一个字符可能的位置，当前字符从last里所有可能的位置+1开始匹配，
        # 如果匹配到则更新last
        last = set([-1])
        for i in range(len(p)):
            if p[i] == '*':
                for x in last.copy():
                    index = x + 1
                    if index in last:
                        continue
                    while index < len(s) and (s[index] == p[i - 1] or p[i - 1] == '.'):
                        last.add(index)
                        index += 1
            else:
                if not (i + 1 < len(p) and p[i + 1] == '*'):
                    temp = set()
                    for x in last:
                        index = x + 1
                        if index < len(s) and (s[index] == p[i] or p[i] == '.'):
                            temp.add(index)

                    if not temp:
                        return False
                    else:
                        last = temp

        return len(s) - 1 in last


s = Solution()
assert s.isMatch('aaa', 'ab*a*c*a') is True
assert s.isMatch('aaa', 'ab*a') is False
assert s.isMatch('ab', '.*c') is False
assert s.isMatch('aaabc', 'a*aa.c') is True
assert s.isMatch('', 'aa') is False
assert s.isMatch('', 'a*a*') is True
assert s.isMatch('', '.*') is True
assert s.isMatch('aa', 'a') is False
assert s.isMatch('aa', 'a*') is True
assert s.isMatch('ab', '.*') is True
assert s.isMatch('aab', 'c*a*b') is True
assert s.isMatch('mississippi', 'mis*is*p*.') is False
