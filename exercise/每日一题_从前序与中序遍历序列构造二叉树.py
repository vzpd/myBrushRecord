# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

# 分治
# 先序遍历后结构如右所示：【根节点，左子树，右子树】
# 中序遍历后结构如右所示：【左子树，根节点，右子树】
# 因此我们可以用分治的方法解
# 先把先序遍历的第一个值设为根节点的值
# 根据题目中的条件：树中没有重复的值
# 所以我们可以根据根节点的值在中序遍历中找到根节点的值的位置i
# i左侧为左子树的中序遍历结果，i右侧为右子树中序遍历的结果
# 同时我们根据上面左右子树的长度，在先序遍历结果的二维数组中分别左右子树的先序遍历结果
# 然后用左子树的先、中序遍历结果递归求出左子树的根节点，设为根节点的左节点
# 右节点求法相同
# 这样我们递归完就可以遍历完了整棵树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                index = i
                break
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])
        return root


s = Solution()
root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
a = 1
