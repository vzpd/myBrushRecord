# Definition for a binary tree node.
from exercise.myUtils import list2TreeNode, TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 验证范围
        # def validate(node: TreeNode, down=float('-inf'), up=float('inf')):
        #     if not node:
        #         return True
        #     val = node.val
        #     if not down < val < up:
        #         return False
        #     return validate(node.left, down, val) and validate(node.right, val, up)
        #
        # return validate(root)

        # 中序遍历
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not inorder < root.val:
                return False
            inorder = root.val
            root = root.right
        return True


s = Solution()
root = list2TreeNode([2, 1, 3])
assert s.isValidBST(root) is True
root = list2TreeNode([5, 1, 4, None, None, 3, 6])
assert s.isValidBST(root) is False
root = list2TreeNode([5, 1, 7, None, None, 6, 8])
assert s.isValidBST(root) is True
