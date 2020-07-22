# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def getsubtree(nums):
            if not nums:
                return [None]
            res = []
            for i in nums:
                left = getsubtree([x for x in range(nums[0], i)])
                right = getsubtree([x for x in range(i + 1, nums[-1] + 1)])
                for j in range(len(left)):
                    for k in range(len(right)):
                        curr = TreeNode(i)
                        res.append(curr)
                        curr.left = left[j]
                        curr.right = right[k]
            return res

        return getsubtree([x for x in range(1, n + 1)])


s = Solution()
res = s.generateTrees(3)
a = 1
