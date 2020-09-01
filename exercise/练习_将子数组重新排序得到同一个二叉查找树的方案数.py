from math import comb
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def numOfWays(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums or len(nums) == 1:
                return 1
            start = nums[0]
            left = [x for x in nums[1:] if x < start]
            right = [x for x in nums[1:] if x > start]
            l = helper(left)
            r = helper(right)
            return l * r * comb(len(nums) - 1, len(left))

        MOD = 10 ** 9 + 7
        ans = helper(nums)

        return (ans - 1) % MOD


s = Solution()
assert s.numOfWays([2, 1, 3]) == 1
assert s.numOfWays([3, 4, 5, 1, 2]) == 5
assert s.numOfWays([1, 2, 3]) == 0
assert s.numOfWays([3, 1, 2, 5, 4, 6]) == 19
assert s.numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]) == 216212978
