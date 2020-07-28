import collections
from typing import List

from exercise.myUtils import timer


class Solution:
    # @timer
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # if not matrix:
        #     return 0
        # h, l = len(matrix), len(matrix[0])
        # temp = [[0] * l for _ in range(h)]
        #
        # def track(last, i, j):
        #     if 0 <= i < h and 0 <= j < l:
        #         if last > matrix[i][j]:
        #             if temp[i][j] == 0:
        #                 maxlength = 0
        #                 maxlength = max(maxlength, track(matrix[i][j], i + 1, j))
        #                 maxlength = max(maxlength, track(matrix[i][j], i - 1, j))
        #                 maxlength = max(maxlength, track(matrix[i][j], i, j + 1))
        #                 maxlength = max(maxlength, track(matrix[i][j], i, j - 1))
        #                 temp[i][j] = maxlength + 1
        #                 return maxlength + 1
        #             else:
        #                 return temp[i][j]
        #         else:
        #             return 0
        #     else:
        #         return 0
        #
        # ans = 0
        # for i in range(h):
        #     for j in range(l):
        #         ans = max(ans, track(float('inf'), i, j))
        #
        # return ans
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > \
                            matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < \
                            matrix[row][column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))

        return ans


s = Solution()
assert s.longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]) == 4

assert s.longestIncreasingPath([
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]) == 4
