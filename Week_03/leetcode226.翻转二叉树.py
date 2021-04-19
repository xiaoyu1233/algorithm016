#经典递归题目
#超99%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return #到最底层节点了，不用递归了，终止
        left = self.invertTree(root.left)   #翻转本层的左右子节点，这子节点要保证是已经翻转好的，所以这里进行左节点递归
        right = self.invertTree(root.right) #这里进行右节点递归
        root.left, root.right = right, left #这里将各自翻转好的左右节点进行翻转
        return root #返回父节点
