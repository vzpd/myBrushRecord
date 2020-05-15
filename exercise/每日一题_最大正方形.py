from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # f(i,j) = min( f(i-1,j), f(i,j-1), f(i-1,j-1) ) + 1
        if not matrix:
            return 0
        maxLength = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i == 0 or j == 0:
                    maxLength = max(maxLength, matrix[i][j])
                elif matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                    maxLength = max(maxLength, matrix[i][j])
        return maxLength ** 2


s = Solution()
# assert s.maximalSquare([[]]) == 0
# assert s.maximalSquare([[1], [1], [1]]) == 1
# assert s.maximalSquare([[0]]) == 0
# assert s.maximalSquare([[1]]) == 1
# assert s.maximalSquare([[1, 1, 1]]) == 1
# assert s.maximalSquare([[1, 0, 1, 0, 0],
#                         [1, 0, 1, 1, 1],
#                         [1, 1, 1, 1, 1],
#                         [1, 0, 0, 1, 0]]) == 4
assert s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 4
