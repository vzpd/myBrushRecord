"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""
from typing import List

"""
动态规划
第x天赚的钱为，昨天手里没有股票时的钱 和 今天卖掉昨天持有的股票时赚的钱  中比较大的那个
第x天手里持有股票时的钱为，前天卖股票赚的钱减去今天买股票花费的钱 和 昨天持有股票时手里的钱 中比较大的那个
最后最大收益为 最后一天没有持有股票时的收益
f(x) = max(f(x-1)[0],fx(x-2)[1]+price[x])
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        # x, y = [0, 0], [0, -prices[0]]
        # for i in range(1, len(prices)):
        #     temp = []
        #     a1 = y[0]
        #     a2 = y[1] + prices[i]
        #     temp.append(max(a1, a2))
        #     b1 = y[1]
        #     b2 = x[0] - prices[i]
        #     temp.append(max(b1, b2))
        #     x, y = y, temp
        # return y[0]
        if not prices:
            return 0
        dp = [[0, 0], [0, -prices[0]]]
        for i in range(1, len(prices)):
            temp = []
            a1 = dp[-1][0]
            a2 = dp[-1][1] + prices[i]
            temp.append(max(a1, a2))
            b1 = dp[-1][1]
            b2 = dp[-2][0] - prices[i]
            temp.append(max(b1, b2))
            dp.append(temp)

        return dp[-1][0]


s = Solution()
assert s.maxProfit([1, 2, 3, 0, 2]) == 3
