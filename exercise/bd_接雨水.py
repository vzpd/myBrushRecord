# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
from functools import reduce
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # i, j, volume = 0, len(height) - 1, 0
        # while i < j:
        #     minHeight = min(height[i], height[j])
        #     for k in range(i + 1, j):
        #         if height[k] < minHeight:
        #             volume += minHeight - height[k]
        #             height[k] = minHeight
        #
        #     while i < j and height[i] == minHeight:
        #         i += 1
        #     while i < j and height[j] == minHeight:
        #         j -= 1
        # return volume
        heightLen = len(height)
        i, volume = 0, 0
        while i < heightLen - 2:
            currentHeight = height[i]
            dp = [0]
            maxHeigth, nextStep = 0, i
            for j in range(i + 1, heightLen):
                if height[j] > currentHeight:
                    nextStep = j
                    break
                else:
                    dp.append(height[j])
                    if height[j] >= maxHeigth:
                        maxHeigth = height[j]
                        nextStep = j
            maxHeigth = min(height[i], height[nextStep])
            if len(dp[:nextStep - i]) > 0:
                volume += reduce(lambda x, y: x + maxHeigth - y, dp[:nextStep - i])
            i = nextStep

        return volume


s = Solution()
assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert s.trap([]) == 0
assert s.trap([1]) == 0
assert s.trap([0, 0]) == 0
assert s.trap([0, 1, 0]) == 0
assert s.trap([0, 1, 1, 0]) == 0
assert s.trap([0, 1, 1, 0, 10]) == 1
