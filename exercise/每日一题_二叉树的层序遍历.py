# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from exercise.myUtils import TreeNode, list2TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        curr = [root]
        while curr:
            currRes = []
            next = []
            for x in curr:
                currRes.append(x.val)
                if x.left:
                    next.append(x.left)
                if x.right:
                    next.append(x.right)
            res.append(currRes)
            curr = next
        return res


s = Solution()
root = list2TreeNode([3, 9, 20, None, None, 15, 7])
assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]
assert s.levelOrder(None) == []
root = list2TreeNode([3, 9])
assert s.levelOrder(root) == [[3], [9]]
