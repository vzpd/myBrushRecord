# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
#
# 示例 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
#
# 示例 2:
#
# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。
#
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lenDP = [0]

        def island(i, j, index):
            if -1 < i < len(grid) and -1 < j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 0
                lenDP[index] += 1
                return True
            else:
                return False

        def goNext(i, j, index):
            if island(i - 1, j, index):
                goNext(i - 1, j, index)
            if island(i + 1, j, index):
                goNext(i + 1, j, index)
            if island(i, j - 1, index):
                goNext(i, j - 1, index)
            if island(i, j + 1, index):
                goNext(i, j + 1, index)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    lenDP.append(1)
                    goNext(i, j, len(lenDP) - 1)
        return max(lenDP)


s = Solution()
assert s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
assert s.maxAreaOfIsland([[]]) == 0
assert s.maxAreaOfIsland([[0, 0, 0, 1, 0, 1, 0]]) == 1
assert s.maxAreaOfIsland([[0, 0, 0, 1, 0, 0, 0]]) == 1
assert s.maxAreaOfIsland([[0, 0, 0, 1, 1, 0, 0, 0]]) == 2
