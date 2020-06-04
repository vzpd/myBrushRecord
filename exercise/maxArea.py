# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#  
#
# 示例：
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def maxArea(self, height: List[int]) -> int:
        # length = len(height)
        # if length < 2:
        #     return 0
        # begin, end = 0, length - 1
        # maxArea = min(height[begin], height[end]) * (end - begin)
        # while begin < end:
        #     minHeight = min(height[begin], height[end])
        #     while begin < end and minHeight >= min(height[begin], height[end]):
        #         if height[begin] > height[end]:
        #             end -= 1
        #         else:
        #             begin += 1
        #     maxArea = max(maxArea, min(height[begin], height[end]) * (end - begin))
        # return maxArea
        i, j = 0, len(height) - 1
        maxArea, tempArea = 0, 0
        for k in range(len(height) - 1):
            if height[i] < height[j]:
                tempArea = (j - i) * height[i]
                i += 1
            else:
                tempArea = (j - i) * height[j]
                j -= 1
            maxArea = max(maxArea, tempArea)
        return maxArea


s = Solution()
assert s.maxArea([]) == 0
assert s.maxArea([1]) == 0
assert s.maxArea([1, 8]) == 1
assert s.maxArea([1, 2, 3]) == 2
assert s.maxArea([1, 1, 1, 1]) == 3
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
