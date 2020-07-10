"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""
from exercise.myUtils import timer


class Solution:
    @timer
    def longestValidParentheses(self, s: str) -> int:
        # left = 0
        # leftindex = [-1]
        # maxl = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         left += 1
        #         leftindex.append(i)
        #     else:
        #         if left:
        #             left -= 1
        #             leftindex.pop(-1)
        #             count = i - leftindex[-1]
        #             maxl = max(maxl, count)
        #         else:
        #             leftindex[-1] = i
        #
        # return maxl
        leftindex = [-1]
        maxl = 0
        for i in range(len(s)):
            if s[i] == '(':
                leftindex.append(i)
            else:
                leftindex.pop(-1)
                if leftindex:
                    maxl = max(maxl, i - leftindex[-1])
                else:
                    leftindex.append(i)

        return maxl


s = Solution()
# assert s.longestValidParentheses(')()()())()()(())()(())()))(()())()((())') == 16
assert s.longestValidParentheses(')()())') == 4
assert s.longestValidParentheses("()(()") == 2
assert s.longestValidParentheses('') == 0
assert s.longestValidParentheses('(') == 0
assert s.longestValidParentheses(')') == 0
assert s.longestValidParentheses(')(') == 0
assert s.longestValidParentheses(')()') == 2
assert s.longestValidParentheses('(()') == 2
assert s.longestValidParentheses(')()(') == 2
assert s.longestValidParentheses('(()') == 2
assert s.longestValidParentheses('()(()))()())') == 6
assert s.longestValidParentheses(')()())(') == 4
assert s.longestValidParentheses('((()))()((') == 8
