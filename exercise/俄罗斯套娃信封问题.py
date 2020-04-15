# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 说明:
# 不允许旋转信封。
#
# 示例:
#
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # dp = []
        # for i in range(len(envelopes)):
        #     maxval = 0
        #     for j in range(len(dp) - 1, -1, -1):
        #         if dp[j][1] < envelopes[i][1]:
        #             maxval = j + 1
        #             break
        #     if len(dp) > maxval:
        #         if dp[maxval][1] > envelopes[i][1]:
        #             dp[maxval] = envelopes[i]
        #     else:
        #         dp.append(envelopes[i])
        # return len(dp)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, y in envelopes:
            index = bisect.bisect_left(dp, y)
            dp[index:index + 1] = [y]
        return len(dp)


s = Solution()

assert s.maxEnvelopes([[30, 50], [12, 2], [3, 4], [12, 15]]) == 3

assert s.maxEnvelopes(
    [[15, 8], [2, 20], [2, 14], [4, 17], [8, 19], [8, 9], [5, 7], [11, 19], [8, 11], [13, 11], [2, 13], [11, 19],
     [8, 11], [13, 11], [2, 13], [11, 19], [16, 1], [18, 13], [14, 17], [18, 19]]) == 5

assert s.maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]) == 5

assert s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3

assert s.maxEnvelopes([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]) == 3

assert s.maxEnvelopes([[5, 4]]) == 1
assert s.maxEnvelopes([[5, 4]]) == 1

assert s.maxEnvelopes(
    [[31, 49], [31, 45], [37, 7], [12, 2], [46, 18], [44, 10], [9, 36], [47, 44], [32, 45], [18, 18], [34, 7], [23, 28],
     [28, 12], [6, 33], [21, 33], [30, 18], [28, 31], [43, 41], [47, 19], [18, 50], [12, 5], [29, 10], [22, 13],
     [17, 21], [18, 38], [28, 46], [41, 1], [49, 21], [48, 5], [40, 21], [20, 39], [27, 13], [15, 23], [28, 48],
     [36, 44], [18, 7], [46, 32], [9, 41], [22, 34], [49, 35], [49, 34], [22, 3], [47, 46], [39, 25], [29, 39],
     [29, 39], [37, 11], [41, 49], [37, 12], [34, 1]]) == 8
