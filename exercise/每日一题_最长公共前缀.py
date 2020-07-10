# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if not strs:
        #     return ''
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     l = min(len(prefix), len(strs[i]))
        #     j = 0
        #     while j < l and prefix[j] == strs[i][j]:
        #         j += 1
        #     prefix = prefix[:j]
        #     if j == 0:
        #         return ''
        # return prefix
        res = ''
        for x in zip(*strs):
            if len(set(x)) == 1:
                res += x[0]
        return res


s = Solution()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ''
