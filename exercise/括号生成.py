# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例：
#
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        dp = {'()'}
        for i in range(1, n):
            temp = set()
            for x in dp:
                temp.add('(' + x + ')')
                temp.add('()' + x)
                temp.add(x + '()')
            dp = temp

        return list(dp)


s = Solution()
assert s.generateParenthesis(0) == []
assert s.generateParenthesis(1) == ['()']
assert set(s.generateParenthesis(2)) == set(['(())', '()()'])
assert set(s.generateParenthesis(3)) == set([
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
])
assert set(s.generateParenthesis(4)) == set(
    ['(()())()', '()()(())', '(((())))', '()(()())', '((()))()', '()(())()', '()()()()', '((())())', '(()()())',
     '((()()))', '()((()))', '(()(()))', '(())()()'])
print(len(s.generateParenthesis(5)))
