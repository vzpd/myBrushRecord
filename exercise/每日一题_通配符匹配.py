"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false
"""
import collections

from exercise.myUtils import timer


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        dict = collections.defaultdict(set)
        for i in range(len(s)):
            dict[s[i]].add(i)
        dp = set([-1])
        for i in range(len(p)):
            if p[i] == '*':
                temp = set(range(min(dp), len(s)))
            elif p[i] == '?':
                temp = set([index + 1 for index in dp if index + 1 < len(s)])
            else:
                temp = set([index + 1 for index in dp if index + 1 in dict[p[i]]])

            if not temp:
                return False
            elif len(s) - 1 in temp and i == len(p) - 1:
                return True

            dp = temp

        return False



s = Solution()
assert s.isMatch(s="adceb", p="*a*b") is True
assert s.isMatch(s="acdcb", p="a*c?b") is False
assert s.isMatch(s="aa", p="a") is False
assert s.isMatch(s="a", p="") is False
assert s.isMatch(s="aa", p="") is False
assert s.isMatch(s="", p="*") is True
assert s.isMatch(s="", p="") is True
assert s.isMatch(s="", p="*a") is False
assert s.isMatch(s="", p="**") is True
assert s.isMatch(s="", p="?") is False
assert s.isMatch(s="", p="a?") is False
assert s.isMatch(s="a", p="*?") is True
assert s.isMatch(s="a", p="*") is True
assert s.isMatch(s="aa", p="a?") is True
assert s.isMatch(s="aa", p="?a") is True
assert s.isMatch(s="aa", p="*") is True
assert s.isMatch(s="cb", p="?a") is False
assert s.isMatch('abcdef', '*') is True
assert s.isMatch('abcdef', '**') is True
assert s.isMatch('abcdef', '*a*') is True
assert s.isMatch('abcdef', '*f*') is True
assert s.isMatch('abcdef', 'abcdef*') is True
assert s.isMatch('abcdef', '*abcdef*') is True
assert s.isMatch('abcdef', '*abc*def*') is True
assert s.isMatch('abcdef', '*ab*c*def*') is True
