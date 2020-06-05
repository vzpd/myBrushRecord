from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # res = []
        # while matrix:
        #     res += matrix[0]
        #     matrix.pop(0)
        #
        #     i = 0
        #     while i < len(matrix):
        #         res.append(matrix[i].pop(-1))
        #         i += 1
        #
        #     if matrix and matrix[-1]:
        #         res += matrix[-1][::-1]
        #     else:
        #         break
        #     matrix.pop(-1)
        #
        #     i -= 2
        #     while i > -1 and matrix[i]:
        #         res.append(matrix[i].pop(0))
        #         if not matrix[i]:
        #             matrix.pop(i)
        #         i -= 1
        #
        # return res
        if not matrix:
            return []
        res = []
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while t <= b or l <= r:
            res += matrix[t][l:r + 1]
            t += 1
            if l <= r:
                res += [matrix[i][r] for i in range(t, b + 1)]
            r -= 1
            if t <= b:
                res += matrix[b][l:r + 1][::-1]
            b -= 1
            if l <= r:
                res += [matrix[i][l] for i in range(b, t - 1, -1)]
            l += 1
        return res


s = Solution()
assert s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert s.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
assert s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert s.spiralOrder([[1]]) == [1]
assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
assert s.spiralOrder([]) == []
