from exercise.myUtils import timer


class Solution:
    @timer
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp = {(0, 0, 0)}
        # while dp:
        #     print('-----------', dp)
        #     if (len(s1), len(s2), len(s3)) in dp:
        #         return True
        #     temp = set()
        #     for i, j, k in dp:
        #         x = 0
        #         while i + x < len(s1) and k + x < len(s3) and s1[i + x] == s3[k + x]:
        #             temp.add((i + x + 1, j, k + x + 1))
        #             print('{0} -> {1}'.format((i, j, k), (i + x + 1, j, k + x + 1)))
        #             x += 1
        #
        #         y = 0
        #         while j + y < len(s2) and k + y < len(s3) and s2[j + y] == s3[k + y]:
        #             temp.add((i, j + y + 1, k + y + 1))
        #             print('{0} -> {1}'.format((i, j, k), (i, j + y + 1, k + y + 1)))
        #             y += 1
        #
        #     dp = temp
        #
        # return False
        if len(s1) + len(s2) != len(s3):
            return False
        col = len(s2) + 1
        row = len(s1) + 1
        dp = [[False] * col for _ in range(row)]
        dp[0][0] = True
        for i in range(row):
            for j in range(col):
                if i > 0:
                    dp[i][j] |= s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                if j > 0:
                    dp[i][j] |= s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
assert s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
assert s.isInterleave('', '', '') is True
assert s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
