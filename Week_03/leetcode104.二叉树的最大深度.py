#可以用递归和层序遍历做

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


#层序遍历

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        queue = [root,]
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return depth