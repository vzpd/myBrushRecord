from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # dungeon[0][0] = [[dungeon[0][0], dungeon[0][0]]]
        #
        # for i in range(len(dungeon)):
        #     for j in range(len(dungeon[0])):
        #         if i > 0 or j > 0:
        #             pre = []
        #             if i > 0:
        #                 pre += dungeon[i - 1][j]
        #             if j > 0:
        #                 pre += dungeon[i][j - 1]
        #             curr = dungeon[i][j]
        #             dungeon[i][j] = []
        #             for k in range(len(pre)):
        #                 left = pre[k][1] + curr
        #                 dungeon[i][j].append([min(left, pre[k][0]), left])
        #             dungeon[i][j].sort()
        #             for k in range(len(dungeon[i][j]) - 2, -1, -1):
        #                 if dungeon[i][j][k][1] <= dungeon[i][j][k + 1][1]:
        #                     dungeon[i][j].pop(k)
        #
        # ans = max([x[0] for x in dungeon[-1][-1]])
        # return 1 if ans >= 0 else -ans + 1
        m, n = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1 or j < n - 1:
                    a, b = float('inf'), float('inf')
                    if i < m - 1:
                        a = dungeon[i + 1][j] - dungeon[i][j]
                    if j < n - 1:
                        b = dungeon[i][j + 1] - dungeon[i][j]
                    dungeon[i][j] = max(min(a, b), 1)

        return dungeon[0][0]


s = Solution()
assert s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
assert s.calculateMinimumHP([[0, 0, 0], [-1, 0, 0], [2, 0, -2]]) == 2
assert s.calculateMinimumHP([[-2, -3, 3]]) == 6
