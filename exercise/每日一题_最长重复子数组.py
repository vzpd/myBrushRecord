import collections
from typing import List

from exercise.myUtils import timer

"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

注意:子序列->长度相同，元素相同，顺序可以不一致，下面的第一个求的是子序列
     子数组->长度相同，元素相同，顺序相反,下面第二个求的是子数组
"""


class Solution:
    @timer
    def findLength(self, A: List[int], B: List[int]) -> int:
        dict = collections.defaultdict(list)
        for i in range(len(A)):
            dict[A[i]].append(i)

        temp = [dict[x] for x in B]

        gap = -1
        for i in range(len(temp)):
            if not temp[i]:
                gap = i
            for j in range(len(temp[i]) - 1, -1, -1):
                if temp[i][j] <= gap:
                    temp[i].pop(j)

        gap = len(temp)
        for i in range(len(temp) - 1, -1, -1):
            if not temp[i]:
                gap = i
            for j in range(len(temp[i]) - 1, -1, -1):
                if temp[i][j] >= gap:
                    temp[i].pop(j)

        maxl = 0
        l = 0
        for i in range(len(temp)):
            if temp[i]:
                l += 1
                maxl = max(maxl, l)
            else:
                l = 0

        return maxl


class Solution:
    @timer
    def findLength(self, A: List[int], B: List[int]) -> int:
        maxl = 0
        for i in range(len(A)):
            for j in range(len(B)):
                l = min(len(A) - i, len(B) - j)
                for k in range(1, l + 1):
                    if A[i:i + l] == B[j:j + l] or A[i:i + l] == B[j:j + l:-1]:
                        maxl = max(maxl, l)
        return maxl


s = Solution()
assert s.findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]) == 4
assert s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
assert s.findLength([1], [3]) == 0
assert s.findLength([3], [3]) == 1
assert s.findLength([3], [3, 2]) == 1
assert s.findLength([3, 2], [3, 2]) == 2
assert s.findLength([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 8, 5, 6, 7, 8]) == 3
