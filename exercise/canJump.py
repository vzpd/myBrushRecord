# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
from typing import List

from exercise.myUtils import count_time


class Solution:
    @count_time
    def canJump(self, nums: List[int]) -> bool:
        # length = len(nums)
        # currIndex = length - 1
        # while currIndex != 0:
        #     tempIndex = currIndex
        #     for i in range(currIndex - 1, -1, -1):
        #         if i + nums[i] >= currIndex:
        #             tempIndex = i
        #             break
        #     if tempIndex == currIndex:
        #         return False
        #     if tempIndex == 0:
        #         return True
        #     currIndex = tempIndex
        # return True

        # length = len(nums)
        # currIndex, maxIndex = 0, nums[0]
        # while currIndex < length - 1:
        #     if maxIndex >= length - 1:
        #         return True
        #     tempIndex = currIndex
        #     for i in range(currIndex + 1, min(maxIndex + 1, length)):
        #         if nums[i] + i > maxIndex:
        #             currIndex = i
        #             maxIndex = nums[i] + i
        #     if tempIndex == currIndex:
        #         return False
        # return True

        # length = len(nums)
        # maxIndex = nums[0]
        # for i in range(length):
        #     if i > maxIndex:
        #         return False
        #     maxIndex = max(maxIndex, i + nums[i])
        #
        # if maxIndex >= length - 1:
        #     return True
        # else:
        #     return False

        length = len(nums)
        if length < 2 or 0 not in nums:
            return True
        else:
            # for i in range(length - 2, -1, -1):
            #     if nums[i] == 0:
            #         for j in range(i):
            #             if j + nums[j] > i:
            #                 break
            #         else:
            #             return False
            i = length - 2
            for i in range(length - 2, -1, -1):
                if nums[i] == 0:
                    for j in range(i-1,-1,-1):
                        if j + nums[j] > i:
                            break
                    else:
                        return False

            return True


# 注意！！！
# 此题中0是特殊数字
# 如果数组中没有0存在，则一定可以到达最后一个位置
# 如果存在0，则只需判断能否到达所有0所在的位置

s = Solution()
assert s.canJump([2]) == True
assert s.canJump([0, 2]) == False
assert s.canJump([1, 1, 0, 1]) == False
assert s.canJump([2, 0]) == True
assert s.canJump([3, 0, 8, 2, 0, 0, 1]) == True
assert s.canJump([1, 1]) == True
assert s.canJump([1, 1, 1]) == True
assert s.canJump([3, 1, 0, 2, 3]) == True
assert s.canJump([2, 3, 1, 1, 4]) == True
assert s.canJump([3, 2, 1, 0, 4]) == False
assert s.canJump([2, 2, 2]) == True
assert s.canJump(
    [1, 2, 2, 6, 3, 6, 1, 8, 9, 4, 7, 6, 5, 6, 8, 2, 6, 1, 3, 6, 6, 6, 3, 2, 4, 9, 4, 5, 9, 8, 2, 2, 1, 6, 1, 6, 2, 2,
     6, 1, 8, 6, 8, 3, 2, 8, 5, 8, 0, 1, 4, 8, 7, 9, 0, 3, 9, 4, 8, 0, 2, 2, 5, 5, 8, 6, 3, 1, 0, 2, 4, 9, 8, 4, 4, 2,
     3, 2, 2, 5, 5, 9, 3, 2, 8, 5, 8, 9, 1, 6, 2, 5, 9, 9, 3, 9, 7, 6, 0, 7, 8, 7, 8, 8, 3, 5, 0]) == True
