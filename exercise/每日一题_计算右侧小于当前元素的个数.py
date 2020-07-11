"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
"""
import bisect
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def countSmaller(self, nums: List[int]) -> List[int]:
        # if not nums:
        #     return []
        # ans = [0]
        # temp = [nums[-1]]
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] > temp[-1]:
        #         ans.insert(0, len(temp))
        #         temp.insert(len(temp), nums[i])
        #     elif nums[i] <= temp[0]:
        #         ans.insert(0, 0)
        #         temp.insert(0, nums[i])
        #     else:
        #         index = bisect.bisect_left(temp, nums[i])
        #         ans.insert(0, index)
        #         temp.insert(index, nums[i])
        # return ans
        cnums = sorted(nums)
        temp = [bisect.bisect_left(cnums, x) + 1 for x in nums]
        c = [0] * (len(nums) + 1)

        def lowbit(n):
            return n & (-n)

        def query(n):
            sum = 0
            while n > 0:
                sum += c[n]
                n -= lowbit(n)
            return sum

        def add(n):
            while n < len(c):
                c[n] += 1
                n += lowbit(n)

        ans = [0] * len(nums)
        for i in range(len(temp) - 1, -1, -1):
            ans[i] = query(temp[i] - 1)
            add(temp[i])

        return ans


s = Solution()
assert s.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
assert s.countSmaller([3, 2, 2]) == [2, 0, 0]
assert s.countSmaller([1]) == [0]
assert s.countSmaller([1, 2]) == [0, 0]
assert s.countSmaller([2, 1]) == [1, 0]
assert s.countSmaller([3, 2, 1]) == [2, 1, 0]
assert s.countSmaller([8, 5, 4, 3, 6]) == [4, 2, 1, 0, 0]
assert s.countSmaller([5, 2, 6, 1, 11, 3, 2, 5, 3, 6]) == [5, 1, 5, 0, 5, 1, 0, 1, 0, 0]
