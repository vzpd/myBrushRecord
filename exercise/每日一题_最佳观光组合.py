# 1014.
# 最佳观光组合
# 给定正整数数组
# A，A[i]
# 表示第
# i
# 个观光景点的评分，并且两个景点
# i
# 和
# j
# 之间的距离为
# j - i。
#
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
#
# 返回一对观光景点能取得的最高分。
#
# 示例：
#
# 输入：[8, 1, 5, 2, 6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
#
# 提示：
#
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # temp1 = [float('-inf')]
        # for i in range(len(A) - 1, -1, -1):
        #     temp1.insert(0, max(temp1[0], A[i] - i))
        #
        # maxv = 0
        # for i in range(len(A) - 1):
        #     maxv = max(maxv, A[i] + temp1[i + 1] + i)
        #
        # return maxv
        # maxv = 0
        # maxl = A[0]
        # maxindex = 0
        # l = len(A)
        # for i in range(1, l):
        #     maxv = max(maxv, maxl + A[i] + maxindex - i)
        #     if A[i] >= maxl - i + maxindex:
        #         maxl = A[i]
        #         maxindex = i
        # return maxv
        # 将部分循环中的计算移动到初始值中
        maxv = 0
        maxl = A[0]
        l = len(A)
        for i in range(1, l):
            maxv = max(maxv, maxl + A[i] - i)
            if A[i] + i >= maxl:
                maxl = A[i] + i
        return maxv


s = Solution()
assert s.maxScoreSightseeingPair([4, 7, 5, 8]) == 13
assert s.maxScoreSightseeingPair([7, 2, 6, 6, 9, 4, 3]) == 14
assert s.maxScoreSightseeingPair([1, 3, 5]) == 7
assert s.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
