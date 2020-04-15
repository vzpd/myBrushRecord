# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def testArea(i, j, length):
            if j + length - 1 < len(matrix) and i + length - 1 < len(matrix[j + length - 1]):
                for x in range(length):
                    if matrix[j + length - 1][i + x] == '0' or matrix[j + x][i + length - 1] == '0':
                        return 0
            else:
                return 0

            return max(length ** 2, testArea(i, j, length + 1))

        maxArea = 0
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if matrix[j][i] == "1":
                    maxArea = max(1, maxArea, testArea(i, j, 2))
        return maxArea


s = Solution()
print(s.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))
assert s.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]) == 4
# assert s.maximalSquare([[1, 0, 1, 0, 0],
#                         [1, 0, 1, 1, 1],
#                         [1, 1, 1, 1, 1],
#                         [1, 0, 0, 1, 0]]) == 4
# assert s.maximalSquare([[1]]) == 1
# assert s.maximalSquare([[1, 1]]) == 1
# assert s.maximalSquare([[1, 1, 2]]) == 1
# assert s.maximalSquare([[]]) == 0
