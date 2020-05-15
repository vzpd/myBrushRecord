# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
#
# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
#
# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。
#
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
#
#  
#
# 示例 1：
#
# 输入：2
# 输出：true
# 解释：爱丽丝选择 1，鲍勃无法进行操作。
# 示例 2：
#
# 输入：3
# 输出：false
# 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
#  
#
# 提示：
#
# 1 <= N <= 1000
from exercise.myUtils import count_time


class Solution:
    @count_time
    def divisorGame(self, N: int) -> bool:
        # 动态规划
        # N为1时，轮到时，谁输，dp[1]=True
        # N为2时，轮到谁，谁赢, dp[2]=False
        # N为3时，轮到谁，谁赢, dp[3]=True
        # 。。。。。
        # 不论N为多少，因为0<x<N，所以，不管x选多少时，N-x都可以在dp中找到，如果dp[N-x]为False时，此时必赢。
        dp = [None, False]
        for x in range(2, N + 1):
            for y in range(1, x // 2 + 1):
                if x % y == 0 and not dp[x - y]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        print(dp)
        return dp[N]
        # return N % 2 == 0


s = Solution()
assert s.divisorGame(1) == False
assert s.divisorGame(2) == True
assert s.divisorGame(3) == False
assert s.divisorGame(4) == True
assert s.divisorGame(1000) == True
