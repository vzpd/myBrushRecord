# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        dp, maxRight = {}, 0
        for i in range(len(intervals)):
            maxRight = max(maxRight, intervals[i][1])
            dp[i] = maxRight
        for i in range(len(intervals) - 1, 0, -1):
            if dp[i - 1] >= intervals[i][1]:
                intervals.pop(i)
            else:
                if dp[i - 1] >= intervals[i][0]:
                    intervals[i - 1][1] = intervals[i][1]
                    intervals.pop(i)
        return intervals


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         ret = []
#         for i in range(len(intervals)):
#             itv = intervals[i]
#             if not ret or itv[0] > ret[-1][-1]:
#                 ret.append(itv)
#             elif itv[0] <= ret[-1][1] <= itv[1]:
#                 ret[-1][-1] = itv[1]
#         return ret


s = Solution()
assert s.merge([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]) == [[2, 4], [5, 5]]
assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert s.merge([[1, 4], [1, 4]]) == [[1, 4]]
assert s.merge([[1, 4], [2, 3]]) == [[1, 4]]
assert s.merge([[4, 5]]) == [[4, 5]]
assert s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
