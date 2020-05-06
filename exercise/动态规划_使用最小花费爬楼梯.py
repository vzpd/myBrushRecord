from typing import List


# f(i) = min( f(i-1), f(i-2) + cost[i])
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepPreTwo = cost[0]
        stepPreOne = cost[1]
        for i in range(2, len(cost)):
            stepPreTwo, stepPreOne, = stepPreOne, min(stepPreOne, stepPreTwo) + cost[i]
        return min(stepPreTwo, stepPreOne)


s = Solution()
assert s.minCostClimbingStairs([10, 15, 20]) == 15
assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
