from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCount = max(candies) - extraCandies
        return [x >= maxCount for x in candies]


s = Solution()
assert s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]
assert s.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1) == [True, False, False, False, False]
assert s.kidsWithCandies(candies=[12, 1, 12], extraCandies=10) == [True, False, True]
