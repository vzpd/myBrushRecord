from typing import List

from exercise.myUtils import timer

# 用类似快速排序的这种方法理论上，时间复杂度可以达到O（n)
class Solution:
    @timer
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find(l, r, j):
            mid = nums[l]
            index = l
            lindex, rindex = l, r
            while lindex < index or index < rindex:
                while index < rindex:
                    if nums[rindex] < mid:
                        nums[index] = nums[rindex]
                        index = rindex
                    rindex -= 1

                while lindex < index:
                    if nums[lindex] >= mid:
                        nums[index] = nums[lindex]
                        index = lindex
                    lindex += 1

            if r - index >= j:
                return find(index + 1, r, j)
            elif r - index + 1 == j:
                return mid
            else:
                return find(l, index - 1, j - (r - index + 1))

        return find(0, len(nums) - 1, k)


s = Solution()
assert s.findKthLargest([5, 6], 2) == 5
assert s.findKthLargest([6, 5], 2) == 5
assert s.findKthLargest([3, 2, 1, 5, 6, 4], k=2) == 5
assert s.findKthLargest([2, 1], 2) == 1
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1
assert s.findKthLargest([3, 4, 5, 5, 6], k=4) == 4
assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
assert s.findKthLargest([1, 2], 2) == 1
assert s.findKthLargest([1], 1) == 1
assert s.findKthLargest([2, 1], 1) == 2
