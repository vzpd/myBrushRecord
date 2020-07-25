from functools import lru_cache
from math import ceil
from typing import List

from exercise.myUtils import timer

"""
二分法
l、r分别为nums中的最大值和nums所有数字只和
然后用二分法，找出l-r中最小的符合要求的数字
"""
class Solution:
    @timer
    def splitArray(self, nums: List[int], m: int) -> int:
        # nums = [0] + nums
        # pre = [nums[0]]
        # for i in range(1, len(nums)):
        #     pre.append(pre[-1] + nums[i])
        # if m == 1:
        #     return pre[-1]
        # l = len(nums)
        # dict = {}
        #
        # def next(i, k):
        #     if (i, k) in dict:
        #         return dict[(i, k)]
        #     if k == 1:
        #         return pre[-1] - pre[i - 1]
        #     r = float('inf')
        #     k -= 1
        #     for j in range(i + 1, l - k + 1):
        #         combo = max(pre[j - 1] - pre[i - 1], next(j, k))
        #         r = min(r, combo)
        #     dict[(i, k + 1)] = r
        #     return r
        #
        # return next(1, m)
        l, r = max(nums), sum(nums)

        def test(mid):
            count = 0
            i = 0
            temp = 0
            while i < len(nums):
                if nums[i] + temp <= mid:
                    temp += nums[i]
                    i += 1
                else:
                    count += 1
                    temp = 0
                    if count == m:
                        return False
            return True

        while l < r:
            mid = (l + r ) // 2
            if test(mid):
                r = mid
            else:
                l = mid+1

        return l


s = Solution()
assert s.splitArray(nums=[7, 2, 5, 10, 8], m=2) == 18
assert s.splitArray([10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8], 8)
assert s.splitArray([2, 3, 5, 3, 2, 4, 6, 8, 6, 5, 3, 6], 5) == 13
assert s.splitArray([1, 2147483647], 2) == 2147483647
assert s.splitArray([4, 6, 3, 2, 1, 5, 6, 7, 5, 3, 2, 4, 6, 7, 5, 4, 3], 10) == 10
