#可以用递归和中序遍历做，本题递归的核心思想在于要维护节点的上下界，因为二叉搜索树的节点要大于它所有的左节点，小于它所有的右节点，所以节点本身就是一个界。
#递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            return helper(node.right, val, upper) and helper(node.left, lower, val)

        return helper(root)


#中序遍历

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack,inorder = [],float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True