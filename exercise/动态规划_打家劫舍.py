from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return max(nums + [0])
        dp = [nums[0], max(nums[:2])]
        for i in range(2, length):
            dp.append(max(nums[i] + dp[-2], dp[-1]))
        return dp[-1]


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
assert s.rob([2, 1, 1, 2]) == 4
