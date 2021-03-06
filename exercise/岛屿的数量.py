# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def numIslands(self, grid: List[List[str]]) -> int:
        def findIsland(i, j):
            if -1 < i < len(grid) and -1 < j < len(grid[i]):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    findIsland(i, j - 1)
                    findIsland(i, j + 1)
                    findIsland(i - 1, j)
                    findIsland(i + 1, j)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    findIsland(i, j)
                    count += 1

        return count


s = Solution()
# assert s.numIslands([]) == 0
assert s.numIslands([['0']]) == 0
assert s.numIslands(
    [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]) == 1
assert s.numIslands(
    [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]) == 3
assert s.numIslands([['1', '1', '0', '1', '1'], [0, '1', '1', '1', 0]]) == 1
assert s.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]) == 1
