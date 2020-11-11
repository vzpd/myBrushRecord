import collections
from functools import lru_cache

from exercise.myUtils import timer


class Solution:
    @timer
    def findRotateSteps(self, ring: str, key: str) -> int:
        d = collections.defaultdict(set)
        for i, x in enumerate(ring):
            d[x].add(i)

        @lru_cache(None)
        def get_dist(m, n):
            l = abs(m - n)
            return min(l, len(ring) - l)

        dp = [[0, 0]]
        for i in range(len(key)):
            temp = []
            for j in d[key[i]]:
                t = float('inf')
                for k, index in dp:
                    t = min(t, get_dist(j, index) + k)
                temp.append([t + 1, j])
            dp = temp

        return min(dp)[0]


s = Solution()
assert s.findRotateSteps(ring="godding", key="gd") == 4
assert s.findRotateSteps("abcde", "ade") == 6
assert s.findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")
