from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = nums[0]
        tempRes = nums[0]
        for i in range(1, len(nums)):
            tempRes = tempRes + nums[i] if tempRes > 0 else nums[i]
            maxRes = max(maxRes, tempRes)
        return maxRes


s = Solution()
assert s.maxSubArray([-1]) == -1
assert s.maxSubArray([-1, 1]) == 1
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
