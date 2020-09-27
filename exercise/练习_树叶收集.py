from exercise.myUtils import timer


class Solution:
    @timer
    def minimumOperations(self, leaves: str) -> int:
        r, ry, ryr = 0 if leaves[0] == 'r' else 1, float('inf'), float('inf')
        for i in range(1, len(leaves)):
            if leaves[i] == 'r':
                r, ry, ryr = r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr) + 1

        return ryr


s = Solution()
assert s.minimumOperations(
    "yyyrrrrrrrryyrrryryyyyyyyyyyrrrr") == 6
