from typing import List

from exercise.myUtils import timer


class Solution:
    @timer
    def findBestValue(self, arr: List[int], target: int) -> int:
        #         avg = target / len(arr)
        #         suml = 0
        #         maxv = 0
        #         temp = []
        #         for i in range(len(arr)):
        #             maxv = max(maxv, arr[i])
        #             if arr[i] <= avg:
        #                 suml += arr[i]
        #             else:
        #                 temp.append(arr[i])
        #         if suml == 0:
        #             return int(avg) if avg <= int(avg) + 0.5 else round(avg)
        #         else:
        #             if temp:
        #                 return min(maxv, self.findBestValue(temp, target - suml))
        #             else:
        #                 return maxv
        arr.sort()
        suml = 0
        for i in range(len(arr)):
            diff = target - suml
            avg = diff / (len(arr) - i)
            if avg <= arr[i]:
                return int(avg) if avg <= int(avg) + 0.5 else round(avg)
            suml += arr[i]
        # 可以求出arr的前缀和，然后用二分法查找，这样效率可能会更高

        return arr[-1]


s = Solution()
assert s.findBestValue([1, 2, 2, 2, 5], 11) == 4
assert s.findBestValue([4, 9], 7) == 3
assert s.findBestValue([1, 2, 23, 24, 34, 36], 110) == 30
assert s.findBestValue([2, 3, 5], 11) == 5
assert s.findBestValue(arr=[4, 9, 3], target=10) == 3
assert s.findBestValue(arr=[2, 3, 5], target=10) == 5
assert s.findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803) == 11361
