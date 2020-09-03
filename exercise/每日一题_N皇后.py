from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def next(virtical, lbans, rbans,  x):
            if x == n:
                temp = [['.'] * n for i in range(n)]
                for i, h in enumerate(virtical):
                    temp[i][h] = 'Q'
                ans.append([''.join(h) for h in temp])
            else:
                for i in range(n):
                    lban, rban = x - i, x + i
                    if i not in virtical and lban not in lbans and rban not in rbans:
                        next(virtical+[i],  lbans + [lban], rbans+[rban], x+1)

        next([],  [], [], 0)

        return ans


s = Solution()
assert s.solveNQueens(4) == [
    [".Q..",
     "...Q",
     "Q...",
     "..Q."],
    ["..Q.",
     "Q...",
     "...Q",
     ".Q.."]


]

s.solveNQueens(8)
