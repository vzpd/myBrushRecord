class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(2, n + 1):
            b, a = a + b, b
        return b


s = Solution()
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
