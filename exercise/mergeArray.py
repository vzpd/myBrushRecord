# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        # intervals.sort()
        # length = len(intervals)
        # temp = [intervals[0]]
        # for i in range(1, length):
        #     if temp[-1][1] < intervals[i][0]:
        #         temp.append(intervals[i])
        #     elif intervals[i][0] <= temp[-1][1] <= intervals[i][1]:
        #         temp[-1][1] = intervals[i][1]
        intervals.sort(key=lambda x: x[1])
        length = len(intervals)
        for i in range(length - 1, 0, -1):
            if intervals[i - 1][0] <= intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = intervals[i][1]
                intervals.pop(i)
            elif intervals[i - 1][0] > intervals[i][0]:
                intervals.pop(i - 1)

        return intervals


s = Solution()
assert s.merge([[1, 2], [4, 5]]) == [[1, 2], [4, 5]]
assert s.merge([[]]) == [[]]
assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
assert s.merge([[1, 1], [1, 1], [1, 1]]) == [[1, 1]]
assert s.merge([[1, 6]]) == [[1, 6]]
assert s.merge([[1, 6], [3, 4], [5, 6]]) == [[1, 6]]
assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert s.merge([[1, 4], [3, 5]]) == [[1, 5]]
