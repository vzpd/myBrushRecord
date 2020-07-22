from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def minArray(self, numbers: List[int]) -> int:
        if numbers[0] < numbers[-1]:
            return numbers[0]

        l, r = 0, len(numbers) - 1
        while l < r and numbers[l] == numbers[l + 1]:
            l += 1
        while l < r and numbers[r - 1] == numbers[r]:
            r -= 1
        while l < r - 1:
            mid = (l + r) // 2
            if numbers[l] <= numbers[mid]:
                l = mid
            elif numbers[mid] <= numbers[r]:
                r = mid

        return numbers[r]


        # low, high = 0, len(numbers) - 1
        # while low < high:
        #     pivot = low + (high - low) // 2
        #     if numbers[pivot] < numbers[high]:
        #         high = pivot
        #     elif numbers[pivot] > numbers[high]:
        #         low = pivot + 1
        #     else:
        #         high -= 1
        # return numbers[low]

s = Solution()
assert s.minArray([10, 1, 10, 10, 10]) == 1
assert s.minArray([10, 10, 11, 1, 10, 10, 10]) == 1
assert s.minArray([3, 4, 5, 1, 2]) == 1
assert s.minArray([3, 1, 1]) == 1
assert s.minArray([3, 3, 1, 1]) == 1
assert s.minArray([1]) == 1
assert s.minArray([1, 1, 1, 1]) == 1
assert s.minArray([1, 1, 1, 2, 2, 2]) == 1
assert s.minArray([1, 2]) == 1
assert s.minArray([1, 2, 3]) == 1
assert s.minArray([1, 3, 5]) == 1
assert s.minArray([1, 3, 5, 5]) == 1
