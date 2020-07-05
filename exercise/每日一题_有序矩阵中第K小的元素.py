"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
"""
"""
矩阵搜索
"""
import bisect
from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n = len(matrix)
        # dp = [[matrix[0][0], 0, 0]]
        # temp = set((0, 0))
        # i = 0
        # while True:
        #     v, x, y = dp[i]
        #     i += 1
        #     if i == k:
        #         return dp[i - 1][0]
        #     if x + 1 < n and (x + 1, y) not in temp:
        #         bisect.insort_left(dp, [matrix[x + 1][y], x + 1, y], i)
        #         temp.add((x + 1, y))
        #     if y + 1 < n and (x, y + 1) not in temp:
        #         bisect.insort_left(dp, [matrix[x][y + 1], x, y + 1], i)
        #         temp.add((x, y + 1))
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


s = Solution()
assert s.kthSmallest([[1, 3, 5],
                      [6, 7, 12],
                      [11, 14, 14]]
                     , 8) == 14

assert s.kthSmallest([[1, 3, 9],
                      [2, 7, 12],
                      [11, 14, 14]]
                     , 3) == 3
assert s.kthSmallest([[1, 3, 5],
                      [6, 7, 12],
                      [11, 14, 14]]
                     , 3) == 5

assert s.kthSmallest([[1, 3, 5],
                      [6, 7, 12],
                      [11, 14, 14]]
                     , 9) == 14

assert s.kthSmallest([[1, 3, 5],
                      [6, 7, 12],
                      [11, 14, 14]], 6) == 11

assert s.kthSmallest([[1, 5, 9],
                      [10, 11, 13],
                      [12, 13, 15]
                      ],
                     k=8) == 13

assert s.kthSmallest([[1, 5, 9],
                      [10, 11, 13],
                      [12, 13, 15]
                      ],
                     k=2) == 5

assert s.kthSmallest([[1, 5, 9],
                      [10, 11, 13],
                      [12, 13, 15]
                      ],
                     k=1) == 1

assert s.kthSmallest([[1]], 1) == 1
