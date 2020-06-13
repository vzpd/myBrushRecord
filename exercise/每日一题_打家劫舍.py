from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for i in range(len(nums)):
            dp.append(max(dp[-1], dp[-2] + nums[i]))
        return dp[-1]


s = Solution()
assert s.rob([1]) == 1
assert s.rob([1, 2]) == 2
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
