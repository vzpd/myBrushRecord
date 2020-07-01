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
"""

"""
子数组：元素相同，个数相同，顺序相同
子序列：元素相同，个数相同，顺序不一定相同

此题二种解法：
    1、动态规划
    2、滑动窗口
"""
import collections
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dict = collections.defaultdict(list)
        # for i in range(len(A)):
        #     dict[A[i]].append(i)
        #
        # maxl = 0
        # downdp = [0] * (len(A) + 1)
        # for i in range(len(B)):
        #     tempdowndp = [0] * (len(A) + 1)
        #     for x in dict[B[i]]:
        #         tempdowndp[x + 1] = downdp[x] + 1
        #         maxl = max(maxl, tempdowndp[x + 1])
        #     downdp = tempdowndp
        # return maxl
        maxl = 0

        def getl(a, b):
            nonlocal maxl
            length = min(len(a), len(b))
            l = 0
            for i in range(length):
                if a[i] == b[i]:
                    l += 1
                else:
                    maxl = max(maxl, l)
                    l = 0
            maxl = max(maxl, l)

        for i in range(len(A)):
            getl(A[i:], B)
        for i in range(len(B)):
            getl(A, B[i:])

        return maxl


s = Solution()
assert s.findLength([1, 2], [1, 2]) == 2
assert s.findLength([69, 51, 94, 52, 72, 74, 65, 65, 99, 1], [65, 99, 82, 27, 43, 95, 9, 20, 13, 99]) == 2
assert s.findLength([1, 2, 3, 4, 1], [3, 2, 1, 4, 7]) == 1
assert s.findLength([1], [1]) == 1
assert s.findLength([1], [2]) == 0
assert s.findLength([1, 2], [2, 1]) == 1
assert s.findLength([1, 2, 3], [1, 2, 3]) == 3
assert s.findLength([1, 2, 3], [3, 2, 1]) == 1
assert s.findLength([1, 2, 3], [1, 3, 2]) == 1
assert s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
