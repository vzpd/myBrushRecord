"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
通过次数144,870提交次数191,367
"""
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        temp = self.generateParenthesis(n - 1)
        res = set()
        for x in temp:
            for i in range(len(x)):
                res.add(x[:i] + '()' + x[i:])
            res.add('(' + x + ')')
        return res


s = Solution()
assert s.generateParenthesis(1)
assert s.generateParenthesis(2)
assert s.generateParenthesis(3)
assert s.generateParenthesis(4)
assert s.generateParenthesis(5)
