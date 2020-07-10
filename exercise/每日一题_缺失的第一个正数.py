"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

 

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
 

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def firstMissingPositive(self, nums: List[int]) -> int:
        # temp = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         temp.append(nums[i])
        # temp.sort()
        # temp = [0] + temp
        # for i in range(len(temp) - 1):
        #     if temp[i + 1] > temp[i] + 1:
        #         return temp[i] + 1
        # else:
        #     return temp[-1] + 1
        nums += [0]
        l = len(nums)

        def swap(num):
            temp = nums[num]
            nums[num] = num
            if 0 < temp < l and temp != num:
                swap(temp)

        for i in range(len(nums)):
            if 0 < nums[i] < l and nums[i] != i:
                temp = nums[i]
                nums[i] = 0
                swap(temp)

        for i in range(1, len(nums)):
            if nums[i] < 1 or nums[i] >= l:
                return i
        else:
            return l


s = Solution()
assert s.firstMissingPositive([0, 3]) == 1
assert s.firstMissingPositive([4, 3, 4, 1, 1, 4, 1, 4]) == 2
assert s.firstMissingPositive([2, 2]) == 1
assert s.firstMissingPositive([1, 2, 0]) == 3
assert s.firstMissingPositive([3, 4, -1, 1]) == 2
assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1
assert s.firstMissingPositive([1, 2, 2, 3]) == 4
assert s.firstMissingPositive([-1, -1, 2]) == 1
assert s.firstMissingPositive([1, 2, 3]) == 4
