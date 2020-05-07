from typing import List

from exercise.myUtils import count_time


class Solution:
    @count_time
    def countBits(self, num: int) -> List[int]:
        # dp = [0, 1]
        # if num < 2:
        #     return dp[:num + 1]
        # temp = 1
        # for i in range(2, num + 1):
        #     if i == 2 * temp:
        #         dp.append(1)
        #         temp = i
        #     else:
        #         dp.append(1 + dp[i - temp])
        # return dp
        dp = [0]
        temp = 1
        for i in range(1, num + 1):
            if i == temp:
                dp.append(1)
                temp *= 2
            else:
                dp.append(1 + dp[i - temp])
        return dp


s = Solution()
assert s.countBits(0) == [0]
assert s.countBits(2) == [0, 1, 1]
assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
s.countBits(10000000)
#2160
#1850