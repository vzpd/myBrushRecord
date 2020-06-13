from typing import List


#
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def next(i, j):
            if i > j:
                return 0
            count = len(piles) - i - j
            if count % 2 == 1:
                return max(piles[i] + next(i + 1, j), piles[j] + next(i, j - 1))
            else:
                return max(-piles[i] + next(i + 1, j), -piles[j] + next(i, j - 1))

        i, j = 0, len(piles) - 1
        return next(i, j) > 0


s = Solution()
assert s.stoneGame([6, 9, 4, 3, 9, 8]) is True
assert s.stoneGame([5, 3, 4, 5]) is True
assert s.stoneGame([5, 2, 19, 6]) is True
assert s.stoneGame([1, 2, 19, 4, 5, 6]) is True
assert s.stoneGame([8, 9, 7, 6, 7, 6]) is True
