class Solution:
    def divisorGame(self, N: int) -> bool:
        # dp = [False, False]
        # for i in range(2, N + 1):
        #     for j in range(1, i // 2 + 1):
        #         if i % j == 0:
        #             if dp[i - j] is False:
        #                 dp.append(True)
        #                 break
        #     else:
        #         dp.append(False)
        #
        # return dp[-1]
        return N % 2 == 0


s = Solution()
assert s.divisorGame(2) is True
assert s.divisorGame(3) is False
