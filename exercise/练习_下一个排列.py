import bisect
from typing import List



class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index = len(nums) - 1
                while nums[index] <= nums[i - 1]:
                    index -= 1
                # 这里需要主要：
                # 交换后nums[i:]仍然是倒叙排列的
                # 设原来nums[index]位置上的数字为temp
                # 未交换之前，是有序的，index之后的数字均小于temp
                # nums[i-1,index]中的数字均大于temp
                # temp>nums[i-1]，因此交换后仍然有序
                nums[i - 1], nums[index] = nums[index], nums[i - 1]
                j, k = i, len(nums) - 1
                while j < k:
                    nums[j], nums[k] = nums[k], nums[j]
                    j += 1
                    k -= 1
                break
        else:
            nums.reverse()

        print(nums)


s = Solution()
s.nextPermutation([1, 2, 3, 5, 4])
s.nextPermutation([5, 4, 3, 2, 1])
s.nextPermutation([4, 5, 3, 2, 1])
s.nextPermutation([5, 3, 4, 2, 1])
s.nextPermutation([5, 4, 3, 1, 2])
s.nextPermutation([1, 5, 1])
