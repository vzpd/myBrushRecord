from typing import List

from exercise.getlargestRectangleAreaTestCase import getLargestRectangleAreaTestCase
from exercise.myUtils import timer

# 单调栈
class Solution:
    @timer
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maxArea = 0
        # for i in range(len(heights)):
        #     minheight = float('inf')
        #     for j in range(i, -1, -1):
        #         minheight = min(minheight, heights[j])
        #         area = (i - j + 1) * minheight
        #         maxArea = max(maxArea, area)
        # return maxArea
        # maxArea = 0
        # dp = [[-1, 0, float('inf')]]
        # for i in range(len(heights)):
        #     start = i
        #     while dp and dp[-1][1] >= heights[i]:
        #         start = dp.pop(-1)[0]
        #     dp.append([start, heights[i], (i - start) * heights[i]])
        #     for j in range(len(dp) - 1, 0, -1):
        #         dp[j][2] += dp[j][1]
        #         maxArea = max(maxArea, dp[j][2])
        # return maxArea
        l = len(heights)
        maxArea = 0
        index = []
        for i in range(l):
            start = None
            while index and index[-1][0] >= heights[i]:
                maxArea = max(maxArea, (i - index[-1][1]) * index[-1][0])
                start = index.pop(-1)[1]

            index.append([heights[i], start if start is not None else i])

        for x in index:
            maxArea = max(maxArea, (l - x[1]) * x[0])

        return maxArea


s = Solution()
assert s.largestRectangleArea([2, 1, 2]) == 3
assert s.largestRectangleArea([0, 1]) == 1
assert s.largestRectangleArea([0, 1, 2]) == 2
assert s.largestRectangleArea([0, 1, 2, 3]) == 4
assert s.largestRectangleArea([0, 1, 2, 3]) == 4
assert s.largestRectangleArea([0, 1, 2, 3, 4]) == 6
assert s.largestRectangleArea([0, 1, 2, 3, 4, 5]) == 9
assert s.largestRectangleArea([1, 2, 3, 4, 5, 6]) == 12
assert s.largestRectangleArea([1, 2, 3, 4, 5, 6, 7, 8]) == 20
assert s.largestRectangleArea([1, 2, 3, 4, 5]) == 9
assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
assert s.largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0]) == 20
assert s.largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]) == 10
assert s.largestRectangleArea([9, 1, 0, 5, 6, 3, 9, 3, 5, 8, 9, 0, 6, 4]) == 24
assert s.largestRectangleArea([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 12
assert s.largestRectangleArea([4, 3, 5, 5, 9, 2, 8, 4, 7, 2, 3, 8, 3, 5, 4, 7, 9]) == 34

assert s.largestRectangleArea(getLargestRectangleAreaTestCase()) == 100000000
