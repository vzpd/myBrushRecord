# 由n个连接的字符串s组成字符串S，记作S = [s, n]。例如，["abc", 3] =“abcabcabc”。
#
# 如果我们可以从s2中删除某些字符使其变为
# s1，则称字符串s1可以从字符串s2获得。
# 例如，根据定义，"abc"可以从 “abdbec” 获得，但不能从 “acbbe” 获得。
#
# 现在给你两个非空字符串s1和s2（每个最多100个字符长）和两个整数0 ≤ n1 ≤ 106和1 ≤ n2 ≤ 106。现在考虑字符串S1和S2，
# 其中S1 = [s1, n1] 、S2 = [s2, n2] 。
#
# 请你找出一个可以满足使[S2, M]从S1获得的最大整数M 。
#
# 示例：
# 输入：
# s1 = "acb", n1 = 4
# s2 = "ab", n2 = 2
# 返回：
# 2
from functools import reduce


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        temp = reduce(lambda x, y: x + y, [x for x in s1 if x in s2])
        if s2 in temp:
            startIndex=temp.index(s2)
        else:
            pass


s = Solution()
assert s.getMaxRepetitions("acb", 4, 'ab', 2) == 2
assert s.getMaxRepetitions('abab', 1, 'ab', 1) == 2
assert s.getMaxRepetitions('abab', 1, 'ab', 2) == 1
assert s.getMaxRepetitions('abab', 2, 'ababa', 1) == 1
assert s.getMaxRepetitions('abab', 1, 'abab', 2) == 0
